import assert from "node:assert/strict";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  requestWithRetry,
  resolveLatestApprovedRelease,
  updateConsumerRelease,
} from "./resolve-reviewed-release.mjs";

const sha = (character) => character.repeat(40);

function jsonResponse(value, { status = 200, statusText = "OK", headers = {} } = {}) {
  const normalizedHeaders = new Map(Object.entries(headers).map(([key, val]) => [key.toLowerCase(), String(val)]));
  return {
    ok: status >= 200 && status < 300,
    status,
    statusText,
    headers: { get: (name) => normalizedHeaders.get(String(name).toLowerCase()) ?? null },
    async json() { return value; },
  };
}

function releaseFetch(history, metadataBySha) {
  return async (url) => {
    const text = String(url);
    if (text.includes("/commits?path=version.json")) return jsonResponse(history);
    const match = text.match(/\/([0-9a-f]{40})\/version\.json$/);
    if (!match || !metadataBySha.has(match[1])) return jsonResponse({}, { status: 404, statusText: "Not Found" });
    return jsonResponse(metadataBySha.get(match[1]));
  };
}

async function testApprovedBoundaryResolution() {
  const candidate110 = sha("a");
  const approved19MetadataEdit = sha("b");
  const approved19Boundary = sha("c");
  const candidate19 = sha("d");
  const approved18 = sha("e");
  const history = [candidate110, approved19MetadataEdit, approved19Boundary, candidate19, approved18]
    .map((value) => ({ sha: value }));
  const metadata = new Map([
    [candidate110, { name: "@johnnyzli/web-design-system", version: "1.10.0", status: "implementation-candidate" }],
    [approved19MetadataEdit, { name: "@johnnyzli/web-design-system", version: "1.9.0", status: "approved" }],
    [approved19Boundary, { name: "@johnnyzli/web-design-system", version: "1.9.0", status: "approved" }],
    [candidate19, { name: "@johnnyzli/web-design-system", version: "1.9.0", status: "implementation-candidate" }],
    [approved18, { name: "@johnnyzli/web-design-system", version: "1.8.2", status: "approved" }],
  ]);

  const release = await resolveLatestApprovedRelease({
    requestOptions: { fetchImpl: releaseFetch(history, metadata), sleepImpl: async () => {} },
  });
  assert.deepEqual(release, {
    package: "@johnnyzli/web-design-system",
    version: "1.9.0",
    sourceCommit: approved19Boundary,
  });
}

async function testRetryPolicy() {
  let attempts = 0;
  const sleeps = [];
  const response = await requestWithRetry("https://example.invalid", "application/json", {
    fetchImpl: async () => {
      attempts += 1;
      if (attempts === 1) return jsonResponse({}, { status: 504, statusText: "Gateway Timeout" });
      return jsonResponse({ ok: true });
    },
    sleepImpl: async (milliseconds) => sleeps.push(milliseconds),
  });
  assert.equal(response.status, 200);
  assert.equal(attempts, 2);
  assert.deepEqual(sleeps, [250]);

  attempts = 0;
  await assert.rejects(
    requestWithRetry("https://example.invalid", "application/json", {
      fetchImpl: async () => {
        attempts += 1;
        return jsonResponse({}, { status: 404, statusText: "Not Found" });
      },
      sleepImpl: async () => assert.fail("404 must not be retried"),
    }),
    /404 Not Found/,
  );
  assert.equal(attempts, 1);

  attempts = 0;
  await requestWithRetry("https://example.invalid", "application/json", {
    fetchImpl: async () => {
      attempts += 1;
      if (attempts === 1) throw new Error("temporary DNS failure");
      return jsonResponse({ ok: true });
    },
    sleepImpl: async () => {},
  });
  assert.equal(attempts, 2);
}

async function testConsumerWrite() {
  const approved = sha("f");
  const candidate = sha("1");
  const history = [{ sha: approved }, { sha: candidate }];
  const metadata = new Map([
    [approved, { name: "@johnnyzli/web-design-system", version: "2.0.0", status: "approved" }],
    [candidate, { name: "@johnnyzli/web-design-system", version: "2.0.0", status: "implementation-candidate" }],
  ]);
  const directory = await mkdtemp(join(tmpdir(), "wds-release-test-"));
  const previous = process.cwd();
  try {
    process.chdir(directory);
    await writeFile("package.json", `${JSON.stringify({ dependencies: { other: "1.0.0" } }, null, 2)}\n`);
    const release = await updateConsumerRelease({
      packageJson: "package.json",
      requestOptions: { fetchImpl: releaseFetch(history, metadata), sleepImpl: async () => {} },
    });
    assert.equal(release.sourceCommit, approved);
    const lock = JSON.parse(await readFile("design-system.lock.json", "utf8"));
    assert.deepEqual(lock, release);
    const manifest = JSON.parse(await readFile("package.json", "utf8"));
    assert.equal(manifest.dependencies.other, "1.0.0");
    assert.equal(
      manifest.dependencies["@johnnyzli/web-design-system"],
      `github:JohnnyZLi/Web-Design-System#${approved}`,
    );
  } finally {
    process.chdir(previous);
    await rm(directory, { recursive: true, force: true });
  }
}

await testApprovedBoundaryResolution();
await testRetryPolicy();
await testConsumerWrite();
console.log("Reviewed-release resolver tests passed.");
