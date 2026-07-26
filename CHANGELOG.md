# Changelog

## 1.4.0 — 2026-07-26

- Added the shared page-content layer for every owned page and application state.
- Added canonical rails, heroes, titles, ledes, metadata, sections, prose, grids, stacks, panels, ruled lists, process steps, metrics, semantic callouts, actions, code blocks, media, tables, and empty states.
- Added 900px and 560px responsive transformations, container-aware grids, forced-colors borders, and mobile action stacking.
- Added the `./content.css` package export and included it in the root stylesheet.
- Expanded package validation to enforce the complete page-content contract and prevent undefined-token, raw-color, import, and responsive drift.
- Coordinated the migration of the portfolio homepage and every project case study, every Network Diagnostics state, and every RolePacket workflow screen.

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
