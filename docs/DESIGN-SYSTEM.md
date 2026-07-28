# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.4.0  
**Package status:** Implementation candidate  
**Production visual baseline:** Approved  
**Owner:** Johnny Li

- **MUST** means required for conformance.
- **SHOULD** means expected unless a documented exception exists.
- **MAY** means optional.
- **CURRENT** describes the approved production behavior.
- **REFERENCE** describes a reusable pattern that products may adopt without being forced to replace stable UI.

The current production interfaces at `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev` are the visual baseline. Future shared work should reduce drift without redesigning those products merely to match the specimen or use identical markup.

## 2. Design intent

> **Editorial warmth, systems precision.**

The sites MUST feel related without becoming identical:

- **Portfolio:** editorial, open, spacious, and narrative.
- **Network Diagnostics:** analytical, measurement-oriented, and data-dense where useful.
- **RolePacket:** compact, workflow-oriented, and optimized for review and state management.

The specimen demonstrates the shared language. It is not a replacement theme for the production sites.

## 3. Ownership boundary

### Shared and required

The design system owns:

- Atomic color, typography, spacing, radius, motion, elevation, and layout tokens
- Warm off-white canvas and exact faint dot texture
- Global focus, selection, reduced-motion, and forced-colors behavior
- Shared global-header geometry and identity lockup
- Sites control and menu styling
- Semantic success, warning, danger, and information token roles
- Cross-site navigation expectations
- Responsive and accessibility principles

### Product-owned

Each product owns:

- Information architecture and page composition
- Product navigation behavior
- Portfolio case-study layouts and editorial rhythm
- Network test controls, measurements, charts, tables, and report states
- RolePacket sidebar, workflow density, forms, review states, authentication, and application behavior
- Product-specific component names and implementation structure

Products MAY use shared content classes from `styles/content.css` and `styles/content-guard.css`. Existing stable product markup is also conforming when it maps to the same shared tokens, accessibility behavior, semantic roles, and responsive outcomes.

A migration MUST NOT be justified solely by replacing a product class with a `jl-*` class when the rendered result and behavior are already correct.

## 4. Principles

1. Preserve the approved production UI before pursuing code-level consolidation.
2. Share foundations and interaction contracts, not product identity.
3. Use one accessible terracotta accent; reserve other hues for semantic or analytical meaning.
4. Make state, evidence, scope, and recovery explicit.
5. Prefer responsive reflow over clipping, shrinking, or hiding essential navigation.
6. Keep runtime dependencies and third-party data sharing minimal.
7. Product adapters MUST NOT redefine the shared global-header or Sites-control geometry.
8. Content MUST remain understandable without color, animation, hover, or a wide viewport.
9. Shared changes that alter production appearance require manual comparison across all three sites.

## 5. Atomic tokens

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
- Semantic success, warning, danger, information, and violet triplets: text, surface, and border

Raw shared colors MUST NOT appear in shared CSS. Product chart colors MAY remain product-owned when they have stable labels and grayscale meaning.

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
- RolePacket sidebar reference: 238px wide at desktop

### Controls, radii, motion, and elevation

- Small, medium, and large control heights: 36px, 44px, and 52px
- Radius scale: 8px, 12px, 18px, 24px, pill
- Motion scale: 160ms, 240ms, 420ms
- Shared ease-out curve
- Low and high warm-neutral shadows
- Reduced motion removes nonessential transitions and smooth scrolling

## 6. Canvas and surfaces

The default body canvas MUST use the exact shared dot texture over the canvas token. Products MUST NOT layer a visible grid over that texture.

Surfaces are selected by information need:

- Canvas: broad page and workflow background
- Surface: panels, controls, tables, and cards
- Surface muted: supporting content and grouped detail
- Surface strong: selected or strongly grouped content
- Inverse surface: restrained dark sections and code or terminal contexts

The portfolio MAY remain predominantly open and borderless. Network Diagnostics and RolePacket MAY use more panels, rules, and dense grouping. This difference is intentional.

## 7. Accessibility contract

### Focus

Every interactive element MUST expose the shared dual focus treatment:

- 2px focus ring
- 3px offset
- 5px contrasting gap
- Appropriate light, dark, or accent gap color

Focus MUST remain visible in forced-colors mode.

### Keyboard and interaction

- Navigation, menus, drawers, dialogs, details, forms, and actions MUST be keyboard operable.
- Escape closes menus, drawers, and dialogs where expected and restores focus to the trigger.
- Modal and off-canvas interactions MUST contain focus while open.
- Closed off-canvas navigation MUST be inert or removed from the tab order.
- Hover-only disclosure is prohibited for essential content.

### Semantics

- Every page or application state has one primary heading.
- Sections use ordered heading levels.
- Tables use header cells and remain inside explicit responsive regions.
- Status includes text; color or icons alone are insufficient.
- Errors include a written reason and recovery action.
- Important success remains persistent rather than toast-only.
- Media requires useful alternative text or a caption when it adds meaning.

### Responsive and zoom

- Two-column heroes become one column before either side becomes cramped.
- Four-column metric grids become two, then one.
- Multi-column forms become one before labels or errors become cramped.
- Sidebars become an accessible drawer or equivalent compact navigation.
- Before/proposed comparisons stack vertically.
- Genuine tables MAY scroll inside a labeled region.
- Action groups stack to full-width controls when needed.
- No page may have document-level overflow at 320px.
- Pages MUST remain usable at 200% browser zoom.

## 8. Shared global header

Every owned website page MUST render the shared `jl-global-header` visual and interaction contract.

