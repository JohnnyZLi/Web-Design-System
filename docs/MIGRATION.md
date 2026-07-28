# Migration and conformance status

This document records the rollout of shared foundations across the owned sites. Repository-specific implementation details and private product logic remain in their own repositories.

## Approved direction

The current production UI and UX of the three sites is the approved baseline:

- `johnnyli.dev` remains editorial and spacious.
- `network.johnnyli.dev` remains analytical and measurement-oriented.
- `rolepacket.johnnyli.dev` remains dense and workflow-oriented.

The migration goal is to remove foundational drift without redesigning the products or forcing identical markup. The shared specimen is a component reference, not a target application skin.

## Shared-asset baseline

Current reviewed package baseline:

- Package: `@johnnyzli/web-design-system`
- Version: `1.4.0`
- Immutable source: recorded in each consumer repository's generated source metadata

Each consumer synchronizes the production foundations it currently uses:

- Generated tokens
- Accessibility and canvas foundations
- Shared global header and Sites control
- Version and source metadata

The optional page-content package remains available for new components and deliberate consolidation. Existing stable product markup is conforming when it uses the same tokens, accessibility behavior, semantic roles, and responsive outcomes.

Documentation-only changes may advance independently of the pinned shared-asset commit when distributable CSS and token files are unchanged.

## Phase 0 — Foundation

Completed:

- Atomic tokens and generated CSS are versioned.
- The exact dot canvas, accessibility foundations, global header, site identity, and Sites control are packaged.
- Reusable page-content and content-guard utilities are packaged for selective adoption.
- Package, release, public-safety, raw-color, import, undefined-token, responsive-content, and version-drift validation are active.
- The three consumer repositories are being aligned to the same immutable v1.4.0 shared-asset source.

Still required before promoting the package from implementation candidate:

- Record current bundle and performance baselines.
- Complete the manual specimen approval record.
- Complete the cross-site manual accessibility checks listed below.

## Phase 1 — Portfolio

Approved current state:

- The homepage retains its editorial composition, open spacing, terracotta treatment, and current responsive behavior.
- The homepage renders the shared global header and Sites control.
- Five project case studies retain a consistent narrative structure, project facts, numbered sections, evidence, limitations, and next-project navigation.
- Case studies currently enhance legacy source header markup into the rendered shared header at runtime.
- Contact destinations remain available at compact widths.
- Automated HTML, CSS, design-system, and Web Content Accessibility Guidelines checks cover every HTML page.

No visual redesign is required for conformance.

Optional technical cleanup:

- Replace the runtime case-study header enhancement with source-level shared markup when convenient, without changing the rendered UI.

Manual confirmation still required:

- 200% zoom review across the homepage and each case-study page.
- Final reduced-motion and forced-colors visual review in supported browsers.

## Phase 2 — Network Diagnostics

Approved current state:

- Shared tokens, exact dot canvas, global header, site navigation, and Sites control are integrated.
- The current hero, sticky test controls, profile selector, measurement preview, result states, charts, history, methodology, privacy, and native-probe import layout are the approved UI baseline.
- Idle, running, error, completed-report, saved-history, methodology, privacy, local-probe import, and imported-report states use consistent token and semantic roles.
- The legacy visible grid is disabled rather than layered over the dots.
- Test profiles expose name, duration, and maximum transfer cap without label collisions.
- Methodology, Privacy, and Source remain reachable in the compact header transformation.
- Product charts, measurements, semantic data colors, Worker behavior, and native probe remain product-owned.

No visual redesign is required for conformance.

Manual confirmation still required:

- Grayscale chart review for every result state.
- 200% zoom review of selectors, result tables, charts, and imported probe reports.

## Phase 3 — RolePacket

Approved current state:

- Shared palette, typography roles, focus, canvas, global header, Sites control, and semantic state tokens are integrated.
- Login, loading, dashboard, new-application intake, tracker, profile, memory, application-detail, fit-analysis, resume-review, notes, versions, empty, warning, and confirmation states retain the current dense workflow UI.
- The wide sidebar remains at desktop widths.
- The compact layout uses a keyboard-operable off-canvas workspace drawer with focus containment, Escape close, focus restoration, inert background navigation, and reduced-motion support.
- Major workflow states use complete semantic text, surface, and border token triplets.
- Product-specific forms, review panels, comparisons, application rows, and workflow density remain local.

RolePacket feature work may continue without requiring a cross-site visual redesign.

Still required:

- Continue component-by-component consolidation of resilience and hotfix stylesheets when it can be done without behavior changes.
- Perform authenticated 200% zoom and forced-colors review across each core workflow.

## Phase 4 — Cross-site validation

Automated requirements:

- Every owned site reaches the other two within two interactions.
- Owned-site links stay in the same tab.
- Every route or application state renders the shared header contract.
- Consumer assets match the pinned v1.4.0 source.
- Product CI covers relevant typechecking, builds, application tests, accessibility checks, security scanning, and packaging.

Manual release checklist:

- Compare the three production headers at desktop and compact widths.
- Confirm the current product-specific layouts remain unchanged after shared-asset synchronization.
- Test keyboard traversal, menu focus, drawers, forms, tables, and dialogs on all three sites.
- Test 320px width and 200% zoom without document-level overflow.
- Review reduced motion, forced colors, contrast, and grayscale meaning.
- Review all project case studies for media framing, prose rhythm, actions, and next-project navigation.
- Register or remove every remaining exception.

The design system remains an **implementation candidate** until the manual release checklist and performance baselines are recorded. The production UI itself is the approved visual baseline.
