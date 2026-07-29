# Migration and conformance status

This document records the rollout of shared foundations, structural shells, interaction contracts, conformance tooling, and consumer update automation across the owned sites. Repository-specific product logic remains in its own repository.

## Approved direction

The current production UI and UX of the three sites is the approved baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The migration goal is to remove foundational, behavioral, accessibility, provenance, and maintenance drift without redesigning the products or forcing identical layouts.

## Current rollout matrix

| Repository | Current default-branch package | Current state |
| --- | --- | --- |
| Website | v1.8.1 | Lock, package dependency, generated assets, source metadata, workflows, integration validation, conformance, visual audit, lint, security scan, and CodeQL are aligned and passing. |
| Network Diagnostics | v1.8.1 | Lock, generated assets, helper copies, workflows, integration validation, conformance, unit tests, build, visual audit, UI regression, security scan, and CodeQL are aligned and passing. |
| RolePacket | v1.7.0 until its independent adoption pull request merges | The v1.8.1 adoption branch contains the conformance pipeline, 320px audit, corrected narrow-desktop expectations, lock-derived validation, and shared provenance files. It remains pending until its complete authenticated test matrix passes. |
| Web Design System | v1.8.1 on the default branch; v1.8.2 under review | The v1.8.2 candidate adds strict manifest validation, provenance-bearing reports, update-safe consumer validators, and a cross-consumer candidate gate. |

No consumer rollout is considered complete merely because generated CSS appears correct. Lock metadata, package or helper provenance, synchronized assets, workflow pins, integration validation, conformance reports, and product tests must describe the same reviewed release.

## Shared package capabilities

Completed through v1.5.0:

- Atomic tokens and generated CSS are versioned.
- The exact dot canvas, accessibility foundations, global header, identity lockup, and Sites control are packaged.
- The owned-site directory is centralized.
- Sites-menu click, outside-click, Escape, ArrowUp, ArrowDown, Home, End, focus-entry, and focus-restoration behavior is shared.
- The compact header-menu trigger and popover shell are shared.
- JavaScript and TypeScript package exports are validated.
- Reusable page-content and content-guard utilities remain available for selective adoption.

Completed in v1.6.0 and v1.6.1:

- Added standalone, variable-backed actions, buttons, callouts, empty states, and table-region shells.
- Made the standalone primitive export independent of the larger content layer.
- Added shared responsive and forced-colors behavior for the primitive layer.
- Added deployed-site smoke checks.
- Adopted selected primitives without redesigning product layouts.
- Removed trial fallbacks only after product-level visual and behavior checks demonstrated equivalence.

Completed in v1.7.0:

- Added a variable-backed native-dialog shell.
- Added a constrained consumer-release resolver that cannot write outside the current repository or execute arbitrary commands.
- Added a reusable consumer synchronization workflow.
- Moved update-branch publication and draft pull-request handling into the shared workflow.
- Kept consumer schedules, Node versions, installation commands, validation commands, and tracked paths product-owned.
- Removed tested structural fallbacks from Network Diagnostics and RolePacket.

Completed in v1.8.0 and v1.8.1:

- Added a machine-readable conformance contract with stable rule identifiers.
- Added a repository-confined evidence runner and reusable conformance workflow.
- Added explicit manual states for actual browser zoom, assistive-technology review, and performance approval.
- Added 320px minimum-width product audits.
- Added the extreme-compact shared-header transformation required by the longest product identity.
- Corrected automated terminology so a 720px viewport is `narrow-desktop`, not actual browser zoom.

Under review in v1.8.2:

- Add a strict consumer-manifest schema.
- Reject unknown declaration and evidence properties before rule evaluation.
- Verify that the consumer lock version matches the conformance contract.
- Add immutable design-system source and consumer commit provenance to reports.
- Derive consumer integration expectations from `design-system.lock.json` so scheduled updates can validate new candidates.
- Run Website, Network Diagnostics, and RolePacket against every design-system candidate before merge.

## Portfolio status

Approved state:

- The homepage retains its editorial composition, spacing, terracotta treatment, and responsive behavior.
- Homepage and case studies render the shared header and Sites control.
- Case studies retain consistent narrative structure, project facts, numbered sections, evidence, limitations, and next-project navigation.
- Case-study headers exist in source-level markup rather than runtime construction.
- The Sites menu uses the shared controller and canonical site directory.
- Compact product navigation uses the shared menu shell and controller.
- Contact destinations remain available at compact widths.
- Case-study actions use the shared action and button shells.
- Scheduled design-system updates use the shared release resolver and reusable workflow.
- Integration validation derives package provenance from the lock.

The portfolio does not adopt the shared dialog shell because it currently has no matching native confirmation dialog.

Completed automated validation for v1.8.1:

- Design-system integration and conformance
- HTML and CSS linting
- Visual audit, including 320px containment
- Web quality
- Secret scan
- CodeQL

Manual confirmation still required:

- Actual 200 percent zoom review across the homepage and each case study
- Final reduced-motion and forced-colors visual review in supported browsers
- Reviewed bundle and user-experience performance baseline

## Network Diagnostics status

Approved state:

