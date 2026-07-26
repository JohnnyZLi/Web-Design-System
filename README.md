# Johnny Li Web Design System

[![Validate](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml/badge.svg)](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml)

A shared UI and UX system for `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev`.

**Version:** 1.3.2  
**Status:** Implementation candidate  
**License:** All rights reserved

The system is derived from all three websites:

- The portfolio supplies the palette, editorial typography, exact dot texture, open layout, and restrained terracotta treatment.
- Network Diagnostics supplies analytical controls, measurements, charts, and data-density patterns.
- RolePacket supplies workflow panels, application rows, review states, and comparison patterns.
- Shared accessibility, focus, semantic borders, token generation, and validation complete the system.

## Use

```bash
make generate       # regenerate tokens/tokens.css
make validate       # validate tokens, package contract, specimen, and public safety
make package-check  # validate only the consumable package contract
make serve          # preview http://localhost:8000/specimen/
make release        # generate a consolidated Markdown release and ZIP in dist/
```

Start with:

- [`specimen/index.html`](specimen/index.html) — visual reference
- [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) — permanent rules
- [`docs/MIGRATION.md`](docs/MIGRATION.md) — high-level rollout plan
- [`tokens/tokens.tokens.json`](tokens/tokens.tokens.json) — sole editable token source

## Consume from another repository

After this package contract is merged and the repository is tagged `v1.3.2`, JavaScript applications can pin the exact GitHub release:

```bash
npm install --save-exact "github:JohnnyZLi/Web-Design-System#v1.3.2"
```

Import the complete shared foundation from an application entry point:

```css
@import "@johnnyzli/web-design-system";
```

Or import only the layers a product needs:

```css
@import "@johnnyzli/web-design-system/tokens.css";
@import "@johnnyzli/web-design-system/foundations.css";
@import "@johnnyzli/web-design-system/site-identity.css";
```

The root stylesheet supplies generated tokens, the exact dot canvas, global accessibility foundations, and shared site-identity styles. It does not include portfolio layouts, Network Diagnostics charts, RolePacket workflows, authentication behavior, or product state.

Static sites should install the exact package during validation or deployment and copy the required CSS into their generated site artifact. Owned sites must not fetch the design system from a runtime CDN.

## Package contract

- [`package.json`](package.json) defines stable CSS and token exports.
- [`version.json`](version.json) records the package version and authoritative token source.
- [`styles/index.css`](styles/index.css) is the complete shared entry point.
- [`styles/foundations.css`](styles/foundations.css) provides the canvas, focus, selection, reduced-motion, forced-colors, and utility foundations.
- [`styles/site-identity.css`](styles/site-identity.css) provides styling hooks for the shared identity and site switcher; products retain their own menu behavior and routing.

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
