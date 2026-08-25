# Changelog

## Unreleased

- Replaced the canonical Sites disclosure indicator with a geometrically centered inline SVG chevron; the open state now rotates around the icon center instead of relying on vertical pixel offsets. Legacy text-span indicators remain temporarily supported for consumer compatibility.
- Added the package-owned `jl-global-header--compact-utility` expression: a 72px desktop bar with a unified 96px Sites + 44px Settings utility cluster, while preserving full control hit targets, disclosure behavior, accessibility, and existing compact/mobile geometry.

## 1.9.0 — 2026-08-06

- Promoted the proven Portfolio wide-desktop header rail into the shared contract: 40px left identity inset, 20px right controls inset, optically centered contextual navigation, and an intentionally empty center zone when a product has no global nav.
- Added shared System, Light, and Dark appearance preferences with a pre-paint bootstrap.
- Added cross-subdomain preference persistence for all owned sites.
- Added dark semantic color and status tokens while preserving the approved warm editorial palette.
- Moved Appearance into an adjacent Settings disclosure with an icon-only System, Light, and Dark selector instead of placing theme controls inside Sites.
- Unified the primary terracotta accent family across light and dark themes while retaining theme-specific neutral, semantic, focus, selection, and soft-accent roles.
- Finalized the shared header as adjacent 104px Sites and 44px Settings controls on desktop, with 40px compact controls and a 96px Sites fallback at the extreme compact breakpoint.
- Added unified expanding Sites and Settings shells with content-driven height, centered menu content, downward clip reveal, mutual exclusion, and reduced-motion handling.
- Pinned the complete header while either disclosure is open, preserved the normal header footprint to prevent page shifts, and added the complete-header dismissal animation after close.
- Locked the final disclosure footprint to 83px on desktop and 69px on compact layouts and finalized the 400ms dismissal timing.
- Forced print and PDF output back to the light paper theme.
- Added a required conformance rule for shared theme adoption and expanded header-contract validation for the final disclosure behavior.
- Reconciled the normative design documentation, migration status, package status, and conformance wording with the approved production implementation on 2026-08-08.

## 1.8.2 — 2026-07-28

- Added a cross-consumer candidate gate that validates Website, Network Diagnostics, and RolePacket before a shared release can merge.
- Added a strict consumer-manifest schema and package export.
- Strengthened the conformance runner to validate declaration shapes, evidence properties, lock provenance, and contract-version alignment.
- Added design-system source and consumer commit provenance to JSON and Markdown reports.
- Expanded runner self-tests for malformed manifests, contract/lock mismatch, report provenance, and repository-boundary enforcement.
- Required consumer integration validators to derive release identity from their lock files so scheduled updates do not self-block.

## 1.8.1 — 2026-07-28

- Added an extreme-compact header transformation at 360px and below.
- Preserved the full product identity, Menu trigger, and exact 88px Sites control at the supported 320px viewport.
- Reduced only compact gutters, gaps, identity size, and Menu-trigger width rather than hiding required navigation.
- Added a dedicated regression guard for the 320px shared-header contract.

## 1.8.0 — 2026-07-28

- Added a versioned machine-readable conformance contract with stable `DS-*` rule identifiers tied to canonical design-system sections.
- Added a dependency-free consumer evidence runner that produces JSON and Markdown reports without executing consumer commands.
- Added repository-confined file, fragment, regular-expression, and JSON evidence with path-escape rejection.
- Added explicit manual-passed, manual-pending, and manual-failed states plus strict-manual release mode.
- Added a reusable consumer conformance workflow with standard report artifact handling.
- Added runner self-tests for normal reports, strict manual blocking, and repository-boundary enforcement.
- Kept product state construction, visual audits, builds, application tests, and deployment checks in their owning repositories.

## 1.7.0 — 2026-07-28

- Added a variable-backed native-dialog shell covering centering, backdrop, surface, title, message, actions, compact placement, and forced-colors behavior.
- Added a constrained consumer release helper that resolves the reviewed design-system commit and updates repository-local lock metadata without executing arbitrary commands.
- Added a reusable GitHub Actions workflow for validated design-system update pull requests across consumer repositories.
- Expanded package validation to protect the dialog contract, repository-local path guard, reusable workflow, and new package export.
- Preserved product-controlled modal dimensions, density, colors, content, state, and confirmation behavior.

## 1.6.1 — 2026-07-28

- Made `content-primitives.css` fully standalone after `tokens.css`.
- Added the structural flex, inline-flex, alignment, text-decoration, white-space, and cursor behavior previously inherited from the larger content layer.
- Expanded validation to prevent the small export from silently depending on `content.css` again.

