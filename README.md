# Johnny Li Web Design System

[![Validate](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml/badge.svg)](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml)

A shared UI and UX system for `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev`.

**Version:** 1.8.2  
**Package status:** Implementation candidate  
**Production visual baseline:** Approved  
**License:** All rights reserved

## Production baseline

The current production interfaces are the reference point for this system:

- The portfolio remains editorial, spacious, and primarily borderless.
- Network Diagnostics remains analytical, measurement-heavy, and chart-oriented.
- RolePacket remains dense, workflow-oriented, and optimized for review.

Unification does **not** mean making the three products look identical or replacing their existing layouts with the specimen. The shared contract covers the palette, exact dot canvas, typography roles, focus behavior, global header, Sites control, compact header-menu shell, semantic states, responsive principles, accessibility expectations, and machine-readable conformance rules. Product-specific composition, density, controls, charts, application state, and workflow layout remain owned by each repository.

The shared header preserves the full product identity, Menu trigger, and exact 88px Sites control at the supported 320px viewport through an extreme-compact transformation rather than hiding required navigation.

The package also includes reusable page-content utilities for future work and selective consolidation. Current consumers are not required to replace stable product markup solely to use those class names.

## Use

```bash
make generate       # regenerate tokens/tokens.css
make validate       # validate tokens, package contract, specimen, and public safety
make package-check  # validate only the consumable package contract
make serve          # preview http://localhost:8000/specimen/
make release        # generate a consolidated Markdown release and ZIP in dist/
node scripts/smoke-deployments.mjs
node scripts/test-conformance-runner.mjs
python scripts/validate_header_contract.py
```

Start with:

- [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) — permanent rules and ownership boundaries
- [`docs/CONFORMANCE.md`](docs/CONFORMANCE.md) — machine-readable rule and evidence model
- [`docs/MIGRATION.md`](docs/MIGRATION.md) — current rollout and conformance status
- [`specimen/index.html`](specimen/index.html) — component reference, not a replacement application theme
- [`tokens/tokens.tokens.json`](tokens/tokens.tokens.json) — sole editable token source

## Consume from another repository

Consumers pin an exact reviewed source commit rather than relying on a floating branch or runtime content-delivery network.

The current production sites synchronize the shared foundations and site controls they need:

```css
@import "@johnnyzli/web-design-system/tokens.css";
@import "@johnnyzli/web-design-system/foundations.css";
@import "@johnnyzli/web-design-system/site-identity.css";
```

```js
import {
  OWNED_SITES,
  installHeaderMenu,
  installSiteSwitcher,
} from "@johnnyzli/web-design-system/site-controls.js";
```

`OWNED_SITES` is the canonical cross-site directory. The framework-neutral controllers provide consistent outside-click, Escape, ArrowUp, ArrowDown, Home, End, focus-entry, focus-restoration, and compact-menu behavior without adding a runtime framework dependency.

The complete CSS package remains available for new components or deliberate consolidation:

```css
@import "@johnnyzli/web-design-system";
```

Products that need only adaptable buttons, callouts, empty states, action groups, table regions, or native-dialog structure can import the standalone shell immediately after shared tokens:

```css
@import "@johnnyzli/web-design-system/content-primitives.css";
```

The standalone export includes its own structural display, alignment, interaction, responsive, and forced-colors behavior; it does not require `content.css`. It exposes `--jl-button-*`, `--jl-callout-*`, `--jl-empty-state-*`, `--jl-actions-*`, `--jl-table-region-*`, and `--jl-dialog-*` customization hooks. Consumers should tune those variables rather than copying complete structural declarations. Semantic variants remain shared while product-specific density and expression remain local.

Static sites copy the reviewed assets into their generated artifact. Owned sites must not fetch the design system from a runtime CDN.

## Consumer release automation

[`scripts/consumer-release.mjs`](scripts/consumer-release.mjs) exposes a constrained helper for resolving the reviewed `main` commit and updating a repository-local `design-system.lock.json`. It may also update the package dependency when a consumer explicitly supplies its local `package.json`; it cannot write outside the current repository or execute commands.

[`.github/workflows/consumer-design-system-sync.yml`](.github/workflows/consumer-design-system-sync.yml) is a reusable workflow. Consumer repositories keep their own install and validation commands, while the shared workflow owns update resolution, synchronization invocation, change detection, branch publication, and draft pull-request creation.

