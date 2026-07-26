# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.4.0  
**Status:** Implementation candidate  
**Owner:** Johnny Li

- **MUST** means required for conformance.
- **SHOULD** means expected unless a documented exception exists.
- **MAY** means optional.
- **CURRENT** describes existing behavior.
- **TARGET** describes intended post-migration behavior.

The system becomes an implementation contract only after the specimen is approved, current production baselines are recorded, tokens and shared content foundations are integrated into all three sites, and the core migrations pass product-level and manual production testing.

## 2. Identity and sources

> **Editorial warmth, systems precision.**

The sites MUST feel related without becoming identical:

- Portfolio: editorial and spacious
- Network Diagnostics: analytical and data-oriented
- RolePacket: dense and workflow-oriented

### Source mapping

**Portfolio contribution**

- Warm off-white canvas
- Near-black ink
- Terracotta accent
- Editorial serif for large display roles
- Exact faint dot texture
- Open section rhythm
- Restrained motion

**Network Diagnostics contribution**

- Explicit measurement scope
- Segmented test controls
- Metric and chart systems
- Tables and imported reports
- Semantic service states
- Data-dense responsive patterns

**RolePacket contribution**

- Dense review-first workflows
- Ruled application rows
- Sidebars and compact drawers
- Before/proposed comparisons
- Persistent status and provenance
- Forms, review actions, versions, and confirmation patterns

## 3. Principles

1. Share foundations and content structure, not product identity.
2. Preserve information architecture before decorative detail.
3. Use one accessible terracotta accent; reserve other hues for semantic or analytical meaning.
4. Make state, evidence, scope, and recovery explicit.
5. Prefer responsive reflow over clipping, shrinking, or hidden essential navigation.
6. Keep runtime dependencies and third-party data sharing minimal.
7. Product adapters MUST NOT redefine shared global-header or shared page-content contracts.
8. Content MUST remain understandable without color, animation, hover, or a wide viewport.

## 4. Atomic tokens

The editable token source is `tokens/tokens.tokens.json`. Generated CSS is not edited manually.

### Color roles

- `canvas`: default page background
- `canvasDot`: exact shared dot texture
- `surface`: raised content surface
- `surfaceMuted`: low-emphasis surface
- `surfaceStrong`: stronger grouped surface
- `surfaceInverse`: dark inverse surface
- `ink`: primary text and strong rules
- `text`: body copy
- `muted`: metadata and secondary copy
- `accent`: accessible terracotta interaction and emphasis
- semantic success, warning, danger, info, and violet triplets: text, surface, and border

Raw colors MUST NOT appear in shared CSS. Product chart colors MAY remain product-owned when they have stable labels and grayscale meaning.

### Typography roles

- UI: system sans-serif stack
- Editorial: Iowan/Palatino/Georgia-style serif stack
- Mono: system monospace stack
- Display, page title, section title, card title, body-large, body, metadata, and eyebrow roles

Editorial type is for prominent narrative hierarchy, not dense control labels or tables.

### Layout roles

- Content maximum: 1360px
- Portfolio maximum: 1328px
- Reading width: 72ch
- Responsive gutter: 20–52px
- Section gap: 64–128px
- Panel padding: 20–32px
- Global header: 82px desktop, 68px compact
- RolePacket sidebar: 238px wide at desktop

### Controls, radii, motion, and elevation

- Small, medium, and large control heights: 36px, 44px, and 52px
- Radius scale: 8px, 12px, 18px, 24px, pill
- Motion scale: 160ms, 240ms, 420ms
- Shared ease-out curve
- Low and high warm-neutral shadows
- Reduced motion removes nonessential transitions and smooth scrolling

## 5. Canvas and surfaces

The default body canvas MUST use the exact shared dot texture over the canvas token. Products MUST NOT layer a visible grid over that dot texture.

Surfaces are used by information need:

- Canvas: page and broad workflow background
- Surface: panels, controls, tables, cards
- Surface muted: supporting content, code alternatives, grouped detail
- Surface strong: selected or strong grouping where contrast remains sufficient
- Inverse surface: restrained dark sections and selected terminal/code contexts

The portfolio MAY use more borderless and open composition. Network and RolePacket MAY use more panels and ruled structures. All use the same token roles.

## 6. Accessibility contract

### Focus

Every interactive element MUST expose the shared dual focus treatment:

- 2px focus ring
- 3px offset
- 5px contrasting gap
- appropriate light, dark, or accent gap color

Focus MUST remain visible in forced-colors mode.

### Keyboard and interaction

- All navigation, menus, drawers, dialogs, details, forms, and application actions MUST be keyboard operable.
- Escape closes menus, drawers, and dialogs where expected and restores focus to the trigger.
- Modal and off-canvas interactions MUST contain focus while open.
- Closed off-canvas navigation MUST be inert or otherwise removed from the tab order.
- Hover-only disclosure is prohibited for essential content.

### Semantics

