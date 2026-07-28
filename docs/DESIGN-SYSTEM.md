# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.5.0  
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

- Atomic color, typography, spacing, radius, control, motion, elevation, and layout tokens
- Warm off-white canvas and exact faint dot texture
- Global focus, selection, reduced-motion, and forced-colors behavior
- Global-header geometry and owner/product identity lockup
- Canonical owned-site registry
- Sites-control styling and interaction behavior
- Compact header-menu toggle and popover shell
- Semantic success, warning, danger, information, and violet token triplets
- Cross-site navigation and accessibility contracts
- Responsive principles

### Product-owned

Each product owns:

- Information architecture and page composition
- Product navigation labels and destinations
- Portfolio editorial rhythm and case-study composition
- Network test controls, measurement logic, charts, tables, reports, and probe behavior
- RolePacket sidebar, forms, workflow density, authentication, review logic, and application behavior
- Product-specific component names and implementation structure

Products MAY use shared content classes from `styles/content.css` and `styles/content-guard.css`. Existing stable markup is conforming when it maps to the same tokens, accessibility behavior, semantic roles, and responsive outcomes.

A migration MUST NOT be justified solely by replacing a product class with a `jl-*` class when the rendered result and behavior are already correct.

## 4. Principles

1. Preserve the approved production UI before pursuing code-level consolidation.
2. Share foundations and interaction contracts, not product identity.
3. Use one accessible terracotta accent; reserve other hues for semantic or analytical meaning.
4. Make state, evidence, scope, and recovery explicit.
5. Prefer responsive reflow over clipping, shrinking, or hiding essential navigation.
6. Keep runtime dependencies and third-party data sharing minimal.
7. Product adapters MUST NOT redefine shared header, Sites-control, or compact-menu geometry.
8. Content remains understandable without color, animation, hover, or a wide viewport.
9. Shared appearance changes require comparison across all three products.

## 5. Atomic tokens

The editable source is `tokens/tokens.tokens.json`. Generated CSS is not edited manually.

### Color roles

- `canvas` and `canvasDot`: page background and exact dot texture
- `surface`, `surfaceMuted`, `surfaceStrong`, `surfaceInverse`: grouped content surfaces
- `ink`, `text`, `muted`: primary, body, and secondary text
- `accent`, `accentHover`, `accentActive`, `accentDecorative`, `accentSoft`, `onAccent`: terracotta emphasis and interaction roles
- Success, warning, danger, information, and violet: complete text, surface, and border triplets

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

`OWNED_SITES` is the source of truth for:

- Stable site IDs
- Display labels
- Canonical production URLs

Consumers SHOULD render the registry directly where their build system permits. Static fallback markup MUST remain consistent with it.

### Sites-menu controller

`installSiteSwitcher()` owns:

- Button click toggle
- Outside-pointer close
- Escape close with focus restoration
- ArrowDown and ArrowUp entry
- ArrowUp and ArrowDown cycling
- Home and End navigation
- Link-selection close
- `aria-expanded` and `hidden` synchronization

Products MAY close their own compact navigation or workspace drawer before the Sites menu opens.

### Compact header-menu controller

`installHeaderMenu()` owns the same disclosure and keyboard contract for compact product navigation. Product labels, destinations, and active-state logic remain local.

### Shared compact menu shell

- `jl-header-menu-toggle`: compact navigation trigger
- `jl-header-menu`: product navigation popover shell
- `jl-header-menu--open`: visible compact state

At 900px and below, the shell uses shared gutters, surface, border, radius, shadow, row height, hover treatment, and forced-colors border behavior. At wider widths, product navigation returns to the normal header slot.

## 9. Shared content references

`styles/content.css` and `styles/content-guard.css` provide REFERENCE utilities for new work and deliberate consolidation:

- Page rails and responsive regions
- Heroes, titles, ledes, actions, and metadata
- Sections and content grids
- Prose and editorial leads
- Panels and ruled structures
- Process steps and metrics
- Semantic callouts
- Buttons and action groups
- Code, media, tables, and empty states

