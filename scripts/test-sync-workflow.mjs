import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const workflow = await readFile(".github/workflows/consumer-design-system-sync.yml", "utf8");

for (const fragment of [
  "package-json:",
  "repository: ${{ job.workflow_repository }}",
  "ref: ${{ job.workflow_sha }}",
  "path: .design-system-tooling",
  ".design-system-tooling/scripts/resolve-reviewed-release.mjs",
  "npm run design-system:sync",
  "git push --force origin \"HEAD:${branch}\"",
  "GitHub Actions is not permitted to create or approve pull requests",
  "Design-system update branch published",
  "exit \"$create_status\"",
]) {
  assert.ok(workflow.includes(fragment), `consumer sync workflow is missing: ${fragment}`);
}

const resolveIndex = workflow.indexOf(".design-system-tooling/scripts/resolve-reviewed-release.mjs");
const installIndex = workflow.indexOf("- name: Install dependencies");
const syncIndex = workflow.indexOf("- name: Synchronize generated assets");
const validateIndex = workflow.indexOf("- name: Validate update");
const pushIndex = workflow.indexOf('git push --force origin "HEAD:${branch}"');
const createIndex = workflow.indexOf("gh pr create --draft");
assert.ok(resolveIndex >= 0 && installIndex > resolveIndex, "release resolution must happen before dependency installation");
assert.ok(syncIndex > installIndex, "asset synchronization must happen after dependency installation");
assert.ok(validateIndex > syncIndex, "consumer validation must happen before publication");
assert.ok(pushIndex > validateIndex && createIndex > pushIndex, "validated update branch must be published before pull-request creation");
assert.doesNotMatch(workflow, /^\s*run:\s*npm run design-system:update\s*$/m, "consumer-owned release resolution must not remain active");
assert.ok(workflow.includes("persist-credentials: false"), "tooling checkout must not persist credentials");

console.log("Consumer sync workflow tests passed.");