- Every page has one primary heading.
- Sections use ordered heading levels.
- Tables use header cells and remain inside explicit responsive regions.
- Status MUST include text; color or icons alone are insufficient.
- Errors include a written reason and recovery action.
- Important success remains persistent rather than toast-only.
- Media requires useful alternative text or a caption when the visual adds meaning.

### Responsive and zoom

Required transformations:

- Two-column heroes become one column.
- Four-column metric grids become two, then one.
- Multi-column forms become one before labels or errors become cramped.
- Sidebars become an accessible compact drawer or an equivalent explicitly documented navigation transformation.
- Before/proposed comparisons stack vertically.
- Genuine tables MAY scroll inside a labeled region; essential summaries remain available without scrolling.
- Action groups stack to full-width controls when needed.
- No page may have document-level overflow at 320px.
- Pages MUST remain usable at 200% browser zoom.

## 7. Shared global header

Every owned website page MUST use the shared `jl-global-header` component contract. Product adapters MUST NOT redefine the header rail, owner/product typography, Sites control geometry, or menu styling.

Canonical identity labels:

- `Johnny Li / Portfolio`
- `Johnny Li / Network Diagnostics`
- `Johnny Li / RolePacket`

The desktop header uses:

- 82px minimum height
- Shared 1328px inner rail and responsive gutters
- Owner/product identity in the first column
- Optional product navigation in the middle column
- Sites control in the final column
- Exact 88×44px Sites control with 13px/700 UI typography and a CSS-drawn chevron

At compact widths the header becomes 68px high, hides the owner and separator while retaining the product identity, and keeps the Sites control at 88×40px.

Product navigation that no longer fits MUST remain reachable through a product-owned compact navigation pattern rather than disappearing.

Every owned site MUST reach the other two within two interactions. Owned-site links open in the same tab. External destinations MAY open in a new tab.

## 8. Shared page-content system

`styles/content.css` owns structural roles used across every page and application state. Products MAY add product classes beside these roles, but MUST NOT replace the core geometry, typography, or responsive transformations with unrelated values.

### Page rails

- `jl-page`: page root and ink role
- `jl-page__inner`: standard 1360px content rail
- `jl-page__inner--portfolio`: 1328px editorial rail
- `jl-reading-width`: 72ch reading measure
- `jl-responsive-region`: container-aware local responsive boundary

### Heroes

- `jl-page-hero`
- `jl-page-hero__grid`
- `jl-page-title`
- `jl-page-lede`
- `jl-page-meta`
- `jl-meta-item`

Hero title, lede, actions, and metadata MUST remain distinct. Metadata MUST reflow rather than shrink into unreadable columns.

### Sections

- `jl-page-section`
- `jl-page-section__header`
- `jl-page-section__index`
- `jl-page-section__title`
- `jl-page-section__body`

Sections use a top rule, concise label, and deliberate body spacing. A product MAY omit the numeric index but MUST retain a visible section heading.

### Content grids

- `jl-content-grid`: 12-column editorial/content grid
- `jl-content-grid__lead`: primary narrative area
- `jl-content-grid__support`: supporting explanation or controls
- `jl-grid-2`, `jl-grid-3`, `jl-grid-4`
- `jl-stack`, `jl-stack--tight`, `jl-stack--loose`
- `jl-cluster`

Wide grids MUST reflow at the shared 900px and 560px breakpoints. Product CSS MAY introduce earlier breakpoints when content requires it.

### Prose and editorial hierarchy

- `jl-eyebrow`
- `jl-prose`
- `jl-editorial-lead`

Body prose uses the shared reading width and 1.6 line height. Long-form pages MUST NOT use arbitrary paragraph widths or unrelated font stacks.

### Panels and ruled structures

- `jl-panel`
- `jl-panel--flat`
- `jl-panel--muted`
- `jl-panel--strong`
- `jl-ruled-grid`

Panels use shared surface, border, radius, padding, and shadow roles. Portfolio MAY use flat panels; workflow and analytical products MAY retain raised or ruled surfaces.

### Process and metric patterns

- `jl-process-list`
- `jl-process-list__step`
- `jl-metric-grid`
- `jl-metric`
- `jl-metric__value`
- `jl-metric__label`

Process stages and metrics use explicit labels and readable values. Metric meaning MUST remain visible without color.

### Semantic callouts

- `jl-callout`
- `jl-callout--success`
- `jl-callout--warning`
- `jl-callout--danger`
- `jl-callout--info`

Semantic callouts MUST use the complete text, surface, and border token triplet.

### Actions

- `jl-actions`
- `jl-button`
- `jl-button--primary`

Primary action count SHOULD remain one per local decision group. Destructive actions retain product-owned confirmation behavior and semantic danger treatment.

### Code, media, tables, and empty states

- `jl-code-block`
- `jl-media`
- `jl-media__frame`
- `jl-table-region`
- `jl-empty-state`

