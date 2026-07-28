import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const runner = resolve(root, "scripts/conformance-runner.mjs");
const contract = resolve(root, "conformance/contract.json");
const contractMetadata = JSON.parse(await readFile(contract, "utf8"));
const fixture = await mkdtemp(resolve(tmpdir(), "jl-conformance-"));
const sourceCommit = "1234567890123456789012345678901234567890";

const writeLock = async (version = contractMetadata.designSystemVersion) => writeFile(resolve(fixture, "design-system.lock.json"), JSON.stringify({
  package: "@johnnyzli/web-design-system",
  version,
  sourceCommit,
}), "utf8");
await writeLock();
await writeFile(resolve(fixture, "page.html"), '<header class="jl-global-header"><div data-site-switcher></div></header>', "utf8");
await writeFile(resolve(fixture, "audit.yml"), "uses: shared\nwidth: 320\nEscape\nfocus restoration\n", "utf8");
await writeFile(resolve(fixture, "styles.css"), "", "utf8");

const automated = (file, value) => ({ evidence: [{ type: "contains", file, value }] });
const manual = (reason) => ({ status: "manual-pending", reason });
const manifest = {
  schemaVersion: "1.0.0",
  product: "portfolio",
  outputDirectory: "design-system-conformance",
  rules: {
    "DS-DIST-001": { evidence: [
      { type: "json-equals", file: "design-system.lock.json", path: "package", value: "@johnnyzli/web-design-system" },
      { type: "json-matches", file: "design-system.lock.json", path: "sourceCommit", pattern: "^[0-9a-f]{40}$" },
    ] },
    "DS-DIST-002": { evidence: [{ type: "file-exists", file: "audit.yml" }] },
    "DS-HEADER-001": automated("page.html", "jl-global-header"),
    "DS-SITES-001": automated("page.html", "data-site-switcher"),
    "DS-SITES-002": automated("audit.yml", "focus restoration"),
    "DS-PRIMITIVE-001": { evidence: [{ type: "not-contains", file: "styles.css", value: "duplicated-shared-structure" }] },
    "DS-RESP-001": automated("audit.yml", "width: 320"),
    "DS-RESP-002": manual("Actual browser zoom remains manual."),
    "DS-A11Y-001": automated("audit.yml", "Escape"),
    "DS-A11Y-002": manual("Assistive-technology review remains manual."),
    "DS-STATE-002": { evidence: [{ type: "file-exists", file: "page.html" }] },
    "DS-OWN-001": { evidence: [{ type: "file-exists", file: "page.html" }] },
    "DS-WORKFLOW-001": automated("audit.yml", "uses: shared"),
    "DS-TEST-001": { evidence: [{ type: "file-exists", file: "audit.yml" }] },
    "DS-PERF-001": manual("Performance baseline remains manual."),
  },
};
const writeManifest = async () => writeFile(resolve(fixture, "design-system.conformance.json"), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
await writeManifest();

function execute(extra = []) {
  return spawnSync(process.execPath, [runner, "--contract", contract, "--root", fixture, ...extra], {
    encoding: "utf8",
  });
}

const normal = execute([]);
if (normal.status !== 0) throw new Error(`Normal conformance self-test failed: ${normal.stderr || normal.stdout}`);
const report = JSON.parse(await readFile(resolve(fixture, "design-system-conformance/report.json"), "utf8"));
if (report.summary.blockingFailures !== 0 || report.summary.manualPending !== 3) throw new Error("Conformance report summary is incorrect.");
if (report.designSystemVersion !== contractMetadata.designSystemVersion || report.sourceCommit !== sourceCommit) {
  throw new Error("Conformance report provenance is incorrect.");
}
if (!(await readFile(resolve(fixture, "design-system-conformance/report.md"), "utf8")).includes(sourceCommit)) {
  throw new Error("Markdown conformance report is missing provenance.");
}

const strict = execute(["--strict-manual"]);
if (strict.status === 0) throw new Error("Strict manual mode did not block pending manual checks.");

await writeLock("0.0.0");
const mismatch = execute([]);
if (mismatch.status === 0 || !mismatch.stderr.includes("does not match consumer lock")) {
  throw new Error("Conformance runner did not reject mismatched contract and lock versions.");
}
await writeLock();

manifest.rules["DS-PERF-001"] = { status: "manual-pending", reason: "" };
await writeManifest();
const malformed = execute([]);
if (malformed.status === 0 || !malformed.stderr.includes("requires a reason")) {
  throw new Error("Conformance runner did not reject a malformed manual declaration.");
}
manifest.rules["DS-PERF-001"] = manual("Performance baseline remains manual.");

manifest.rules["DS-DIST-002"] = { evidence: [{ type: "file-exists", file: "../outside-repository" }] };
await writeManifest();
const escape = execute([]);
const escapeReport = JSON.parse(await readFile(resolve(fixture, "design-system-conformance/report.json"), "utf8"));
const escapeResult = escapeReport.results.find((result) => result.id === "DS-DIST-002");
if (escape.status === 0 || !escapeResult?.detail.includes("must stay inside the consumer repository")) {
  throw new Error("Conformance runner did not reject an escaping evidence path.");
}

console.log("Conformance runner self-test passed.");