- Shared tokens, exact dot canvas, global header, product navigation, and Sites control are integrated.
- The current hero, sticky test controls, profile selector, measurement preview, result states, charts, history, methodology, privacy, and native-probe import layout remain the approved baseline.
- The Sites menu uses the shared controller and canonical site directory.
- Compact product navigation uses the shared controller and menu shell.
- Compact DOM and focus order is Menu, then Sites.
- The obsolete clipped mobile-navigation shell is removed.
- Idle, running, error, completed-report, saved-history, methodology, privacy, local-probe import, and imported-report states retain consistent semantic roles.
- The legacy visible grid remains disabled.
- Product charts, measurements, semantic data colors, Worker behavior, and native probe remain product-owned.
- Error recovery and latency-table containment use shared primitives without duplicate structural fallbacks.
- The data-use confirmation dialog uses the shared dialog shell.
- Dialog dimensions, mobile bottom-sheet behavior, checkbox content, transfer-cap logic, remembered consent, wording, and test behavior remain product-owned.
- Scheduled design-system updates use the shared resolver and reusable workflow.
- Integration validation derives package provenance from the lock.

Completed automated validation for v1.8.1:

- Design-system integration and conformance
- CI and unit tests
- Application build
- Visual audit, including 320px containment
- UI regression
- Secret scan
- CodeQL

Manual confirmation still required:

- Grayscale chart review for every result state
- Actual 200 percent zoom review of selectors, tables, charts, and imported probe reports
- Final forced-colors and assistive-technology review
- Reviewed bundle and user-experience performance baseline

## RolePacket status

Approved product boundary:

- Shared palette, typography roles, focus, canvas, global header, Sites control, semantic tokens, content primitives, and confirmation-dialog shell are integrated.
- Login, loading, dashboard, intake, tracker, profile, memory, application detail, fit analysis, resume review, notes, versions, empty, warning, and confirmation states retain the dense workflow UI.
- The wide sidebar remains at desktop widths.
- The compact layout retains its keyboard-operable workspace drawer with focus containment, Escape close, focus restoration, inert navigation, and reduced-motion support.
- Product-specific forms, review panels, comparisons, application rows, and workflow density remain local.
- Queueing, extension events, destructive/default tone selection, copy, animation, cancellation, and focus behavior remain product-owned.
- The fit-analysis blocker uses the shared callout structure without inheriting the separate resume-audit warning selector.
- The workspace drawer remains product-owned and is not moved into the design system.

The v1.8.1 adoption pull request adds:

- Exact v1.8.1 lock and generated provenance
- Conformance contract, manifest, runner, and workflow
- 320px minimum-width coverage
- Correct 720px narrow-desktop header expectations
- State-without-color evidence based on actual labels, alignment text, and condition marks
- Lock-derived integration validation
- Immutable reusable-workflow validation

The adoption remains pending until the following branch checks complete successfully:

- Design-system drift, integration, and conformance
- Typechecks and application build
- Cloudflare dry deployment
- Unit, server, and browser tests
- Dependency audit and static analysis
- Authenticated visual audit
- Secret scan

`RolePacket-Autopilot` is outside this migration and is not modified.

Manual confirmation after merge still requires:

- Authenticated actual 200 percent zoom review across core workflows
- Forced-colors and assistive-technology review
- Reviewed bundle and user-experience performance baseline

## Consumer update tooling

Approved behavior:

- Every consumer pins an immutable source commit.
- Release resolution uses the shared constrained helper.
- Consumer update workflows call reusable workflows by immutable commit.
- Update publication logic is not duplicated across repositories.
- Consumer validation commands and schedules remain local.
- Generated helpers and contract files are included in drift validation where committed locally.
- Each consumer retains an independent pull request and rollback boundary.
- Consumer integration validators derive expected version and source commit from the lock.

Required behavior:

- The resolver may update only repository-local design-system metadata and an explicitly supplied package manifest.
- The resolver rejects path traversal and invalid commit or version formats.
- The shared workflow validates before creating or refreshing an update pull request.
- A consumer workflow does not pin a reusable workflow to a floating branch.
- Validation does not compare a synchronized candidate against hard-coded metadata from the previous release.

## Cross-consumer release gate

The v1.8.2 candidate gate validates the shared candidate against the current default branch of all three consumers.

The gate must prove that each candidate can:

- Synchronize the consumer-owned asset set
- Pass lock and generated-asset provenance checks
- Pass the product conformance manifest
- Preserve shared header, Sites-control, primitive, dialog, and ownership boundaries
- Pass relevant product lint, tests, builds, and deployment dry runs

The gate does not publish consumer changes. Consumer adoption still occurs in independent pull requests after the shared release merges.

## Repository governance

The intended required checks are:

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

Repository rulesets must enforce these checks before merging. The repository API available to the implementation workflow does not expose ruleset mutation, so enforcement must be confirmed in GitHub settings rather than inferred from passing runs.

## Manual release checklist

- Compare all three production headers at desktop and compact widths.
- Confirm product-specific layouts remain visually unchanged after synchronization.
- Test keyboard traversal, menu focus, drawers, forms, tables, and dialogs.
- Test 320px width and actual 200 percent zoom without document-level overflow.
- Review reduced motion, forced colors, contrast, and grayscale meaning.
- Review all portfolio case studies for media framing, prose rhythm, actions, and next-project navigation.
- Record current bundle and user-experience performance baselines.
- Register or remove every remaining exception.

The design system remains an **implementation candidate** until the manual release checklist and performance baselines are recorded. The production UI itself remains the approved visual baseline.