Code blocks and tables may scroll locally, never at the document level. Media frames preserve intrinsic dimensions. Empty states explain what is absent and, when relevant, how to proceed.

## 9. Component state requirements

Every canonical component defines:

- Default
- Hover where pointer interaction exists
- Focus-visible
- Disabled where applicable
- Loading or pending where applicable
- Empty where applicable
- Error with recovery
- Success when important
- Compact transformation
- Forced-colors behavior
- Reduced-motion behavior when animated

| State | Required communication |
|---|---|
| Loading | Written activity and stable layout |
| Empty | What is absent and how to proceed |
| Error | Written reason and recovery |
| Success | Persistent when important; not color- or toast-only |
| Disabled | Reduced emphasis without removing readable labels |

## 10. Product patterns

### Portfolio

Preserve:

- Editorial display hierarchy
- Open composition and restrained panels
- Numbered selected-work rows
- Narrative case studies
- Dark contact/next-project sections

Required:

- Homepage and every case study use shared header and content roles.
- Project heroes use shared title, lede, actions, and metadata.
- Case-study sections use shared section, prose, process, panel, metric, code, and action patterns.
- Work rows stack as metadata, title, description, and action at compact widths.
- Project navigation and contact remain accessible at all widths.

### Network Diagnostics

Preserve:

- Explicit data-use disclosure
- Quick, Full, and Stress test profiles
- Separate idle, download-loaded, and upload-loaded conditions
- Analytical charts and tables
- Optional native deep probe
- Local-only recent history

Required:

- Idle, running, error, completed, saved-history, methodology, privacy, import, and imported-report states use shared content roles.
- Each profile shows name, duration, and maximum transfer.
- Findings, recommendations, service status, and errors use complete semantic roles.
- Tables remain in local responsive regions.
- Charts retain stable labels, summaries, and grayscale distinction.
- Browser request loss is not labeled raw packet loss.

Stable analytical mapping remains product-owned and MUST be documented in product code.

### RolePacket

Preserve:

- Dense review-first workflow
- Sidebar at wide widths and accessible drawer at compact widths
- Ruled application rows
- Explicit status and provenance
- Before/proposed comparisons
- Version history and reusable memory

Required:

- Login, loading, dashboard, intake, tracker, profile, memory, detail, analysis, resume, notes, version, empty, warning, and confirmation states use shared content roles.
- Shared page rails and panel geometry remain consistent while workflow density is preserved.
- Before/proposed comparisons stack before either side becomes cramped.
- Major workflow states use complete semantic triplets.
- Forms and actions reflow without horizontal page scrolling.
- Authentication and private state remain product-owned.

## 11. Motion

Motion is restrained and functional:

- Reveal motion MAY clarify entry into a page.
- Loading motion MUST include written status.
- Menus, drawers, and dialogs MAY animate within the shared motion scale.
- Reduced-motion users receive no nonessential movement.
- Animation MUST NOT delay access to controls or content.

## 12. Privacy and external services

- Shared assets are packaged locally; owned sites MUST NOT fetch the design system from a runtime CDN.
- Runtime third parties are disclosed at the point of use.
- Results and private workflow data are not added to unrelated analytics or advertising systems.
- Private RolePacket implementation details do not belong in this public design-system repository.

## 13. Performance

Performance limits remain pending measured production baselines. Until then:

- Shared CSS MUST remain dependency-free.
- Product bundles MUST avoid duplicate copies of shared assets.
- Static pages SHOULD avoid JavaScript for content that can be present in source HTML.
- Page-load budgets remain separate from user-initiated diagnostic transfer budgets.
- New visual dependencies require a measured reason and ownership record.

## 14. Governance

A shared change includes:

- Atomic tokens
- Global accessibility behavior
- Global header and Sites control
- Page rails and shared content primitives
- Shared semantic status roles
- Shared responsive transformations

A product-local change includes:

- Portfolio composition unique to a project narrative
- Network measurement logic, charts, and probe behavior
- RolePacket authentication, application state, and workflow logic

Shared changes require:

1. Design-system update
2. Version bump under semantic versioning
3. Specimen or contract update
4. Package validation
5. Consumer pin update
6. Product-level tests
7. Manual production review when visual behavior changes

### Exceptions

No exceptions are approved for version 1.4.0. Future exceptions MUST record the rule, repository/component, rationale, owner, review date, removal issue, and accessibility impact.

### Conformance checklist

- Uses current shared package version and immutable source
- Uses exact dot canvas without a second grid
- Uses shared header on every route
- Uses shared content roles on every page and application state
- Preserves product-specific information architecture
- No raw shared colors or duplicate token values in product adapters
- No hidden essential navigation at compact widths
- No document-level overflow at 320px
- Usable at 200% zoom
- Keyboard, focus, reduced motion, and forced colors verified
- Semantic status includes text, surface, and border where applicable
- Tables, code, and media remain locally bounded
- Every empty and error state explains recovery
- Every external or third-party interaction is disclosed
