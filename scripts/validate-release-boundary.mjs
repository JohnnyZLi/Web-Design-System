import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const VERSION = /^\d+\.\d+\.\d+$/;
const STATUS_CANDIDATE = "implementation-candidate";
const STATUS_APPROVED = "approved";
const ALLOWED_STATUS = new Set([STATUS_CANDIDATE, STATUS_APPROVED]);

const RELEASE_PAYLOAD_FILES = new Set([
  "LICENSE",
  "package.json",
  "scripts/conformance-runner.mjs",
  "scripts/consumer-release.mjs",
  "scripts/site-controls.d.ts",
  "scripts/site-controls.js",
  "scripts/theme-bootstrap.js",
]);
const RELEASE_PAYLOAD_PREFIXES = ["conformance/", "styles/", "tokens/"];

function parseVersion(value, label) {
  const version = String(value ?? "");
  if (!VERSION.test(version)) throw new Error(`${label} has an invalid semantic version: ${version || "<empty>"}`);
  return version.split(".").map(Number);
}

function compareVersions(left, right) {
  for (let index = 0; index < 3; index += 1) {
    if (left[index] !== right[index]) return left[index] - right[index];
  }
  return 0;
}

function validateMetadata(metadata, label) {
  const version = String(metadata?.version ?? "");
  const status = String(metadata?.status ?? "");
  parseVersion(version, label);
  if (!ALLOWED_STATUS.has(status)) throw new Error(`${label} has unsupported release status: ${status || "<empty>"}`);
  return { version, status };
}

export function isReleasePayload(path) {
  const normalized = String(path).replaceAll("\\", "/");
  return RELEASE_PAYLOAD_FILES.has(normalized)
    || RELEASE_PAYLOAD_PREFIXES.some((prefix) => normalized.startsWith(prefix));
}

export function validateReleaseTransition({ base, current, changedFiles }) {
  const previous = validateMetadata(base, "Base version.json");
  const next = validateMetadata(current, "Current version.json");
  const payloadChanges = [...changedFiles].filter(isReleasePayload);
  const payloadChanged = payloadChanges.length > 0;
  const versionChanged = previous.version !== next.version;
  const statusChanged = previous.status !== next.status;

  if (payloadChanged && !versionChanged) {
    throw new Error(
      `Release payload changed without a version bump: ${payloadChanges.join(", ")}. `
      + "Bump the design-system version and mark it implementation-candidate.",
    );
  }

  if (versionChanged) {
    const direction = compareVersions(parseVersion(next.version, "Current version.json"), parseVersion(previous.version, "Base version.json"));
    if (direction <= 0) throw new Error(`Design-system version must increase from ${previous.version}; received ${next.version}.`);
    if (!payloadChanged) throw new Error(`Version changed from ${previous.version} to ${next.version} without release-payload changes.`);
    if (next.status !== STATUS_CANDIDATE) {
      throw new Error(`New version ${next.version} must enter main as ${STATUS_CANDIDATE}, not ${next.status}.`);
    }
    return { kind: "candidate", version: next.version, payloadChanges };
  }

  if (statusChanged) {
    if (previous.status === STATUS_CANDIDATE && next.status === STATUS_APPROVED && !payloadChanged) {
      return { kind: "approval", version: next.version, payloadChanges: [] };
    }
    throw new Error(`Invalid status transition for ${next.version}: ${previous.status} -> ${next.status}.`);
  }

  return { kind: "non-release", version: next.version, payloadChanges: [] };
}

function git(...args) {
  return execFileSync("git", args, { encoding: "utf8" }).trim();
}

function baseMetadata(baseSha) {
  return JSON.parse(git("show", `${baseSha}:version.json`));
}

function changedFiles(baseSha) {
  const output = git("diff", "--name-only", `${baseSha}...HEAD`);
  return output ? output.split(/\r?\n/).filter(Boolean) : [];
}

const invokedPath = process.argv[1] ? resolve(process.argv[1]) : null;
if (invokedPath === fileURLToPath(import.meta.url)) {
  try {
    const baseSha = process.argv[2];
    if (!/^[0-9a-f]{40}$/.test(String(baseSha ?? ""))) {
      throw new Error("Usage: node scripts/validate-release-boundary.mjs <base-sha>");
    }
    const current = JSON.parse(await readFile(resolve("version.json"), "utf8"));
    const result = validateReleaseTransition({
      base: baseMetadata(baseSha),
      current,
      changedFiles: changedFiles(baseSha),
    });
    console.log(`Release boundary validated: ${result.kind} (${result.version}).`);
  } catch (error) {
    console.error(`Error: ${error?.message ?? error}`);
    process.exitCode = 1;
  }
}
