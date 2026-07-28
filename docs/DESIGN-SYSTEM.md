# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.8.0  
**Package status:** Implementation candidate  
**Production visual baseline:** Approved  
**Owner:** Johnny Li

- **MUST** means required for conformance.
- **SHOULD** means expected unless a documented exception exists.
- **MAY** means optional.
- **CURRENT** describes approved production behavior.
- **REFERENCE** describes a reusable pattern that does not require replacing stable UI.

The production interfaces at `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev` are the visual baseline. Shared work reduces drift without making the products identical.

## 2. Design intent

> **Editorial warmth, systems precision.**

The products feel related while serving different purposes:

- **Portfolio:** editorial, open, spacious, and narrative.
- **Network Diagnostics:** analytical, measurement-oriented, and data-dense where useful.
- **RolePacket:** compact, workflow-oriented, and optimized for review and state management.

The specimen demonstrates shared language. It is not a replacement application theme.

## 3. Ownership boundary

### Shared and required

The design system owns:

- Atomic color, typography, spacing, radius, control, motion, elevation, icon, z-index, and layout tokens
- Warm off-white canvas and exact faint dot texture
- Global focus, selection, reduced-motion, and forced-colors behavior
- Global-header geometry and owner/product identity lockup
- Canonical owned-site registry
- Sites-control styling and framework-neutral interaction behavior
- Compact header-menu toggle, popover shell, and interaction controller
- Semantic success, warning, danger, information, and violet token triplets
- Standalone adaptable shells for actions, buttons, callouts, empty states, table regions, and native dialogs
- Shared dialog structure for backdrop, placement, surface, title, message, actions, compact transformation, and forced-colors behavior
- Constrained consumer-release resolution for immutable source and version metadata
- Reusable GitHub Actions workflows for consumer synchronization and conformance reporting
- Stable machine-readable conformance rule IDs, applicability, severity, and canonical source links
- Cross-site navigation, accessibility, distribution, and responsive contracts

### Product-owned

Each product owns:

- Information architecture and page composition
- Product navigation labels, destinations, and active-state logic
- Portfolio editorial rhythm and case-study composition
- Network test controls, measurement logic, charts, reports, profiles, Worker behavior, and native probe behavior
- RolePacket sidebar, forms, workflow density, authentication, review logic, application state, APIs, storage, and extension behavior
- Dialog copy, application state, confirmation logic, focus timing, dimensions, density, color expression, and animation configured through shared hooks
- Consumer schedules, Node versions, installation commands, validation commands, and tracked generated paths
- Product state fixtures, visual-audit adapters, browser tests, builds, deployment checks, and conformance evidence manifests
- Product-specific component names and implementation structure

Products MAY use shared content classes from `styles/content.css` and `styles/content-guard.css`. Products SHOULD use `styles/content-primitives.css` when an approved local component matches one of its structural shells.

A migration MUST NOT be justified solely by replacing a product class with a `jl-*` class when the rendered result and behavior are already correct.

After a shared primitive has passed product-level visual and behavioral validation, the product MUST remove equivalent structural fallback declarations rather than retain a second implementation indefinitely.

## 4. Principles

1. Preserve the approved production UI before pursuing code-level consolidation.
2. Share foundations, structural shells, interaction contracts, and test contracts—not product identity.
3. Use one accessible terracotta accent; reserve other hues for semantic or analytical meaning.
4. Make state, evidence, scope, ownership, and recovery explicit.
5. Prefer responsive reflow over clipping, shrinking, or hiding essential navigation.
6. Keep runtime dependencies and third-party data sharing minimal.
7. Product adapters MUST NOT redefine shared header, Sites-control, compact-menu, or adopted primitive structure.
8. Content remains understandable without color, animation, hover, or a wide viewport.
9. Shared appearance changes require comparison across all three products.
10. Shared distribution changes require immutable source pins and consumer validation before merge.
11. Product-local logic MUST remain local even when its visible shell becomes shared.
12. Automated conformance MUST use stable rule IDs and explicit evidence; CI MUST NOT derive tests by parsing prose from this document.
13. Automation MUST NOT claim coverage for checks that still require manual review.

## 5. Atomic tokens

The editable source is `tokens/tokens.tokens.json`. Generated CSS is not edited manually.

### Color roles

- `canvas` and `canvasDot`: page background and exact dot texture
- `surface`, `surfaceMuted`, `surfaceStrong`, `surfaceInverse`: grouped content surfaces
- `ink`, `text`, `muted`: primary, body, and secondary text
- `accent`, `accentHover`, `accentActive`, `accentDecorative`, `accentSoft`, `onAccent`: terracotta emphasis and interaction roles
- Success, warning, danger, information, and violet: complete text, surface, and border triplets
- Overlay, focus-gap, placeholder, skeleton, and selection roles