Product-local classes are conforming when they:

- Use shared token roles rather than duplicate values
- Preserve the approved composition
- Meet the same accessibility and responsive outcomes
- Avoid overriding shared ownership
- Keep semantic state understandable without color

## 10. Approved product baselines

### Portfolio

Preserve:

- Homepage composition and section rhythm
- Editorial display hierarchy
- Numbered selected-work rows
- Narrative case studies
- Restrained terracotta use
- Dark contact and next-project sections
- Responsive navigation and contact availability

Case-study headers SHOULD exist in source HTML rather than being constructed by runtime enhancement. Technical cleanup MUST preserve the rendered design.

### Network Diagnostics

Preserve:

- Hero and sticky test-control composition
- Quick, Full, and Stress profiles with duration and maximum-transfer disclosure
- Idle, download-loaded, and upload-loaded conditions
- Metric cards, charts, findings, tables, recent history, and native probe
- Local-only result history
- Terracotta text hierarchy with product-owned analytical colors
- Exact dot canvas without a visible grid

Browser request loss MUST NOT be labeled raw packet loss. Charts retain stable labels, summaries, and grayscale distinction.

### RolePacket

Preserve:

- Dense review-first workflow
- Wide sidebar and accessible compact drawer
- Ruled application rows
- Explicit status and provenance
- Before/proposed comparisons
- Resume preview, version history, answer matching, notes, and memory workflows
- Current panel density and form structure

RolePacket feature work MAY substantially change workflow behavior. It MUST NOT force workflow-specific patterns onto the portfolio or Network Diagnostics.

## 11. Component states and responsive behavior

Every interactive product component defines the states that apply:

- Default
- Hover
- Focus-visible
- Disabled
- Loading or pending
- Empty
- Error with recovery
- Success when important
- Compact transformation
- Forced-colors behavior
- Reduced-motion behavior

Responsive requirements:

- Two-column heroes become one before either side becomes cramped.
- Four-column metrics become two, then one.
- Multi-column forms become one before labels or errors become cramped.
- Sidebars become accessible drawers or equivalent navigation.
- Before/proposed comparisons stack vertically.
- Genuine tables MAY scroll inside labeled regions.
- Action groups stack to full-width controls when needed.
- No document-level overflow at 320px.
- Pages remain usable at 200% browser zoom.

## 12. Motion, privacy, and performance

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

## 13. Governance

A shared change includes:

- Atomic tokens
- Global accessibility behavior
- Global header and site controls
- Canonical owned-site registry
- Shared semantic status roles
- Shared responsive principles
- Optional reusable content utilities

A product-local change includes:

- Portfolio narrative composition
- Network measurement logic, charts, controls, and probe behavior
- RolePacket authentication, application state, and workflow logic
- Product-specific spacing or density that preserves shared roles

Shared distributable changes require:

1. Design-system update
2. Semantic-version decision
3. Specimen or contract update
4. Package validation
5. Consumer pin update
6. Product-level tests
7. Manual production comparison when appearance changes

Documentation-only changes do not require repinning when packaged assets are unchanged.

### Conformance checklist

- Uses the current reviewed shared-asset source
- Preserves approved appearance unless change is intentional
- Uses the exact dot canvas without a second grid
- Renders the shared header on every route or state
- Uses the canonical site directory and shared interaction contract
- Uses shared compact-menu geometry where applicable
- Uses shared tokens or documented product aliases
- Preserves product-specific information architecture
- Does not hide essential compact navigation
- Has no document-level overflow at 320px
- Remains usable at 200% zoom
- Supports keyboard, focus, reduced motion, and forced colors
- Communicates semantic status with text and appropriate token roles
- Keeps tables, code, charts, and media locally bounded
- Gives every empty and error state a recovery path
- Discloses every external or third-party interaction