Canonical identity labels:

- `Johnny Li / Portfolio`
- `Johnny Li / Network Diagnostics`
- `Johnny Li / RolePacket`

Desktop behavior:

- 82px minimum height
- Shared 1328px inner rail and responsive gutters
- Owner/product identity in the first column
- Optional product navigation in the middle column
- Sites control in the final column
- Exact 88×44px Sites control with 13px/700 UI typography and a CSS-drawn chevron

Compact behavior:

- 68px minimum height
- Owner and separator may hide while the product identity remains
- Sites control remains 88×40px
- Product navigation that no longer fits remains reachable through a product-owned compact pattern

Every owned site MUST reach the other two within two interactions. Owned-site links open in the same tab. External destinations MAY open in a new tab.

Products MAY retain different implementation strategies, including static markup or a product component, provided the rendered contract and behavior remain equivalent.

## 9. Shared content references

`styles/content.css` and `styles/content-guard.css` provide reusable reference classes for new work and deliberate consolidation:

- Page rails and responsive regions
- Heroes, titles, ledes, actions, and metadata
- Sections and content grids
- Prose and editorial leads
- Panels and ruled structures
- Process steps and metrics
- Semantic callouts
- Buttons and action groups
- Code, media, tables, and empty states

These classes are REFERENCE utilities, not a requirement to rewrite stable production markup. Product-local classes are conforming when they:

- Use shared token roles rather than duplicate values
- Preserve the approved production composition
- Meet the same accessibility and responsive outcomes
- Avoid overriding shared header ownership
- Keep semantic state understandable without color

## 10. Approved product baselines

### Portfolio

Preserve:

- Current homepage composition and section rhythm
- Editorial display hierarchy
- Numbered selected-work rows
- Narrative case-study structure
- Restrained terracotta use
- Dark contact and next-project sections
- Current responsive navigation and contact availability

The case studies may continue using their current rendered shared-header enhancement until source-level markup cleanup is deliberately scheduled. That cleanup is technical debt, not a reason to restyle the pages.

### Network Diagnostics

Preserve:

- Current hero and sticky test-control composition
- Quick, Full, and Stress profile selector
- Explicit duration and maximum-transfer disclosure
- Separate idle, download-loaded, and upload-loaded conditions
- Current metric cards, charts, findings, tables, and recent-history layout
- Optional native deep probe
- Local-only result history
- Current terracotta text hierarchy with product-owned analytical chart colors
- Exact dot canvas without the legacy visible grid

Browser request loss MUST NOT be labeled raw packet loss. Charts retain stable labels, summaries, and grayscale distinction.

### RolePacket

Preserve:

- Current dense review-first workflow
- Wide sidebar and accessible compact drawer
- Ruled application rows
- Explicit status and provenance
- Before/proposed comparisons
- Resume preview, version history, answer matching, notes, and memory workflows
- Existing panel density and form structure

RolePacket feature development MAY substantially change workflow behavior. UI changes should remain incremental and should not force the portfolio or Network Diagnostics to adopt workflow-specific patterns.

## 11. Component state requirements

Every interactive product component defines the states that apply to it:

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

## 12. Motion, privacy, and performance

Motion is restrained and functional:

- Reveal motion MAY clarify entry into a page.
- Loading motion MUST include written status.
- Menus, drawers, and dialogs MAY animate within the shared scale.
- Reduced-motion users receive no nonessential movement.
- Animation MUST NOT delay access to controls or content.

Privacy and external services:

- Shared assets are packaged locally; owned sites MUST NOT fetch the design system from a runtime CDN.
- Runtime third parties are disclosed at the point of use.
- Results and private workflow data are not added to unrelated analytics or advertising systems.
- Private RolePacket implementation details do not belong in this public repository.

Performance:

- Shared CSS remains dependency-free.
- Product bundles avoid duplicate shared assets.
- Static pages SHOULD avoid JavaScript for content that can be present in source HTML.
- Page-load budgets remain separate from user-initiated diagnostic transfer budgets.
- New visual dependencies require a measured reason and ownership record.

## 13. Governance

A shared change includes:

- Atomic tokens
- Global accessibility behavior
- Global header and Sites control
- Shared semantic status roles
- Shared responsive principles
- Optional reusable content utilities

A product-local change includes:

- Portfolio composition unique to a project narrative
- Network measurement logic, charts, controls, and probe behavior
- RolePacket authentication, application state, and workflow logic
- Product-specific spacing or density that preserves shared roles

Shared visual changes require:

1. Design-system update
2. Version decision under semantic versioning
3. Specimen or contract update
4. Package validation
5. Consumer pin update when distributable assets changed
6. Product-level tests
7. Manual production comparison across all three sites

Documentation-only changes do not require consumer repinning when packaged assets are unchanged.

### Exceptions

Exceptions record the rule, repository or component, rationale, owner, review date, removal issue, and accessibility impact.

### Conformance checklist

- Uses the current reviewed shared-asset source
- Preserves the approved production appearance unless a visual change is intentional
- Uses the exact dot canvas without a second grid
- Renders the shared header contract on every route or state
- Uses shared tokens or documented product aliases rather than duplicate shared values
- Preserves product-specific information architecture
- Does not hide essential navigation at compact widths
- Has no document-level overflow at 320px
- Remains usable at 200% zoom
- Supports keyboard, focus, reduced motion, and forced colors
- Communicates semantic status with text and appropriate token roles
- Keeps tables, code, charts, and media locally bounded
- Gives every empty and error state a recovery path
- Discloses every external or third-party interaction
