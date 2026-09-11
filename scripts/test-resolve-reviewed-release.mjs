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
const PACKAGE = "@johnnyzli/web-design-system";

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

function releaseFetch({ versionHistory, generalHistory, metadataBySha, packageBySha, detailsBySha, mainSha }) {
  return async (url) => {
    const text = String(url);
    if (text.includes("/commits?path=version.json")) return jsonResponse(versionHistory.map((value) => ({ sha: value })));
    if (text.includes("/commits?sha=")) return jsonResponse(generalHistory.map((value) => ({ sha: value })));
    const commitMatch = text.match(/\/commits\/([0-9a-f]{40}|main)$/);
    if (commitMatch) {
      const ref = commitMatch[1];
      if (ref === "main") return jsonResponse({ sha: mainSha, ...(detailsBySha.get(mainSha) ?? {}) });
      if (detailsBySha.has(ref)) return jsonResponse({ sha: ref, ...detailsBySha.get(ref) });
      return jsonResponse({}, { status: 404, statusText: "Not Found" });
    }
    const rawMatch = text.match(/\/([0-9a-f]{40})\/(version|package)\.json$/);
    if (rawMatch) {
      const [, ref, kind] = rawMatch;
      const source = kind === "version" ? metadataBySha : packageBySha;
      if (source.has(ref)) return jsonResponse(source.get(ref));
    }
    return jsonResponse({}, { status: 404, statusText: "Not Found" });
  };
}

async function testHistoricalApprovedDriftStabilizesAtLatestPackageCommit() {
  const infra = sha("a");
  const latestPackage = sha("b");
  const olderPackage = sha("c");
  const approval = sha("d");
  const candidate = sha("e");
  const versionHistory = [approval, candidate];
  const generalHistory = [infra, latestPackage, olderPackage, approval, candidate];
  const approvedMetadata = { name: PACKAGE, version: "1.9.0", status: "approved" };
  const metadataBySha = new Map([
    [infra, approvedMetadata], [latestPackage, approvedMetadata], [olderPackage, approvedMetadata], [approval, approvedMetadata],
    [candidate, { name: PACKAGE, version: "1.9.0", status: "implementation-candidate" }],
  ]);
  const packageBySha = new Map([[infra, { name: PACKAGE, private: false, files: ["styles/site-identity.css", "version.json"] }]]);
  const detailsBySha = new Map([
    [infra, { files: [{ filename: "docs/CONFORMANCE.md" }] }],
    [latestPackage, { files: [{ filename: "styles/site-identity.css" }] }],
    [olderPackage, { files: [{ filename: "styles/site-identity.css" }] }],
    [approval, { files: [{ filename: "version.json" }] }],
  ]);
  const release = await resolveLatestApprovedRelease({
    requestOptions: {
      fetchImpl: releaseFetch({ versionHistory, generalHistory, metadataBySha, packageBySha, detailsBySha, mainSha: infra }),
      sleepImpl: async () => {},
    },
  });
  assert.deepEqual(release, { package: PACKAGE, version: "1.9.0", sourceCommit: latestPackage });
}

async function testNewerCandidateKeepsPreviousApprovedRelease() {
  const candidateInfra = sha("1");
  const candidate = sha("2");
  const approvedPackage = sha("3");
  const approval = sha("4");
  const olderCandidate = sha("5");
  const versionHistory = [candidate, approval, olderCandidate];
  const metadataBySha = new Map([
    [candidate, { name: PACKAGE, version: "2.0.0", status: "implementation-candidate" }],
    [approvedPackage, { name: PACKAGE, version: "1.9.0", status: "approved" }],
    [approval, { name: PACKAGE, version: "1.9.0", status: "approved" }],
    [olderCandidate, { name: PACKAGE, version: "1.9.0", status: "implementation-candidate" }],
  ]);
  const packageBySha = new Map([[approvedPackage, { name: PACKAGE, private: false, files: ["styles/site-identity.css", "version.json"] }]]);
  const detailsBySha = new Map([
    [candidate, { parents: [{ sha: approvedPackage }], files: [{ filename: "version.json" }] }],
    [approvedPackage, { files: [{ filename: "styles/site-identity.css" }] }],
  ]);
  const release = await resolveLatestApprovedRelease({
    requestOptions: {
      fetchImpl: releaseFetch({
        versionHistory,
        generalHistory: [approvedPackage, approval, olderCandidate],
        metadataBySha,
        packageBySha,
        detailsBySha,
        mainSha: candidateInfra,
      }),
      sleepImpl: async () => {},
    },
  });
  assert.deepEqual(release, { package: PACKAGE, version: "1.9.0", sourceCommit: approvedPackage });
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
    requestWithRetry("https://api.github.com/example", "application/json", {
      fetchImpl: async () => {
        attempts += 1;
        return jsonResponse({}, { status: 403, statusText: "Forbidden" });
      },
      sleepImpl: async () => assert.fail("permission 403 must not be retried"),
      token: "test-token",
    }),
    /403 Forbidden/,
  );
  assert.equal(attempts, 1);
}

async function testConsumerWrite() {
  const approved = sha("f");
  const candidate = sha("6");
  const metadataBySha = new Map([
    [approved, { name: PACKAGE, version: "2.0.0", status: "approved" }],
    [candidate, { name: PACKAGE, version: "2.0.0", status: "implementation-candidate" }],
  ]);
  const packageBySha = new Map([[approved, { name: PACKAGE, private: false, files: ["version.json"] }]]);
  const detailsBySha = new Map([[approved, { files: [{ filename: "version.json" }] }]]);
  const directory = await mkdtemp(join(tmpdir(), "wds-release-test-"));
  const previous = process.cwd();
  try {
    process.chdir(directory);
    await writeFile("package.json", `${JSON.stringify({ dependencies: { other: "1.0.0" } }, null, 2)}\n`);
    const release = await updateConsumerRelease({
      packageJson: "package.json",
      requestOptions: {
        fetchImpl: releaseFetch({
          versionHistory: [approved, candidate],
          generalHistory: [approved, candidate],
          metadataBySha,
          packageBySha,
          detailsBySha,
          mainSha: approved,
        }),
        sleepImpl: async () => {},
      },
    });
    assert.equal(release.sourceCommit, approved);
    assert.deepEqual(JSON.parse(await readFile("design-system.lock.json", "utf8")), release);
    const manifest = JSON.parse(await readFile("package.json", "utf8"));
    assert.equal(manifest.dependencies.other, "1.0.0");
    assert.equal(manifest.dependencies[PACKAGE], `github:JohnnyZLi/Web-Design-System#${approved}`);
  } finally {
    process.chdir(previous);
    await rm(directory, { recursive: true, force: true });
  }
}

await testHistoricalApprovedDriftStabilizesAtLatestPackageCommit();
await testNewerCandidateKeepsPreviousApprovedRelease();
await testRetryPolicy();
await testConsumerWrite();
console.log("Reviewed-release resolver tests passed.");
