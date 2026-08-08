# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.9.0  
**Documentation revision:** 2026-08-08  
**Package status:** Approved  
**Production visual baseline:** Approved  
**Owner:** Johnny Li

- **MUST** means required for conformance.
- **SHOULD** means expected unless a documented exception exists.
- **MAY** means optional.
- **CURRENT** describes approved production behavior.
- **REFERENCE** describes a reusable pattern that does not require replacing stable UI.

The production interfaces at `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev` are the visual baseline. Shared work reduces foundational, behavioral, accessibility, and maintenance drift without making the products identical.

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

- Atomic color, typography, spacing, radius, control, motion, elevation, icon, z-index, layout, and light/dark theme tokens
- Warm off-white canvas and exact faint dot texture
- Global focus, selection, reduced-motion, and forced-colors behavior
- Global-header geometry and owner/product identity lockup
- Canonical owned-site registry and Sites-control interaction contract
- Adjacent Settings appearance control and shared System, Light, and Dark preference behavior
- Unified Sites and Settings attached-disclosure shells, open-state pinning, and dismissal behavior
- Compact and extreme-compact header-menu structure
- Semantic status roles and shared content primitives
- Native-dialog structural shell
- Consumer release resolver and reusable synchronization workflow
- Machine-readable conformance contract, schemas, runner, report format, and candidate gate
- Shared responsive and accessibility principles

### Product-owned and local

Each consumer owns:

- Product information architecture, density, copy, content, and visual composition
- Product state, workflows, persistence, APIs, authentication, storage, and deployment
- Network measurements, profiles, charts, reports, Worker logic, and native probe
- RolePacket application lifecycle, resume logic, extension integration, and workspace drawer
- Portfolio narrative structure, case-study content, and editorial motion
- Product-specific validation commands, fixtures, schedules, and rollback boundaries

A shared abstraction MUST NOT absorb product logic merely because two products currently use similar markup.

## 4. Tokens and canvas

`tokens/tokens.tokens.json` is the only editable atomic-token source. `tokens/tokens.css` is generated and MUST match the package version.

Consumers MUST use shared tokens directly or through documented product aliases. Shared package CSS MUST NOT introduce raw color values outside generated token definitions.

Accent roles are distinct:

- `--jl-color-accent` is the primary readable terracotta for prominent emphasis, primary-action fills, and strong edges. It is valid on light surfaces and for selected high-emphasis text on inverse surfaces when the resulting contrast is sufficient.
- `--jl-color-accent-decorative` is for compact labels, markers, metadata, and low-opacity decorative mixtures.
- `--jl-color-accent-soft` is the secondary terracotta for lower-emphasis text, arrows, underlines, and restrained borders on inverse surfaces.

Consumers MAY define product aliases for these roles, but MUST preserve their semantic distinction. A prominent phrase on an inverse surface MAY use the primary accent while surrounding headline text remains the inverse text color and secondary details use the soft accent. Decorative or soft accents MUST NOT replace the primary accent for prominent emphasis merely because the hues are similar.

The primary accent, hover, active, and decorative terracotta roles use the same approved color family in Light and Dark. Dark mode changes the neutral surfaces, text hierarchy, semantic colors, selection, focus, and soft-accent roles rather than substituting a brighter independent primary accent palette.

The canvas uses:

- `--jl-color-canvas` as the base
- `--jl-color-canvas-dot` for the exact faint dot field
- No second visible grid or competing background texture

Product visualizations MAY use product-owned analytical colors when color meaning remains accessible without color alone.

### Theme modes

Every owned site MUST support `System`, `Light`, and `Dark` through the shared theme contract. The pre-paint bootstrap resolves the stored preference before styles render, writes `data-theme-preference` and the resolved `data-theme` to the root element, follows operating-system changes while set to System, and preserves the preference across `*.johnnyli.dev`.