Raw shared colors MUST NOT appear in shared CSS. Product chart colors MAY remain local when labels and grayscale distinction preserve meaning.

### Typography roles

- UI: system sans-serif
- Editorial: Iowan/Palatino/Georgia-style serif
- Mono: system monospace
- Display, page title, section title, card title, body-large, body, metadata, and eyebrow roles

Editorial type is for narrative hierarchy, not dense controls or tables.

### Layout and control roles

- Content maximum: 1360px
- Portfolio maximum: 1328px
- Reading width: 72ch
- Responsive gutter: 20–52px
- Section gap: 64–128px
- Panel padding: 20–32px
- Global header: 82px desktop, 68px compact
- RolePacket sidebar reference: 238px
- Control heights: 36px, 44px, 52px
- Radius scale: 8px, 12px, 18px, 24px, pill
- Motion scale: 160ms, 240ms, 420ms
- Dialog z-index: 80

## 6. Foundations and accessibility

The body MUST use the shared dot texture over the canvas token. Products MUST NOT layer a visible grid over it.

Every interactive element exposes the shared dual focus treatment:

- 2px focus ring
- 3px offset
- 5px contrasting gap
- Light, dark, or accent gap color appropriate to the surface

Additional requirements:

- Focus remains visible in forced-colors mode.
- Escape closes menus, drawers, and dialogs where expected and restores focus.
- Modal and off-canvas interactions contain focus while open.
- Closed off-canvas navigation is inert or removed from the tab order.
- Hover-only disclosure is prohibited for essential content.
- Status includes text; color or icons alone are insufficient.
- Errors include a written reason and recovery action.
- Important success remains persistent rather than toast-only.
- Media includes useful alternative text or a caption when it adds meaning.
- Native dialogs use explicit accessible names and descriptions.
- Dialog cancellation, backdrop behavior, and initial focus remain product-owned and MUST be tested.
- Actual assistive-technology and forced-colors review remains a recorded manual release requirement until an equivalent automated check exists.

## 7. Shared global header

Every owned page or application state renders the shared `jl-global-header` visual contract.

Canonical identity labels:

- `Johnny Li / Portfolio`
- `Johnny Li / Network Diagnostics`
- `Johnny Li / RolePacket`

Desktop contract:

- 82px minimum height
- 1328px inner rail with responsive gutters
- Identity in the first column
- Optional product navigation in the middle column
- Sites control in the final column
- Exact 88×44px Sites control with 13px/700 UI typography and a CSS-drawn chevron

Compact contract:

- 68px minimum height
- Owner and separator MAY hide while product identity remains
- Sites control remains 88×40px
- Product navigation remains reachable through the shared compact-menu shell or an equivalent accessible product pattern

Every owned site reaches the other two within two interactions. Owned-site links open in the same tab. External destinations MAY open in a new tab.

## 8. Shared site controls

`scripts/site-controls.js` is framework-neutral and has no runtime dependency.

### Canonical site directory

`OWNED_SITES` is the source of truth for stable site IDs, display labels, and canonical production URLs. Consumers SHOULD render it directly where their build system permits. Static fallback markup MUST remain consistent with it.

### Sites-menu controller

`installSiteSwitcher()` owns:

- Button click toggle
- Outside-pointer close
- Escape close with focus restoration
- ArrowDown and ArrowUp entry and cycling
- Home and End navigation
- Link-selection close
- `aria-expanded` and `hidden` synchronization

Products MAY close their own compact navigation or workspace drawer before the Sites menu opens.

### Compact header-menu controller and shell

`installHeaderMenu()` owns the same disclosure and keyboard contract for compact product navigation. Product labels, destinations, and active-state logic remain local.

- `jl-header-menu-toggle`: compact navigation trigger
- `jl-header-menu`: product navigation popover shell
- `jl-header-menu--open`: visible compact state

At 900px and below, the shell uses shared gutters, surface, border, radius, shadow, row height, hover treatment, and forced-colors border behavior. At wider widths, product navigation returns to the normal header slot.

## 9. Shared content references and primitives

### Reference content layer

`styles/content.css` and `styles/content-guard.css` provide REFERENCE utilities for page rails, heroes, titles, ledes, metadata, sections, grids, prose, panels, ruled structures, process steps, metrics, semantic callouts, actions, code, media, tables, and empty states.

