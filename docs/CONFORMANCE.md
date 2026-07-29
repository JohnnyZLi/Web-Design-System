# Design-system conformance

This document defines how the human-readable requirements in `docs/DESIGN-SYSTEM.md` become auditable consumer evidence without making the product repositories identical.

## Sources of truth

- `docs/DESIGN-SYSTEM.md` is the normative human-readable specification.
- `conformance/contract.json` assigns stable rule IDs and machine-readable applicability, severity, evidence classes, and canonical source sections.
- `conformance/manifest.schema.json` defines the accepted consumer declaration and evidence shape.
- Each consumer owns a `design-system.conformance.json` manifest that points to repository-local evidence.
- Each consumer records the package version and immutable source commit in `design-system.lock.json`.
- Product tests, builds, visual audits, deployment checks, and state fixtures remain product-owned and are invoked by product CI.

The runner does not parse prose from Markdown and does not execute consumer commands. This prevents wording changes from silently changing tests and preserves each product repository as the owner of its build and application behavior.

## Rule identifiers

Rules use the form `DS-CATEGORY-NNN`.

Examples:

- `DS-DIST-001` — immutable package and source metadata
- `DS-HEADER-001` — shared global-header contract
- `DS-DIALOG-002` — dialog accessible naming and focus recovery
- `DS-RESP-002` — actual 200 percent browser zoom review

Rule IDs are stable. A material change updates a rule description or adds a new rule rather than reusing an ID for unrelated behavior.

## Evidence types

The shared runner accepts repository-confined evidence declarations:

- `file-exists`
- `contains`
- `not-contains`
- `matches`
- `json-equals`
- `json-matches`

A consumer manifest may also declare:

- `manual-passed`
- `manual-pending`
- `manual-failed`

Manual items exist for checks that automation cannot honestly reproduce, including actual browser zoom, assistive-technology review, and final performance approval. Pending manual items are recorded but do not block normal pull requests. `--strict-manual` blocks them for final release sign-off.

## Consumer manifest

A consumer manifest has this shape:

```json
{
  "schemaVersion": "1.0.0",
  "product": "network",
  "outputDirectory": "design-system-conformance",
  "rules": {
    "DS-DIST-001": {
      "evidence": [
        {
          "type": "json-matches",
          "file": "design-system.lock.json",
          "path": "sourceCommit",
          "pattern": "^[0-9a-f]{40}$"
        }
      ]
    },
    "DS-RESP-002": {
      "status": "manual-pending",
      "reason": "Actual 200 percent browser zoom remains a release check."
    }
  }
}
```

Every applicable rule must be declared. Rules that do not apply to a product are omitted and reported automatically as `not-applicable` from the central contract.

The manifest schema rejects:

- Unknown top-level, declaration, or evidence properties
- Unknown products or malformed rule identifiers
- Unsupported evidence types
- Missing files, patterns, values, or JSON paths required by an evidence type
- Manual declarations without a written reason
- A declaration that mixes manual status with automated evidence

## Provenance contract

Before evaluating rule evidence, the runner reads `design-system.lock.json` and verifies:

- The package is `@johnnyzli/web-design-system`.
- The version is a semantic version.
- The source commit is an immutable 40-character commit identifier.
- The consumer lock version equals the conformance contract’s design-system version.

Consumer integration validation separately verifies that synchronized assets, source metadata, local helper copies, and package dependencies match the same lock. Consumer validators derive release identity from the lock rather than hard-coding the previous release, so scheduled update automation can validate a new candidate before it creates an update pull request.

## Report behavior

The runner writes:

- `design-system-conformance/report.json`
- `design-system-conformance/report.md`

Reports include:

- Product identifier
- Contract schema version
- Design-system version
- Immutable design-system source commit
- Consumer commit when `GITHUB_SHA` is available
- Rule severity, status, and evidence details
- Blocking, advisory, and manual summaries

Required automated failures block the command. Advisory failures are reported. Manual failures block. Manual pending items block only under `--strict-manual`.

## Runtime test ownership

The conformance manifest proves that required product-owned checks and assertions exist. The product pipeline still runs them directly.

Current runtime layers include:

- Portfolio page and navigation visual audit
- Network Diagnostics state, profile, dialog, and report audit
- RolePacket authenticated workflow and workspace-drawer audit
- Product-specific typechecks, unit tests, browser tests, builds, deployment checks, and security scans

The common testbench standardizes the contract and report format while product adapters continue to create meaningful states.

## Cross-consumer candidate gate

`.github/workflows/consumer-candidate-gate.yml` validates a design-system candidate against the current default branch of every accessible consumer before the shared change is merged.

For each product, the gate:

1. Checks out the design-system candidate and consumer repository.
2. Points the consumer lock, and package dependency where applicable, at the candidate version and commit.
3. Synchronizes the consumer-owned asset set and provenance record.
4. Runs the consumer’s integration and conformance commands.
5. Runs relevant lint, test, build, and deployment-dry-run commands.

The gate does not publish consumer branches or alter product state. Consumer rollout still occurs through independent pull requests after the shared release is merged.

RolePacket is private. When `ROLEPACKET_REPOSITORY_TOKEN` is configured, the hosted gate validates it directly. When the token is unavailable, the hosted job reports a notice and the release owner must run the repository-owned local fallback before merge:

```bash
npm run validate:rolepacket-local -- --rolepacket /absolute/path/to/RolePacket-repo
```

The local fallback fetches RolePacket `origin/main`, creates an isolated detached worktree, injects the exact design-system candidate version and commit, synchronizes the candidate, runs `verify:local:quick` and the production dependency audit, prints both immutable commits on success, and removes the temporary worktree. It does not change the developer’s active RolePacket checkout.

## Responsive terminology

A reduced viewport approximates available layout width but is not called actual browser zoom. Automated suites use names such as `narrow-desktop` for those viewports. Actual 200 percent browser zoom remains a manual release item until the browser runner can reproduce and validate it reliably.

## Security boundary

The runner resolves evidence, manifest, lock, and output paths against the consumer repository root. Escaping paths fail. The runner contains no subprocess execution and cannot run arbitrary commands from a manifest.

The reusable workflow accepts a consumer-owned conformance command because GitHub Actions already treats workflow inputs as code owned by the calling repository. The shared runner itself remains data-only.

The candidate gate uses immutable action pins, disables persisted checkout credentials, and runs only for branches in the design-system repository or by manual dispatch. The local RolePacket validator executes fixed repository-owned commands only; it does not accept arbitrary command input or modify the caller’s active worktree.

## Release sequence

1. Update the design-system specification and machine-readable contract.
2. Update package, token, schema, and version metadata atomically.
3. Validate the contract, schemas, runner, package exports, generated assets, self-tests, and local fallback syntax.
4. Run the hosted candidate gate against Website and Network Diagnostics.
5. Validate RolePacket through the token-backed hosted job or the repository-owned local fallback.
6. Merge the reviewed design-system release only after package and consumer gates pass.
7. Update consumers independently and retain independent rollback boundaries.
8. Run consumer static, runtime, visual, accessibility, build, deployment, and product tests.
9. Use strict manual mode only for final release approval.