## 1.6.0 — 2026-07-28

- Added variable-backed button, action, callout, empty-state, and table-region shells for selective cross-product adoption.
- Added compact and danger button variants while preserving product-controlled geometry through documented custom properties.
- Added a daily and manually dispatchable smoke check for the portfolio, Network Diagnostics, and the Cloudflare Access-protected RolePacket deployment.
- Added optional authenticated RolePacket smoke coverage through Cloudflare Access service-token secrets.
- Expanded package validation to protect the adaptable primitive hooks, export order, semantic variants, and deployed-site smoke contract.
- Kept page composition, product controls, charts, workflow layouts, and product-specific behavior outside the shared package.

## 1.5.0 — 2026-07-27

- Declared the current production interfaces as the approved visual baseline.
- Clarified that unification applies to tokens, accessibility, canvas, global identity, semantic roles, and responsive principles rather than identical product layouts.
- Reclassified the page-content classes as reusable references for new work and deliberate consolidation instead of a mandatory rewrite target.
- Added the canonical owned-site registry and framework-neutral Sites-menu controller.
- Standardized outside-click, Escape, ArrowUp, ArrowDown, Home, End, focus-entry, and focus-restoration behavior.
- Added the shared compact header-menu toggle and popover shell used by the portfolio and Network Diagnostics.
- Added JavaScript and TypeScript package exports for shared site controls.
- Expanded package validation to protect the site directory, interaction contract, compact menu geometry, and typed export.

## 1.4.0 — 2026-07-26

- Added the shared page-content layer for every owned page and application state.
- Added canonical rails, heroes, titles, ledes, metadata, sections, grids, stacks, panels, ruled lists, process steps, metrics, semantic callouts, actions, code blocks, media, tables, and empty states.
- Added 900px and 560px responsive transformations, container-aware grids, forced-colors borders, and mobile action stacking.
- Added the `./content.css` package export and included it in the root stylesheet.
- Expanded package validation to enforce the complete page-content contract and prevent undefined-token, raw-color, import, and responsive drift.
- Added reference implementations adapted from the portfolio, Network Diagnostics, and RolePacket.

## 1.3.4 — 2026-07-25

- Moved the global-header component out of the optional cascade layer so generic product button resets cannot override it.
- Locked the Sites control to an exact 88 × 44px desktop geometry, 13px UI typography, and shared spacing.
- Replaced the font glyph chevron with a CSS-drawn chevron for identical rendering across products.
- Added a 40px compact-height transformation while preserving the same width and typography.

## 1.3.3 — 2026-07-25

- Replaced loosely shared site-identity styles with one concrete global-header component.
- Standardized header height, inner width, gutters, owner/product lockup, navigation slot, Sites control, border, and responsive behavior.
- Removed product-level casing, sizing, and identity variations from the shared contract.
- Added compatibility support for the earlier `jl-site-header` class while consumers migrate to `jl-global-header`.

## 1.3.2 — 2026-07-25

- Changed release packaging from repository traversal to explicit file allowlists.
- Added validation for CSS-specific token overrides and malicious-syntax regression checks.
- Expanded public-safety checks for sensitive filenames, credentials, private IP addresses, local home paths, and Cloudflare identifiers.
- Pinned GitHub Actions to immutable commit SHAs and disabled persisted checkout credentials.
- Added workflow concurrency and a five-minute timeout.
- Added Dependabot updates for pinned GitHub Actions.
- Added a security policy and private vulnerability-reporting guidance.
- Added a versioned package contract for consuming tokens and shared CSS across repositories.
- Added shared accessibility foundations and site-identity styling without product-specific components.
- Added package export, token-reference, raw-color, import, and version-drift validation.
- Corrected the specimen version and aligned its Network Diagnostics profiles with the public application.

## 1.3.1 — 2026-07-25

- Converted atomic tokens to DTCG 2025.10 structure.
- Added namespaced CSS extensions for fluid values.
- Added generated CSS, executable validation, release generation, and local serving.
- Added GitHub Actions and CODEOWNERS.
- Removed the committed combined specification; releases generate it into `dist/`.
- Consolidated the public documentation into one core specification and one migration file.
- Moved detailed product logic out of the public design-system core.
- Removed private repository commit snapshots and private source paths.
- Marked unmeasured performance limits as pending baselines.
- Expanded the specimen with patterns adapted from all three sites.
- Added an all-rights-reserved license while public licensing remains undecided.

## 1.3.0 — 2026-07-25

- Split the original monolithic document into a package with tokens, tooling, governance, and a specimen.
