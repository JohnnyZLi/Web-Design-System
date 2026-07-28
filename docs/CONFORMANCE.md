# Design-system conformance

This document defines how the human-readable requirements in `docs/DESIGN-SYSTEM.md` are converted into auditable consumer evidence without making product repositories identical.

## Sources of truth

- `docs/DESIGN-SYSTEM.md` remains the normative human-readable specification.
- `conformance/contract.json` assigns stable rule IDs and machine-readable applicability, severity, evidence classes, and canonical source sections.
- Each consumer owns a `design-system.conformance.json` manifest that points to repository-local evidence.
- Product tests, builds, visual audits, and deployment checks remain product-owned and are invoked by product CI.

The runner does not parse prose from Markdown and does not execute consumer commands. This prevents wording changes from silently changing tests and preserves the consumer repository as the owner of its build and application behavior.

## Rule identifiers

Rules use the form `DS-CATEGORY-NNN`.

Examples:

- `DS-DIST-001` — immutable package and commit metadata
- `DS-HEADER-001` — shared global-header contract
- `DS-DIALOG-002` — dialog accessible naming and focus recovery
- `DS-RESP-002` — actual 200 percent browser zoom review

Rule IDs are stable. A material change to a rule updates its description or adds a new rule rather than reusing the ID for unrelated behavior.

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

Manual items exist for checks that automation cannot honestly reproduce, including real browser zoom, assistive-technology review, and final performance approval. Pending manual items are recorded but do not block normal pull requests. `--strict-manual` blocks them for a final release sign-off.

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

## Report behavior

The runner writes:

- `design-system-conformance/report.json`
- `design-system-conformance/report.md`

Each result includes the rule ID, severity, status, and evidence details. Required automated failures block the command. Advisory failures are reported. Manual failures block. Manual pending items block only under `--strict-manual`.

## Runtime test ownership

The conformance manifest proves that required product-owned checks and assertions exist. The product pipeline still runs them directly.

Current runtime layers include:

- Portfolio page and navigation visual audit
- Network Diagnostics state, profile, dialog, and report audit
- RolePacket authenticated workflow and workspace-drawer audit
- Product-specific typechecks, unit tests, browser tests, builds, deployment checks, and security scans

The common testbench standardizes the contract and report format while product adapters continue to create meaningful states.

## Responsive terminology

A reduced viewport approximates available layout width but is not called actual browser zoom. Automated suites use names such as `narrow-desktop` for those viewports. Actual 200 percent browser zoom remains a manual release item until the browser runner can reproduce and validate it reliably.

## Security boundary

The runner resolves evidence, manifest, and output paths against the consumer repository root. Escaping paths fail. The runner contains no subprocess execution and cannot run arbitrary commands from a manifest.

The reusable workflow accepts a consumer-owned conformance command because GitHub Actions already treats workflow inputs as code owned by the calling repository. The shared runner itself remains data-only.

## Release sequence

1. Update the design-system specification and machine-readable contract.
2. Validate the contract, runner, package exports, and self-test.
3. Merge the reviewed design-system release.
4. Update consumers independently and retain independent rollback boundaries.
5. Run static, runtime, visual, accessibility, build, and product tests.
6. Enable the cross-consumer design-system release gate after all consumers support the current contract.
7. Use strict manual mode only for final release approval.