Appearance preferences are owned by the adjacent Settings disclosure, not by the Sites directory. Settings uses the shared icon-only System, Light, and Dark selector and the shared controller/theme-control stylesheet. The selected preference is communicated through the terracotta selection rail plus accessible pressed state and labels. Consumers MUST NOT introduce a separate product theme toggle.

Theme values change through semantic tokens; products MUST NOT maintain independent light and dark component implementations. Print and PDF output MUST resolve to the light paper theme. Forced-colors behavior remains independent of the selected theme.

## 5. Typography and layout

The system provides:

- A user-interface sans-serif stack
- An editorial serif stack
- A monospace stack for code and diagnostic evidence
- Shared display, page-title, section, card-title, body, metadata, and eyebrow roles
- Shared content rails, gutters, section rhythm, panel padding, and reading width

Products MAY preserve distinct typography scale, density, and composition through token-derived aliases and component variables.

## 6. Foundations and accessibility

Every product MUST preserve:

- One visible focus indication that works on light and dark surfaces
- Keyboard reachability for essential controls
- Written labels for meaningful state
- Reduced-motion behavior for nonessential movement
- Forced-colors boundaries for interactive and semantic regions
- Sufficient text and semantic-border contrast
- Accessible names and descriptions for menus, drawers, dialogs, forms, and stateful controls
- Recovery actions for meaningful errors
- Focus restoration after dismissing menus, drawers, and dialogs

State MUST NOT rely on color alone. Use text, labels, shape, marks, or position in addition to color.

Automation MUST distinguish real browser behavior from approximations. A narrow viewport is not evidence of actual browser zoom.

## 7. Shared global header

Every route or application state MUST render the shared global-header contract:

1. Owner/product identity
2. Optional contextual navigation
3. Sites disclosure
4. Adjacent Settings disclosure

The shared header owns:

- 82px desktop inner-row height and 68px compact inner-row height
- A 1px divider, producing an 83px desktop and 69px compact reserved footprint while disclosures are pinned or dismissing
- Shared inner rail and gutters
- Owner/product typography and muted product treatment
- 104px Sites-control width through normal desktop and compact layouts
- 96px Sites-control width at the 360px-and-below extreme-compact transformation
- 44px desktop and 40px compact Settings-control width and height
- 44px desktop and 40px compact Sites-control height
- UI-font, weight, radius, border, centered menu labels, CSS-drawn Sites chevron, and Settings gear treatment
- Sticky placement, border, surface, menu layering, and forced-colors border treatment
- Unified expanding Sites and Settings shells whose content grows below the trigger instead of replacing or overlaying it
- Content-driven disclosure height and downward clip reveal so open-state transitions do not flash between rounded and squared trigger geometry
- Sites/Settings mutual exclusion and shared keyboard, focus, outside-click, and dismissal behavior
- Complete-header viewport pinning while either disclosure is open so the identity, navigation, controls, background, and divider remain one visual unit while scrolling
- Preservation of the header's normal document footprint while pinned so disclosure state changes do not move page content
- A 400ms complete-header dismissal animation using the approved easing after a scrolled disclosure closes, with nonessential motion removed under `prefers-reduced-motion`

At 900px and below, applicable product navigation becomes the shared compact menu shell. At 560px and below, the owner and separator MAY hide while the product identity remains. At 420px and below, gutters and inter-control gaps tighten. At 360px and below, gutters, gaps, identity size, Menu-trigger width, and the Sites width reduce so the product identity, Menu trigger where applicable, Sites control, and Settings control remain contained at 320px.

Required navigation or appearance preferences MUST NOT be hidden as an overflow workaround.

## 8. Shared site controls

`OWNED_SITES` is the canonical directory for Portfolio, Network Diagnostics, and RolePacket. The Sites disclosure contains only those destinations; appearance preferences belong to Settings.

The shared framework-neutral controllers own:

- Sites and Settings control creation or normalization where the consumer markup does not already provide them
- Open and close state synchronization
- Sites/Settings mutual exclusion
- Outside-click dismissal
- Escape dismissal and focus restoration
- ArrowUp and ArrowDown navigation
- Home and End navigation
- Focus entry when opened from the keyboard
- Theme-button pressed-state synchronization
- System-preference tracking and shared theme-change handling
- Complete-header disclosure-exit coordination after close
- Compact-menu closing at the desktop breakpoint
- Coordination between Sites, Settings, and product navigation menus

Consumers own their framework adapter and local state integration, but MUST NOT reimplement the shared keyboard, dismissal, theme-preference, or Sites/Settings coordination contract.

Owned-site links remain same-tab navigation and every site reaches the other two within two interactions.

## 9. Shared content references and primitives

The complete content layer is a REFERENCE for new work and deliberate consolidation. Stable product markup remains conforming when it preserves the same token, semantic, accessibility, and responsive outcomes.

The standalone primitive layer provides adaptable shells for:

- Action groups
- Buttons and compact or danger variants
- Semantic callouts
- Empty states
- Scrollable table regions
- Native-dialog structure

Consumers customize documented `--jl-*` component variables instead of copying complete shared structural declarations.

After a primitive is adopted and validated, equivalent product fallback structure MUST be removed. Product spacing, dimensions, animation, copy, state, and behavior MAY remain local.

### Native dialog contract

Matching native confirmation dialogs use:

- `.jl-dialog`
- `.jl-dialog__surface`
- `.jl-dialog__title`
- `.jl-dialog__message`
- `.jl-dialog__actions`
- Shared button shells where applicable

The shared layer owns centering or compact placement hooks, viewport containment, backdrop, surface, title, message, actions, and forced-colors structure.

Products retain:

- Dialog dimensions and density
- Copy and tone
- Destructive or default action selection
- Queueing and application state
- Animation
- Cancellation behavior
- Focus timing and product events

## 10. Consumer distribution and synchronization

Consumers MUST pin an immutable reviewed source commit in `design-system.lock.json` and synchronize shared assets into their repository or generated artifact. Runtime content-delivery-network loading is not allowed.

A consumer integration check MUST derive the expected package version and source commit from its lock, then verify:

- Package identity and semantic version
- Immutable 40-character source commit
- Generated version metadata
- Generated source record
- Package dependency where applicable
- Locally copied helpers and contract files
- Required CSS or JavaScript imports
- Product-specific ownership and fallback-removal rules

Consumer validators MUST NOT hard-code the previous package release because doing so prevents the scheduled updater from validating a new candidate.

### Reusable update workflow

The shared release resolver may update only repository-local design-system metadata and an explicitly supplied package manifest. It MUST reject path traversal, invalid commit identifiers, and invalid semantic versions. It MUST NOT execute consumer commands.

The reusable synchronization workflow owns:

- Checkout and Node setup
- Release resolution
- Consumer synchronization invocation
- Consumer-owned validation invocation
- Tracked-path change detection
- Update branch publication
- Draft pull-request creation or refresh

Consumers retain:

- Schedule and manual-dispatch configuration
- Node version
- Install command
- Validation command
- Tracked paths
- Independent pull request and rollback boundary

Reusable workflow references MUST use immutable commit identifiers rather than floating branches.

## 11. Product-specific contracts

### Portfolio

Preserve editorial composition, spacing, terracotta hierarchy, source-authored homepage and case-study emphasis, narrative sections, evidence, limitations, actions, next-project navigation, and the inverse contact section. The portfolio uses the shared header, Sites/Settings controllers, compact product menu, shared appearance contract, and selected action/button primitives. It has no matching native confirmation dialog and therefore does not adopt the shared dialog shell.

#### Portfolio case-study contract

The approved case-study pages use an open editorial composition rather than a card dashboard.

**Hero composition**