Existing product-local classes remain conforming when they preserve approved composition, shared token roles, accessibility outcomes, responsive behavior, and product ownership.

### Standalone primitive layer

`styles/content-primitives.css` is standalone after `tokens.css`. It does not depend on `content.css`.

It provides:

- `jl-actions`
- `jl-button`, including primary, compact, and danger variants
- `jl-callout`, including semantic variants
- `jl-empty-state`
- `jl-table-region`
- `jl-dialog`
- `jl-dialog__surface`
- `jl-dialog__title`
- `jl-dialog__message`
- `jl-dialog__actions`

The primitive layer owns reusable structure, interaction-safe defaults, compact transformations, and forced-colors borders. Products customize approved geometry and expression through documented `--jl-*` custom properties.

Products MUST NOT copy shared structural declarations into mapping files. Mapping files contain variables and genuinely product-specific content styling only.

### Native-dialog contract

The shared dialog shell owns transparent native-dialog reset, viewport placement, maximum dimensions, backdrop hooks, surface geometry, title and message styling hooks, action layout, compact stacking, and forced-colors fallback.

Products own whether and when a dialog opens; queueing, cancellation, confirmation, and focus restoration; accessible labels and descriptions; product wording and tone; workflow-specific content; dimensions, density, colors, and animation through shared hooks.

## 10. Consumer distribution and synchronization

Consumers pin an exact reviewed commit. Floating branches and runtime content-delivery network imports are prohibited.

Each consumer records the package name, semantic version, immutable source commit, and generated source metadata. Shared assets are copied into the consumer build artifact and validated against the lock.

### Consumer release resolver

`scripts/consumer-release.mjs` MUST:

- Accept only repository-local output paths
- Reject paths that escape the current repository
- Update only the design-system lock and an explicitly supplied local package manifest
- Avoid subprocess execution and arbitrary validation commands
- Validate commit and semantic-version formats

Consumers MAY commit synchronized local copies of small shared helpers when installing the package would cause unnecessary lockfile churn. Every copy MUST be included in design-system drift validation.

### Reusable update workflow

`.github/workflows/consumer-design-system-sync.yml` owns checkout, Node setup, consumer installation invocation, release resolution, synchronization invocation, validation invocation, tracked-path change detection, update-branch publication, and draft pull-request creation or refresh.

Each consumer owns schedule, manual trigger, Node version, installation command, validation command, tracked paths, and product name. Consumer workflows MUST pin reusable workflows to immutable design-system commits.

### Machine-readable conformance

`conformance/contract.json` assigns stable rule IDs to enforceable requirements in this document. Each rule records title, description, severity, applicable products, accepted evidence classes, and a canonical source section.

Each consumer MUST provide `design-system.conformance.json` after adopting the conformance framework. Applicable rules MUST have repository-local evidence or an explicit manual status. Unknown rules and missing applicable declarations fail.

`scripts/conformance-runner.mjs` MUST:

- Read data only and never execute consumer commands
- Confine the manifest, evidence files, and report output to the consumer repository
- Support file, fragment, regular-expression, and JSON evidence
- Produce machine-readable JSON and human-readable Markdown reports
- Block required automated failures and manual failures
- Record pending manual checks without treating them as automated passes
- Support strict-manual mode for final release approval

`.github/workflows/consumer-conformance.yml` standardizes checkout, Node setup, consumer command invocation, and report artifact upload. The consumer remains responsible for building meaningful application states and running its own tests.

A reduced viewport MUST NOT be described as actual browser zoom. Automated narrow-layout checks and actual 200% browser zoom review are separate evidence.

## 11. Approved product baselines

### Portfolio

Preserve homepage composition and section rhythm, editorial display hierarchy, numbered selected-work rows, narrative case studies, restrained terracotta use, dark contact and next-project sections, and responsive navigation/contact availability.

Case-study headers SHOULD exist in source HTML rather than being constructed by runtime enhancement. Technical cleanup MUST preserve the rendered design.

The portfolio adopts the shared updater workflow and selected content primitives. It does not adopt the shared dialog shell because it has no matching product dialog.

### Network Diagnostics

Preserve hero and sticky test controls; Quick, Full, and Stress profiles with duration and maximum-transfer disclosure; idle and loaded conditions; metric cards, charts, findings, tables, recent history, and native probe; local-only result history; terracotta hierarchy with product-owned analytical colors; and the exact dot canvas without a visible grid.

Browser request loss MUST NOT be labeled raw packet loss. Charts retain stable labels, summaries, and grayscale distinction.

