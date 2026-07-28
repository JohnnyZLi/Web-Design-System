# Johnny Li Web Design System

[![Validate](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml/badge.svg)](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml)

A shared UI and UX system for `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev`.

**Version:** 1.4.0  
**Package status:** Implementation candidate  
**Production visual baseline:** Approved  
**License:** All rights reserved

## Production baseline

The current production interfaces are the reference point for this system:

- The portfolio remains editorial, spacious, and primarily borderless.
- Network Diagnostics remains analytical, measurement-heavy, and chart-oriented.
- RolePacket remains dense, workflow-oriented, and optimized for review.

Unification does **not** mean making the three products look identical or replacing their existing layouts with the specimen. The shared contract covers the palette, exact dot canvas, typography roles, focus behavior, global header, Sites control, semantic states, responsive principles, and accessibility expectations. Product-specific composition, density, controls, charts, and workflow layout remain owned by each repository.

The package also includes reusable page-content utilities for future work and selective consolidation. Current consumers are not required to replace stable product markup solely to use those class names.

## Use

```bash
make generate       # regenerate tokens/tokens.css
make validate       # validate tokens, package contract, specimen, and public safety
make package-check  # validate only the consumable package contract
make serve          # preview http://localhost:8000/specimen/
make release        # generate a consolidated Markdown release and ZIP in dist/
```

Start with:

- [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) — permanent rules and ownership boundaries
- [`docs/MIGRATION.md`](docs/MIGRATION.md) — current rollout and conformance status
- [`specimen/index.html`](specimen/index.html) — component reference, not a replacement application theme
- [`tokens/tokens.tokens.json`](tokens/tokens.tokens.json) — sole editable token source

## Consume from another repository

Consumers pin an exact reviewed source commit rather than relying on a floating branch or runtime content-delivery network.

The current production sites synchronize the shared foundations they need:

```css
@import "@johnnyzli/web-design-system/tokens.css";
@import "@johnnyzli/web-design-system/foundations.css";
@import "@johnnyzli/web-design-system/site-identity.css";
```

The complete package remains available for new components or deliberate consolidation:

```css
@import "@johnnyzli/web-design-system";
```

The root stylesheet includes generated tokens, foundations, the exact dot canvas, the global header and Sites control, and reusable content utilities. Products retain their own application logic, charts, navigation behavior, authentication, workflow state, and data presentation.

Static sites copy the reviewed CSS into their generated artifact. Owned sites must not fetch the design system from a runtime CDN.

## Package contract

- [`package.json`](package.json) defines stable CSS and token exports.
- [`version.json`](version.json) records the package version and authoritative token source.
- [`styles/index.css`](styles/index.css) is the complete shared entry point.
- [`styles/foundations.css`](styles/foundations.css) provides canvas, focus, selection, reduced-motion, forced-colors, and utility foundations.
- [`styles/site-identity.css`](styles/site-identity.css) owns the shared global-header geometry, owner/product lockup, navigation slot, Sites control, and menu styling.
- [`styles/content.css`](styles/content.css) and [`styles/content-guard.css`](styles/content-guard.css) provide optional shared content primitives and resilience against generic resets.

## Structure

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── Makefile
├── package.json
├── version.json
├── tokens/
├── styles/
├── specimen/
├── scripts/
├── docs/
├── ci/
└── .github/
```

The repository is public, but public visibility does not grant permission to reuse the work. See `LICENSE`.

## Security

The repository validates release contents, package exports, CSS override syntax, common secret patterns, private network addresses, local home-directory paths, and sensitive filenames. Report vulnerabilities privately as described in [`SECURITY.md`](SECURITY.md).