- The hero uses the light canvas with a token-derived warm radial light.
- The radial light MUST remain inside the hero and reach transparency before the content or viewport edge. A visible vertical clipping seam is not conforming.
- The eyebrow, title, summary, and actions SHOULD begin without a large dead zone below the global header.
- The title and summary use the twelve-column editorial grid and MUST stack before either side becomes cramped.
- The project-facts row retains a top rule, four equal columns on desktop, and centered label/value alignment within each column. Its vertical placement remains deliberately offset rather than mechanically centered, while the band stays compact.
- Hero actions remain content-width and use the shared action/button primitive. The approved desktop expression uses the large 52px control height, 20px inline padding, a 10px label/icon gap, 0.95rem semibold text, and a restrained 6px radius.
- The primary hero action uses `--jl-color-accent` with the on-accent text role. The secondary action uses the standard light-surface rule role and remains visually subordinate.

**Terracotta cadence and hierarchy**

- `--jl-color-accent` or its documented portfolio alias is used for readable emphasis on light surfaces and selected high-emphasis phrases on inverse surfaces.
- `--jl-color-accent-decorative` or its alias is used for small section numbers, process markers, decision markers, metric labels, and low-opacity decorative mixtures.
- `--jl-color-accent-soft` or its alias is used for secondary inverse-surface details such as small labels, arrows, underlines, and restrained link borders.
- Large narrative leads remain ink by default. Terracotta emphasis is source-authored around selected clauses or phrases only; entire lead or body sentences MUST NOT be colored as a shortcut.
- Normal scrolling SHOULD retain a meaningful terracotta cadence through selective lead emphasis, metric labels, output accents, or inverse-section emphasis rather than relying only on tiny section numbers.
- Metric values remain ink. Their compact uppercase labels use the decorative terracotta role and a bold weight.
- Dark code or evidence panels MAY use a subtle token-derived terracotta wash and a primary-accent edge. Raw color copies are not conforming.

**Open editorial groups**

- Process stages use an open four-column row on wide screens. The outer perimeter is omitted and only internal dividers remain.
- Process stages become two columns and then one column before content becomes cramped; stacked layouts use horizontal separators.
- Engineering decisions use an open two-by-two editorial grid with the center divider and the divider between rows. A complete outer box is omitted.
- Validation uses a compact twelve-column composition with the metric group on the left and explanatory evidence alongside it on the right. It stacks at the product breakpoint before either side becomes cramped.
- Metric groups omit top and bottom perimeter rules in the approved case-study expression and retain only the internal dividers needed to explain grouping.
- Process stages, engineering decisions, and metric groups are noninteractive. They MUST NOT receive hover backgrounds, elevation, translation, pointer cursors, or other affordances that imply activation.
- Spacing within these groups SHOULD keep labels, headings, values, and descriptions visually connected and avoid tall empty cells or floating divider lines.

#### Portfolio inverse-section contract

Inverse narrative sections retain cream or the inverse text token as the dominant readable color. Primary terracotta marks one semantically meaningful phrase or action; soft terracotta supports secondary details. Coloring the full display title with terracotta, or dividing it between two similar terracotta shades, SHOULD be avoided when it flattens the hierarchy.

**Next project**

- The non-emphasized headline clause remains cream.
- The source-authored editorial phrase uses the primary terracotta.
- The small `Next project` label and the link arrow or underline use the soft terracotta.
- The link text remains cream.
- This composition is shared by all portfolio case-study pages through the product-owned case-study stylesheet.

**Homepage contact**

- The editorial `Let’s` remains cream.
- The action word `talk.` uses the primary terracotta because it carries the semantic emphasis.
- The contact paragraph and link text remain cream.
- The section number and link arrows use the primary terracotta; contact-link rules use the soft terracotta.
- Footer metadata remains muted cream and does not compete with the contact action.

### Network Diagnostics

Preserve hero and sticky test controls; Quick, Full, and Stress profiles with duration and maximum-transfer disclosure; idle and loaded conditions; metric cards, charts, findings, tables, recent history, and native probe; local-only result history; terracotta hierarchy with product-owned analytical colors; and the exact dot canvas without a visible grid.

Browser request loss MUST NOT be labeled raw packet loss. Charts retain stable labels, summaries, and grayscale distinction.

