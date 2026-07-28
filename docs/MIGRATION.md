# Migration and conformance status

This document records the rollout of shared foundations, structural shells, interaction contracts, and consumer tooling across the owned sites. Repository-specific product logic remains in its own repository.

## Approved direction

The current production UI and UX of the three sites is the approved baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The migration goal is to remove foundational, behavioral, and maintenance drift without redesigning the products or forcing identical layouts.

## Shared-asset baseline

Current package rollout:

- Package: `@johnnyzli/web-design-system`
- Version: `1.7.0`
- Immutable source: recorded in each consumer lock and generated source metadata

Each consumer synchronizes the assets it uses from the reviewed source commit:

- Generated tokens
- Accessibility and canvas foundations
- Global-header and Sites-control styling
- Canonical owned-site registry
- Framework-neutral Sites-menu behavior
- Compact header-menu shell where applicable
- Standalone content primitives
- Shared consumer-release helper where applicable
- Version and source metadata

The reference page-content package remains available for new work and deliberate consolidation. Stable product markup remains conforming when it uses the same tokens, accessibility behavior, semantic roles, and responsive outcomes.

## Phase 0 — Shared foundation

Completed in v1.5.0:

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
- Adopted selected primitives in all three consumers without redesigning their layouts.
- Kept trial fallbacks until product-level visual and behavior checks demonstrated equivalence.

Completed in v1.7.0:

- Added a variable-backed native-dialog shell.
- Added a constrained consumer-release resolver that cannot write outside the current repository or execute arbitrary commands.
- Added a reusable consumer synchronization workflow.
- Moved update-branch publication and draft pull-request handling into the shared workflow.
- Kept consumer schedules, Node versions, installation commands, validation commands, and tracked paths product-owned.
- Removed tested structural fallbacks from Network Diagnostics and RolePacket.

Still required before promoting the package from implementation candidate:

- Record current bundle and performance baselines.
- Complete the manual specimen approval record.
- Complete the remaining cross-site manual accessibility checks listed below.

## Phase 1 — Portfolio

Approved state:

- The homepage retains its editorial composition, spacing, terracotta treatment, and responsive behavior.
- Homepage and case studies render the shared header and Sites control.
- Five case studies retain consistent narrative structure, project facts, numbered sections, evidence, limitations, and next-project navigation.
- Case-study headers exist in source-level shared markup rather than runtime construction.
- The Sites menu uses the shared controller and canonical site directory.
- Compact product navigation uses the shared menu shell and controller.
- Contact destinations remain available at compact widths.
- Case-study actions use the shared action and button shells.
- Scheduled design-system updates use the shared release resolver and reusable workflow.

The portfolio does not adopt the shared dialog shell because it currently has no matching native confirmation dialog.

Manual confirmation still required:

- 200% zoom review across the homepage and each case study.
- Final reduced-motion and forced-colors visual review in supported browsers.

## Phase 2 — Network Diagnostics

Approved state:

- Shared tokens, exact dot canvas, global header, site navigation, and Sites control are integrated.
- The current hero, sticky test controls, profile selector, measurement preview, result states, charts, history, methodology, privacy, and native-probe import layout remain the approved baseline.
- The Sites menu uses the shared controller and canonical site directory.
- Compact product navigation uses the shared controller and menu shell.
- Idle, running, error, completed-report, saved-history, methodology, privacy, local-probe import, and imported-report states retain consistent semantic roles.
- The legacy visible grid remains disabled.
- Product charts, measurements, semantic data colors, Worker behavior, and native probe remain product-owned.
- Error recovery and latency-table containment use shared primitives without duplicate structural fallbacks.
- The data-use confirmation dialog uses the shared dialog shell.
- Dialog dimensions, mobile bottom-sheet behavior, checkbox content, transfer-cap logic, remembered consent, wording, and test behavior remain product-owned.
- Scheduled design-system updates use the shared resolver and reusable workflow.

Completed validation:

- CI, CodeQL, secret scan, visual audit, and UI regression passed for the v1.7.0 adoption.

Manual confirmation still required:

- Grayscale chart review for every result state.
- 200% zoom review of selectors, tables, charts, and imported probe reports.

## Phase 3 — RolePacket

Approved state:

- Shared palette, typography roles, focus, canvas, global header, Sites control, and semantic tokens are integrated.
- The Sites menu uses the shared controller and canonical site directory.
- Login, loading, dashboard, intake, tracker, profile, memory, application detail, fit analysis, resume review, notes, versions, empty, warning, and confirmation states retain the dense workflow UI.
- The wide sidebar remains at desktop widths.
- The compact layout retains its keyboard-operable workspace drawer with focus containment, Escape close, focus restoration, inert navigation, and reduced-motion support.
- Product-specific forms, review panels, comparisons, application rows, and workflow density remain local.
- The reusable confirmation service uses the shared dialog shell.
- Queueing, extension events, destructive/default tone selection, copy, animation, cancellation, and focus behavior remain product-owned.
- The fit-analysis blocker uses the shared callout structure without inheriting the separate resume-audit warning selector.
- Scheduled design-system updates use the shared resolver and reusable workflow.

The workspace drawer remains product-owned and was not moved into the design system.

Completed validation:

- Design-system drift and integration checks passed.
- Typechecks, application build, Cloudflare dry deployment, unit tests, server tests, browser tests, dependency audit, static analysis, authenticated visual audit, and secret scan passed for the v1.7.0 adoption.

Still required:

- Continue component-by-component cleanup only when it removes demonstrated duplication without behavior changes.
- Perform authenticated 200% zoom and forced-colors review across each core workflow.

## Phase 4 — Consumer update tooling

Approved state:

- All three consumers pin the design system to an immutable source commit.
- Release resolution uses the shared constrained helper.
- Consumer update workflows call the reusable workflow by immutable commit.
- Update publication logic is no longer duplicated across the three repositories.
- Consumer validation commands and schedules remain local.
- Generated helpers are included in drift validation where they are committed locally.
- Each consumer retains an independent pull request and rollback boundary.

Required behavior:

- The resolver may update only repository-local design-system metadata and an explicitly supplied package manifest.
- The resolver must reject path traversal and invalid commit or version formats.
- The shared workflow must validate before creating or refreshing an update pull request.
- A consumer workflow must not pin the reusable workflow to a floating branch.

## Phase 5 — Cross-site validation

Automated requirements:

- Every owned site reaches the other two within two interactions.
- Owned-site links stay in the same tab.
- Every route or application state renders the shared header contract.
- Consumers use the canonical site registry and shared Sites-menu behavior.
- Portfolio and Network compact navigation use the shared header-menu shell.
- Consumer assets match the pinned v1.7.0 source.
- Matching native confirmation dialogs use the shared dialog structure.
- Adopted primitives do not retain equivalent structural fallbacks.
- Consumer workflows use the immutable shared synchronization workflow.
- Product CI covers relevant typechecking, builds, application tests, accessibility checks, security scanning, packaging, and deployment validation.

Manual release checklist:

- Compare all three production headers at desktop and compact widths.
- Confirm product-specific layouts remain visually unchanged after synchronization.
- Test keyboard traversal, menu focus, drawers, forms, tables, and dialogs.
- Test 320px width and 200% zoom without document-level overflow.
- Review reduced motion, forced colors, contrast, and grayscale meaning.
- Review all project case studies for media framing, prose rhythm, actions, and next-project navigation.
- Register or remove every remaining exception.

The design system remains an **implementation candidate** until the manual release checklist and performance baselines are recorded. The production UI itself remains the approved visual baseline.
