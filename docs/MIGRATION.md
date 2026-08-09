# Migration and conformance status

This document records the completed shared-design-system rollout across the owned sites. Historical release details remain in [`CHANGELOG.md`](../CHANGELOG.md).

## Approved direction

The production interfaces remain the approved visual baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The design system removes foundational, behavioral, accessibility, provenance, and maintenance drift without forcing the products into one layout.

## Current rollout matrix

| Repository | Design system | Current state |
| --- | --- | --- |
| Website | v1.9.0 | Lock, generated assets, shared dark theme, Sites/Settings disclosures, complete-header pinning, approved wide-desktop rail adapter, source metadata, reusable workflows, integration validation, conformance, visual audit, quality checks, security scan, CodeQL, and performance baseline are aligned. The 2026-07-29 manual accessibility/zoom review remains the historical manual baseline. |
| Network Diagnostics | v1.9.0 | Lock, generated assets, shared dark theme, Sites/Settings disclosures, complete-header pinning, helper copies, workflows, integration validation, conformance, tests, build, visual audit, UI regression, security scan, CodeQL, performance baseline, zoom review, forced-colors review, assistive-technology review, and grayscale chart review are aligned. |
| RolePacket | v1.9.0 | Lock, generated assets, shared dark theme, Sites/Settings disclosures, complete-header pinning, helper copies, workflows, integration validation, conformance, typechecks, builds, Cloudflare dry runs, automated tests, visual audit, dependency audit, Semgrep, Gitleaks, performance baseline, and manual accessibility review are aligned. |
| Web Design System | v1.9.0 | Approved light/dark tokens, separate Sites and Settings controls, unified attached disclosure shells, complete-header pinned and dismissal behavior, strict manifest validation, provenance-bearing reports, lock-derived consumer validation, cross-consumer candidate gating, performance evidence standards, and acceptance documentation are aligned. |

The original shared-system migration was accepted on 2026-07-29 after automated validation and repository-owner manual review. The v1.9.0 appearance and header extension was completed and reconciled with the canonical documentation on 2026-08-08. The final Portfolio product expression, including its product-owned wide-desktop header rail, was recorded on 2026-08-09 without changing the shared runtime package. Package status is **approved**.

## Shared package capabilities

The approved package provides:

- Versioned atomic tokens and generated CSS
- Exact dot-canvas, focus, selection, reduced-motion, and forced-colors foundations
- Shared System, Light, and Dark preference resolution with cross-subdomain persistence
- Warm dark-theme neutral and semantic roles with the primary terracotta family shared across light and dark themes
- Shared global-header control geometry, default rail, owner/product identity, and the documented boundary for approved product rail adapters
- Canonical owned-site directory and Sites behavior
- Adjacent 104px Sites and 44px Settings controls on desktop, with compact and extreme-compact transformations
- Icon-only Settings appearance selector for System, Light, and Dark
- Unified expanding Sites and Settings disclosure shells with centered content and downward reveal
- Complete-header pinning while a disclosure is open, stable header footprint, and reduced-motion-aware dismissal behavior
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

## Header and appearance acceptance record

The v1.9.0 header and appearance work established the following shared production behavior:

- Sites contains only the three owned destinations; appearance preferences are owned by the adjacent Settings disclosure.
- Sites and Settings are mutually exclusive and use the same expanding-shell interaction model.
- Disclosure content grows downward from the trigger and is clipped during reveal so the trigger does not flash between rounded and squared states.
- Site labels are centered in the compact disclosure width.
- The selected System, Light, or Dark icon is indicated by the shared terracotta selection rail.
- Opening either disclosure keeps the complete header together while scrolling rather than pinning only the controls.
- The normal page footprint remains reserved while the header is fixed: 83px on desktop and 69px in the compact header state, including the divider.
- Closing a scrolled disclosure uses the complete-header exit animation; reduced-motion users receive no nonessential animation.
- All three consumers currently pin the same reviewed v1.9.0 shared-asset source.
- Network Diagnostics and RolePacket use the default shared header rail; Portfolio uses the documented 1024px-and-up product adapter with 40px left identity inset, 20px right controls inset, and optically centered navigation.

## Manual acceptance record

The repository owner completed and accepted the original remaining manual checks on 2026-07-29:

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

Meaningful navigation, layout, or interaction changes after those acceptance runs still require the applicable manual checks to be re-run rather than inheriting approval automatically. The Portfolio desktop header rail changed on 2026-08-09 and passed the repository automated visual, theme, conformance, quality, security, CodeQL, and performance checks; its 2026-07-29 actual-zoom and assistive-technology review remains historical until that manual review is refreshed.

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
- Keep canonical documentation synchronized with the shipped header and appearance contract whenever shared behavior changes.
- Keep approved product rail adapters documented and bounded so they cannot silently fork shared controls or interaction behavior.
- Documentation-only governance changes do not require consumer repins when packaged shared assets remain byte-identical.
- Register every future exception explicitly instead of allowing undocumented drift.

`RolePacket-Autopilot` remains outside this migration and must not be modified as part of Web Design System maintenance.