Consumer integration checks derive the expected package version and source commit from `design-system.lock.json`. This lets an update synchronize a new candidate and validate it before opening a pull request instead of failing against hard-coded metadata from the previous release.

## Conformance testbench

[`conformance/contract.json`](conformance/contract.json) gives enforceable design-system requirements stable `DS-*` rule IDs. Each rule names the products it applies to, its severity, accepted evidence classes, and the canonical design-document section that owns it.

[`conformance/manifest.schema.json`](conformance/manifest.schema.json) defines the strict consumer declaration shape. Unknown properties, unsupported evidence types, malformed manual states, and incomplete evidence declarations are rejected before rule evaluation.

[`scripts/conformance-runner.mjs`](scripts/conformance-runner.mjs) evaluates a consumer-owned `design-system.conformance.json` manifest. It supports repository-confined file, fragment, regular-expression, and JSON evidence; verifies that the consumer lock version matches the conformance contract; emits design-system and consumer commit provenance in JSON and Markdown reports; blocks required failures; and tracks actual browser zoom, assistive-technology review, and performance approval as explicit manual items. It deliberately does not execute consumer commands.

```bash
node node_modules/@johnnyzli/web-design-system/scripts/conformance-runner.mjs
```

[`.github/workflows/consumer-conformance.yml`](.github/workflows/consumer-conformance.yml) is the reusable pipeline shell. Consumers retain the command that builds states and runs product tests; the shared workflow standardizes checkout, Node setup, execution, and report artifacts.

[`.github/workflows/consumer-candidate-gate.yml`](.github/workflows/consumer-candidate-gate.yml) checks the current design-system candidate against Website, Network Diagnostics, and RolePacket before a shared release is merged. Each product keeps its own build and validation commands, while the gate proves that the package candidate can synchronize and pass all three integration boundaries.

## Deployed smoke checks

`.github/workflows/deployed-smoke.yml` checks all three owned domains every day and on manual dispatch. The public sites must return their expected product marker, shared header, and complete Sites directory. RolePacket is expected to remain behind Cloudflare Access; optional `ROLEPACKET_ACCESS_CLIENT_ID` and `ROLEPACKET_ACCESS_CLIENT_SECRET` repository secrets enable an authenticated application-shell check.

## Package contract

- [`package.json`](package.json) defines stable CSS, token, site-control, consumer-release, and conformance exports.
- [`version.json`](version.json) records the package version and authoritative token source.
- [`styles/index.css`](styles/index.css) is the complete shared CSS entry point.
- [`styles/foundations.css`](styles/foundations.css) provides canvas, focus, selection, reduced-motion, forced-colors, and utility foundations.
- [`styles/site-identity.css`](styles/site-identity.css) owns the shared global-header geometry, owner/product lockup, navigation slot, Sites control, compact and extreme-compact header-menu shells, and menu styling.
- [`scripts/site-controls.js`](scripts/site-controls.js) owns the site directory and framework-neutral Sites and header-menu controllers.
- [`scripts/site-controls.d.ts`](scripts/site-controls.d.ts) provides the TypeScript contract for the shared controllers.
- [`styles/content.css`](styles/content.css) and [`styles/content-guard.css`](styles/content-guard.css) provide optional content patterns and resilience against generic resets.
- [`styles/content-primitives.css`](styles/content-primitives.css) provides standalone, adaptable cross-product shells for selective consolidation, including native dialogs.
- [`scripts/consumer-release.mjs`](scripts/consumer-release.mjs) provides constrained consumer lock resolution.
- [`scripts/conformance-runner.mjs`](scripts/conformance-runner.mjs) evaluates consumer evidence and writes provenance-bearing reports.
- [`conformance/contract.json`](conformance/contract.json) is the versioned machine-readable rule source.
- [`conformance/manifest.schema.json`](conformance/manifest.schema.json) defines the consumer evidence-manifest contract.
- [`scripts/smoke-deployments.mjs`](scripts/smoke-deployments.mjs) validates the live domain and Access-gate contract.

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
├── conformance/
├── specimen/
├── scripts/
├── docs/
├── ci/
└── .github/
```

The repository is public, but public visibility does not grant permission to reuse the work. See `LICENSE`.
