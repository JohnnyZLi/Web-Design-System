# Migration and conformance status

This document records the current shared-design-system rollout across the owned sites. Historical release details remain in [`CHANGELOG.md`](../CHANGELOG.md); this file describes the current default-branch state and the work that is still intentionally manual.

## Approved direction

The production interfaces remain the approved visual baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The design system removes foundational, behavioral, accessibility, provenance, and maintenance drift without forcing the products into one layout.

## Current rollout matrix

| Repository | Default-branch design system | Current state |
| --- | --- | --- |
| Website | v1.8.2 at `abb6c44f588afe09e8f593a8c467b564ac9fef86` | Lock, package dependency, generated assets, source metadata, reusable workflows, integration validation, conformance, visual audit, lint, security scan, and CodeQL are aligned. |
| Network Diagnostics | v1.8.2 at `abb6c44f588afe09e8f593a8c467b564ac9fef86` | Lock, generated assets, helper copies, workflows, integration validation, conformance, tests, build, visual audit, UI regression, security scan, and CodeQL are aligned. |
| RolePacket | v1.8.2 at `abb6c44f588afe09e8f593a8c467b564ac9fef86` | Lock, generated assets, helper copies, workflows, integration validation, conformance, typechecks, builds, Cloudflare dry runs, 109 automated tests, visual audit, and production dependency audit were validated before adoption. |
| Web Design System | v1.8.2 | Strict manifest validation, provenance-bearing reports, lock-derived consumer validation, and the cross-consumer candidate gate are merged on `main`. |

A rollout is complete only when lock metadata, package or helper provenance, generated assets, reusable workflow pins, integration validation, conformance evidence, and product checks describe the same reviewed release.

## Shared package capabilities

The current package provides:

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

## Portfolio status

The approved portfolio state retains:

- Editorial homepage and case-study composition
- Shared header and Sites control on every page
- Source-level case-study headers
- Shared compact navigation controller
- Shared action and button shells for case-study actions
- Lock-derived provenance and weekly design-system update automation
- Automated HTML, CSS, accessibility, visual, security, and CodeQL checks

Manual confirmation still required:

- Actual 200 percent browser zoom across the homepage and every case study
- Final reduced-motion and forced-colors review in supported browsers
- Assistive-technology review
- Recorded bundle and user-experience performance baseline

## Network Diagnostics status

The approved Network Diagnostics state retains:

- Shared tokens, dot canvas, header, product navigation, and Sites control
- Existing hero, sticky controls, profile selector, measurement preview, result states, charts, history, methodology, privacy, and native-probe import layout
- Menu-then-Sites compact order and keyboard behavior
- Shared error, action, table, and dialog primitives where adopted
- Product-owned charts, measurements, semantic data colors, Worker behavior, and native probe
- Automated integration, conformance, unit, build, visual, UI-regression, security, and CodeQL checks

Manual confirmation still required:

- Grayscale chart review for every result state
- Actual 200 percent browser zoom of selectors, tables, charts, and imported reports
- Final forced-colors and assistive-technology review
- Recorded bundle and user-experience performance baseline

## RolePacket status

The approved RolePacket state retains:

- Shared palette, typography roles, focus, canvas, header, Sites control, semantic tokens, content primitives, and confirmation-dialog shell
- Dense review-first workflow and wide desktop sidebar
- Keyboard-operable compact workspace drawer with focus containment, Escape close, focus restoration, inert navigation, and reduced-motion support
- Product-owned forms, review panels, comparisons, application rows, state transitions, extension events, and workflow density
- Shared fit-analysis blocker and confirmation-dialog structures without moving the workspace drawer into the design system

The v1.8.2 adoption was validated with design-system drift, integration and conformance checks; local and cloud TypeScript checks; client and server builds; both Cloudflare Worker dry runs; 109 automated tests; visual audit; and a production dependency audit.

`RolePacket-Autopilot` is outside this migration and must not be modified.

Manual confirmation still required:

- Authenticated actual 200 percent browser zoom across core workflows
- Forced-colors and assistive-technology review
- Recorded bundle and user-experience performance baseline

## Consumer update tooling

Every consumer:

- Pins an immutable WDS source commit
- Resolves updates through the constrained shared helper
- Calls reusable workflows by immutable commit
- Keeps product-specific schedules and validation commands locally
- Includes generated helpers and contracts in drift validation when they are committed locally
- Retains an independent pull request and rollback boundary

The shared synchronization workflow stages the configured generated paths before checking for changes. This ensures newly created, previously untracked assets are included rather than incorrectly reporting that a consumer is current.

## Cross-consumer release gate

Every WDS candidate must validate against the current default branch of all three consumers before merge. The gate:

- Checks out the exact candidate SHA that is written into consumer lock metadata
- Synchronizes each consumer-owned asset set
- Validates lock and generated-asset provenance
- Evaluates the product conformance manifest
- Runs relevant product lint, tests, builds, and deployment dry runs
- Requires private RolePacket repository access instead of silently skipping that consumer

The WDS repository therefore requires a `ROLEPACKET_REPOSITORY_TOKEN` secret with read access to `JohnnyZLi/RolePacket`. Absence of that secret is a blocking release-gate failure. The public WDS workflow remains the runner owner, so this check does not require a private-repository hosted runner.

## Repository governance

Intended required checks:

### Website

- Design-system conformance
- Web quality
- Visual audit
- Secret scan
- CodeQL

### Network Diagnostics

- Design-system conformance
- CI
- Visual audit
- UI regression
- Secret scan
- CodeQL

### RolePacket

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

Repository rulesets must enforce these checks before merging. Enforcement must be confirmed in GitHub settings rather than inferred from passing runs.

## Manual release checklist

- Compare all three production headers at desktop and compact widths.
- Confirm product-specific layouts remain visually unchanged after synchronization.
- Test keyboard traversal, menu focus, drawers, forms, tables, and dialogs.
- Test 320px width and actual 200 percent zoom without document-level overflow.
- Review reduced motion, forced colors, contrast, grayscale meaning, and assistive-technology output.
- Review every portfolio case study for media framing, prose rhythm, actions, and next-project navigation.
- Record bundle and user-experience performance baselines.
- Register or remove every remaining exception.

The package remains an **implementation candidate** until the manual checklist and performance baselines are recorded. The production UI itself remains the approved visual baseline.
