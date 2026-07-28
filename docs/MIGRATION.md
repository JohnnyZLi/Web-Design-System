# Migration and conformance status

This document records the rollout of shared foundations and interaction contracts across the owned sites. Repository-specific implementation details and private product logic remain in their own repositories.

## Approved direction

The current production UI and UX of the three sites is the approved baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The migration goal is to remove foundational and behavioral drift without redesigning the products or forcing identical markup.

## Shared-asset baseline

Current package rollout:

- Package: `@johnnyzli/web-design-system`
- Version: `1.5.0`
- Immutable source: recorded in each consumer repository's generated source metadata

Each consumer synchronizes:

- Generated tokens
- Accessibility and canvas foundations
- Global-header and Sites-control styling
- Canonical owned-site registry
- Framework-neutral Sites-menu behavior
- Compact header-menu shell where applicable
- Version and source metadata

The optional page-content package remains available for new components and deliberate consolidation. Stable product markup remains conforming when it uses the same tokens, accessibility behavior, semantic roles, and responsive outcomes.

## Phase 0 — Shared foundation

Completed in v1.5.0:

- Atomic tokens and generated CSS are versioned.
- The exact dot canvas, accessibility foundations, global header, identity lockup, and Sites control are packaged.
- The owned-site directory is centralized.
- Sites-menu click, outside-click, Escape, ArrowUp, ArrowDown, Home, End, focus-entry, and focus-restoration behavior is shared.
- The compact header-menu trigger and popover shell are shared.
- JavaScript and TypeScript package exports are validated.
- Reusable page-content and content-guard utilities remain available for selective adoption.

Still required before promoting the package from implementation candidate:

- Record current bundle and performance baselines.
- Complete the manual specimen approval record.
- Complete the cross-site manual accessibility checks listed below.

## Phase 1 — Portfolio

Approved state:

- The homepage retains its editorial composition, spacing, terracotta treatment, and responsive behavior.
- Homepage and case studies render the shared header and Sites control.
- Five case studies retain consistent narrative structure, project facts, numbered sections, evidence, limitations, and next-project navigation.
- Case-study headers are migrated from runtime construction to source-level shared markup.
- The Sites menu uses the shared controller and canonical site directory.
- Compact product navigation uses the shared menu shell and controller.
- Contact destinations remain available at compact widths.

No visual redesign is required for conformance.

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

RolePacket feature work may continue without requiring a cross-site redesign.

Still required:

- Continue component-by-component consolidation of resilience and hotfix stylesheets when it can be done without behavior changes.
- Perform authenticated 200% zoom and forced-colors review across each core workflow.

## Phase 4 — Cross-site validation

Automated requirements:

- Every owned site reaches the other two within two interactions.
- Owned-site links stay in the same tab.
- Every route or application state renders the shared header contract.
- Consumers use the canonical site registry and shared Sites-menu behavior.
- Portfolio and Network compact navigation use the shared header-menu shell.
- Consumer assets match the pinned v1.5.0 source.
- Product CI covers relevant typechecking, builds, application tests, accessibility checks, security scanning, and packaging.

Manual release checklist:

- Compare all three production headers at desktop and compact widths.
- Confirm product-specific layouts remain visually unchanged after synchronization.
- Test keyboard traversal, menu focus, drawers, forms, tables, and dialogs.
- Test 320px width and 200% zoom without document-level overflow.
- Review reduced motion, forced colors, contrast, and grayscale meaning.
- Review all project case studies for media framing, prose rhythm, actions, and next-project navigation.
- Register or remove every remaining exception.

The design system remains an **implementation candidate** until the manual release checklist and performance baselines are recorded. The production UI itself remains the approved visual baseline.