The data-use confirmation dialog uses the shared dialog shell. Transfer-cap logic, remembered consent, checkbox content, wording, and test behavior remain product-owned.

### RolePacket

Preserve the dense review-first workflow, wide sidebar and accessible compact drawer, ruled application rows, explicit status and provenance, before/proposed comparisons, resume preview, version history, answer matching, notes, memory workflows, and current panel density and form structure.

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
- The shared identity, required Menu trigger where applicable, Sites control, and Settings control remain available at the supported 320px viewport.
- No document-level overflow occurs at 320px.
- Pages remain usable at actual 200 percent browser zoom.

Automated suites SHOULD include desktop, narrow-desktop, mobile, and 320px minimum viewports. Only actual browser zoom receives the browser-zoom label.

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
- Update and conformance automation MUST NOT weaken consumer validation or bypass repository protections.
- Bundle and user-experience performance baselines are recorded and manually reviewed by each consumer. Automation MUST NOT invent new blocking thresholds without repeated same-environment evidence and an explicit tolerance decision.

## 14. Governance

A shared change includes atomic tokens, global accessibility behavior, global header and site controls, canonical site registry, shared semantic roles, shared primitive and dialog structure, consumer release and synchronization tooling, conformance contract, schemas and runner, shared responsive principles, candidate-gate behavior, and optional reusable content utilities.

A product-local change includes portfolio narrative composition; Network measurement logic, charts, controls, profiles, Worker and probe behavior; RolePacket authentication, application state, workflow logic, APIs, storage, extension behavior, and workspace drawer; product-specific spacing, density, animation, copy, or color expression; consumer state fixtures; and consumer validation commands and schedules.

Shared distributable changes require:

1. Design-system update
2. Semantic-version decision
3. Canonical documentation, specimen, or contract update
4. Atomic package, token, contract, and version metadata
5. Package validation and conformance-runner self-test
6. Cross-consumer candidate-gate validation against all three default branches
7. Visual comparison when appearance changes
8. Reviewed merge only after shared and consumer gates pass
9. Independent consumer pull requests and rollback boundaries
10. Product-level static, runtime, visual, and application tests
11. Recorded manual approval for checks that cannot be automated honestly

Documentation-only changes do not require repinning when packaged assets are unchanged.

### Conformance checklist

- Uses the current reviewed shared-asset source
- Preserves approved appearance unless change is intentional
- Uses the exact dot canvas without a second grid
- Renders the shared header on every route or state
- Uses the canonical site directory and shared Sites/Settings interaction contract
- Keeps appearance preferences in the adjacent shared Settings disclosure rather than the Sites directory or a product-local toggle
- Uses shared compact-menu geometry where applicable
- Preserves the required product identity, Menu trigger where applicable, Sites control, and Settings control at 320px
- Uses the shared complete-header pinned state without shifting page content when Sites or Settings is open
- Uses shared tokens or documented product aliases
- Uses standalone primitives where adopted and removes equivalent structural fallbacks
- Uses the shared dialog shell for matching native confirmation dialogs
- Keeps product dialog logic, wording, state, and focus behavior local
- Pins shared workflows and generated assets to immutable commits
- Derives expected asset provenance from the consumer lock
- Keeps consumer schedules, state fixtures, and validation commands product-owned
- Provides schema-valid evidence for every applicable machine-readable rule
- Includes source and consumer commit provenance in reports
- Distinguishes automated narrow-layout evidence from actual browser-zoom review
- Preserves product-specific information architecture
- Does not hide essential compact navigation or appearance preferences
- Has no document-level overflow at 320px
- Remains usable at actual 200 percent zoom
- Supports keyboard, focus, reduced motion, and forced colors
- Communicates semantic status with text and appropriate token roles
- Keeps tables, code, charts, dialogs, and media locally bounded
- Gives every empty and error state a recovery path
- Discloses every external or third-party interaction
- Passes the cross-consumer candidate gate before a shared release merge