The data-use confirmation dialog uses the shared dialog shell. Transfer-cap logic, remembered consent, checkbox content, wording, and test behavior remain product-owned.

### RolePacket

Preserve the dense review-first workflow, wide sidebar and accessible compact drawer, ruled application rows, explicit status and provenance, before/proposed comparisons, resume preview, version history, answer matching, notes, memory workflows, and current panel density/form structure.

RolePacket feature work MAY substantially change workflow behavior. It MUST NOT force workflow-specific patterns onto the portfolio or Network Diagnostics.

The reusable confirmation service uses the shared dialog shell. Queueing, extension events, destructive/default tone selection, wording, and focus behavior remain product-owned. The workspace drawer remains entirely product-owned.

## 12. Component states and responsive behavior

Every interactive product component defines the states that apply: default, hover, focus-visible, disabled, loading or pending, empty, error with recovery, important success, compact transformation, forced-colors behavior, and reduced-motion behavior.

Responsive requirements:

- Two-column heroes become one before either side becomes cramped.
- Four-column metrics become two, then one.
- Multi-column forms become one before labels or errors become cramped.
- Sidebars become accessible drawers or equivalent navigation.
- Before/proposed comparisons stack vertically.
- Genuine tables MAY scroll inside labeled regions.
- Action groups stack to full-width controls when needed.
- Dialogs remain within the viewport and preserve reachable actions.
- No document-level overflow at 320px.
- Pages remain usable at actual 200% browser zoom.

## 13. Motion, privacy, and performance

- Motion is restrained and functional.
- Reduced-motion users receive no nonessential movement.
- Loading motion includes written status.
- Shared assets are packaged locally and are not fetched from a runtime CDN.
- Runtime third parties are disclosed at the point of use.
- Results and private workflow data are not added to unrelated analytics or advertising systems.
- Shared CSS and JavaScript remain dependency-free.
- Product bundles avoid duplicate shared assets.
- Static pages SHOULD avoid JavaScript for content that can exist in source HTML.
- New visual dependencies require a measured reason and ownership record.
- Update and conformance automation MUST not weaken consumer validation or bypass repository protections.
- Bundle and user-experience performance baselines remain manual-pending until measured and approved; automation MUST not invent thresholds before that record exists.

## 14. Governance

A shared change includes atomic tokens, global accessibility behavior, global header and site controls, canonical site registry, shared semantic roles, shared primitive and dialog structure, consumer release and synchronization tooling, conformance contract and runner, shared responsive principles, and optional reusable content utilities.

A product-local change includes portfolio narrative composition; Network measurement logic, charts, controls, profiles, Worker and probe behavior; RolePacket authentication, application state, workflow logic, APIs, storage, extension behavior, and workspace drawer; product-specific spacing, density, animation, copy, or color expression; consumer state fixtures; and consumer validation commands and schedules.

Shared distributable changes require:

1. Design-system update
2. Semantic-version decision
3. Canonical documentation, specimen, or contract update
4. Package validation and conformance-runner self-test
5. Immutable consumer pin update
6. Product-level static, runtime, visual, and application tests
7. Visual comparison when appearance changes
8. Independent consumer pull requests and rollback boundaries
9. Cross-consumer release-gate validation after all consumers support the contract
10. Recorded manual approval for checks that cannot be automated honestly

Documentation-only changes do not require repinning when packaged assets are unchanged.

### Conformance checklist

- Uses the current reviewed shared-asset source
- Preserves approved appearance unless change is intentional
- Uses the exact dot canvas without a second grid
- Renders the shared header on every route or state
- Uses the canonical site directory and shared interaction contract
- Uses shared compact-menu geometry where applicable
- Uses shared tokens or documented product aliases
- Uses standalone primitives where adopted and does not retain equivalent structural fallbacks
- Uses the shared dialog shell for matching native confirmation dialogs
- Keeps product dialog logic, wording, state, and focus behavior local
- Pins shared workflows and generated assets to immutable commits
- Keeps consumer schedules, state fixtures, and validation commands product-owned
- Provides evidence for every applicable machine-readable rule
- Distinguishes automated narrow-layout evidence from actual browser-zoom review
- Preserves product-specific information architecture
- Does not hide essential compact navigation
- Has no document-level overflow at 320px
- Remains usable at actual 200% zoom
- Supports keyboard, focus, reduced motion, and forced colors
- Communicates semantic status with text and appropriate token roles
- Keeps tables, code, charts, dialogs, and media locally bounded
- Gives every empty and error state a recovery path
- Discloses every external or third-party interaction
