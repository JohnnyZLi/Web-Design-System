import assert from "node:assert/strict";
import { validateReleaseTransition } from "./validate-release-boundary.mjs";

const approved = (version) => ({ version, status: "approved" });
const candidate = (version) => ({ version, status: "implementation-candidate" });

assert.equal(
  validateReleaseTransition({ base: approved("1.9.0"), current: approved("1.9.0"), changedFiles: ["README.md", ".github/workflows/validate.yml"] }).kind,
  "non-release",
);
assert.throws(
  () => validateReleaseTransition({ base: approved("1.9.0"), current: approved("1.9.0"), changedFiles: ["styles/index.css"] }),
  /without a version bump/,
);
assert.equal(
  validateReleaseTransition({ base: approved("1.9.0"), current: candidate("1.9.1"), changedFiles: ["scripts/site-controls.js"] }).kind,
  "candidate",
);
assert.throws(
  () => validateReleaseTransition({ base: approved("1.9.0"), current: candidate("1.8.9"), changedFiles: ["styles/index.css"] }),
  /must increase/,
);
assert.throws(
  () => validateReleaseTransition({ base: approved("1.9.0"), current: approved("1.9.1"), changedFiles: ["styles/index.css"] }),
  /must enter main as implementation-candidate/,
);
assert.throws(
  () => validateReleaseTransition({ base: approved("1.9.0"), current: candidate("1.9.1"), changedFiles: ["README.md"] }),
  /without release-payload changes/,
);
assert.equal(
  validateReleaseTransition({ base: candidate("1.9.1"), current: approved("1.9.1"), changedFiles: ["docs/MIGRATION.md"] }).kind,
  "approval",
);
assert.throws(
  () => validateReleaseTransition({ base: candidate("1.9.1"), current: approved("1.9.1"), changedFiles: ["styles/index.css"] }),
  /without a version bump/,
);
assert.throws(
  () => validateReleaseTransition({ base: approved("1.9.0"), current: candidate("1.9.0"), changedFiles: [] }),
  /Invalid status transition/,
);

console.log("Release-boundary tests passed.");
