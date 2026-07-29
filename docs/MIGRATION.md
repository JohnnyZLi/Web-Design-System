# Migration and conformance status

This document records the completed shared-design-system rollout across the owned sites. Historical release details remain in [`CHANGELOG.md`](../CHANGELOG.md).

## Approved direction

The production interfaces remain the approved visual baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The design system removes foundational, behavioral, accessibility, provenance, and maintenance drift without forcing the products into one layout.

## Final rollout matrix

| Repository | Design system | Final state |
| --- | --- | --- |
| Website | v1.8.2 | Lock, package dependency, generated assets, source metadata, reusable workflows, integration validation, conformance, visual audit, quality checks, security scan, CodeQL, performance baseline, and manual accessibility review are aligned. |
| Network Diagnostics | v1.8.2 | Lock, generated assets, helper copies, workflows, integration validation, conformance, tests, build, visual audit, UI regression, security scan, CodeQL, performance baseline, zoom review, forced-colors review, assistive-technology review, and grayscale chart review are aligned. |
| RolePacket | v1.8.2 | Lock, generated assets, helper copies, workflows, integration validation, conformance, typechecks, builds, Cloudflare dry runs, automated tests, visual audit, dependency audit, Semgrep, Gitleaks, performance baseline, and manual accessibility review are aligned. |
| Web Design System | v1.8.2 | Strict manifest validation, provenance-bearing reports, lock-derived consumer validation, cross-consumer candidate gating, performance evidence standards, and final acceptance documentation are complete. |

The migration was accepted on 2026-07-29 after automated validation and repository-owner manual review. Package status is **approved**.

## Shared package capabilities

The approved package provides:

- Versioned atomic tokens and generated CSS
- Exact dot-canvas, focus, selection, reduced-motion, and forced-colors foundations
- Shared global-header geometry and owner/product identity
- Canonical owned-site directory and Sites-menu behavior
- Shared compact header-menu shell and controller
- Reusable action, button, callout, empty-state, table-region, and native-dialog primitives
- A constrained consumer-release resolver
- A reusable consumer synchronization workflow
- A machine-readable conformance contract with stable `DS-*` identifiers
- A strict consumer-manifest schema
- Repository-confined evidence evaluation and provenance-bearing reports
- A cross-consumer release gate for Website, Network Diagnostics, and RolePacket
- Daily deployed-site smoke checks

Product-specific composition, density, charts, forms, workflow state, measurements, and application behavior remain owned by their repositories.

## Manual acceptance record

The repository owner completed and accepted the remaining manual checks on 2026-07-29:

### Website

- Actual 200 percent browser zoom across the homepage and all case studies
- Reduced-motion and forced-colors review
- Keyboard and assistive-technology review
- Initial bundle and browser-timing performance baseline review

### Network Diagnostics

- Actual 200 percent browser zoom of selectors, tables, charts, and imported reports
- Forced-colors and assistive-technology review
- Grayscale chart-meaning review across result states
- Initial application-shell performance baseline review

### RolePacket

- Authenticated actual 200 percent browser zoom across core workflows
- Forced-colors, keyboard, and assistive-technology review
- Initial authenticated-fixture performance baseline review

The consumer conformance manifests record `DS-RESP-002`, `DS-A11Y-002`, and `DS-PERF-001` as `manual-passed`. No blocking manual issue or exception remains from this migration.

## Performance evidence

Each consumer owns a reproducible performance recorder and report artifact. The initial reports were generated, reviewed for fixture and measurement errors, and accepted as engineering references on 2026-07-29. See [`PERFORMANCE-BASELINES.md`](PERFORMANCE-BASELINES.md) for the common evidence standard and interpretation limits.

The initial reports are not universal real-user field claims or rigid budgets. Future blocking thresholds should be based on repeated same-environment runs and an explicit tolerance decision.

## Consumer update tooling

Every consumer:

- Pins an immutable Web Design System source commit
- Resolves updates through the constrained shared helper
- Calls reusable workflows by immutable commit
- Keeps product-specific schedules and validation commands locally
- Includes generated helpers and contracts in drift validation when committed locally
- Retains an independent pull-request and rollback boundary

The synchronization workflow stages configured generated paths before checking for changes, including newly created assets.

## Cross-consumer release gate

Every future Web Design System candidate must validate against the current default branch of all three consumers before merge. The gate:

- Checks out the exact candidate SHA written into consumer lock metadata
- Synchronizes each consumer-owned asset set
- Validates lock and generated-asset provenance
- Evaluates the product conformance manifest
- Runs relevant product lint, tests, builds, and deployment dry runs
- Requires private RolePacket repository access instead of silently skipping that consumer

The Web Design System repository therefore requires `ROLEPACKET_REPOSITORY_TOKEN` with read access to `JohnnyZLi/RolePacket`. Absence of that secret is a blocking gate failure.

## Repository governance

Intended required checks:

### Website

- Design-system conformance
- Web quality
- Visual audit
- Performance baseline
- Secret scan
- CodeQL

### Network Diagnostics

- Design-system conformance
- CI
- Visual audit
- UI regression
- Performance baseline
- Secret scan
- CodeQL

### RolePacket

- Self-hosted macOS validation when private hosted minutes are unavailable
- Design-system conformance
- CI
- Visual audit
- Static analysis
- Secret scan

### Web Design System

- Validate
- Consumer candidate gate: Portfolio
- Consumer candidate gate: Network Diagnostics
- Consumer candidate gate: RolePacket

Repository rulesets must enforce the intended checks before merging. Enforcement must be confirmed in GitHub settings rather than inferred from passing runs.

## Ongoing maintenance

- Re-run manual zoom and accessibility checks after meaningful navigation, layout, or interaction changes.
- Re-record performance baselines after intentional architecture, framework, rendering-state, or asset changes.
- Keep generated assets, source provenance, lock metadata, and workflow pins aligned.
- Register every future exception explicitly instead of allowing undocumented drift.

`RolePacket-Autopilot` remains outside this migration and must not be modified as part of Web Design System maintenance.
