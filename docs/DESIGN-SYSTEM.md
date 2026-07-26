# Johnny Li Web Design System

## 1. Status and normative language

**Version:** 1.3.4  
**Status:** Implementation candidate  
**Owner:** Johnny Li

- **MUST** means required for conformance.
- **SHOULD** means expected unless a documented exception exists.
- **MAY** means optional.
- **CURRENT** describes existing behavior.
- **TARGET** describes intended post-migration behavior.

The system becomes an implementation contract only after the specimen is approved, current production baselines are recorded, tokens are integrated into all three sites, and the core migrations pass product-level testing.

## 2. Identity and sources

> **Editorial warmth, systems precision.**

The sites MUST feel related without becoming identical:

- Portfolio: editorial and spacious
- Network Diagnostics: analytical and data-oriented
- RolePacket: dense and workflow-oriented

### Source mapping

**Portfolio contribution**

- Warm paper canvas
- Near-black ink
- Terracotta family
- Exact 5px dot texture
- Editorial serif stack
- Open sections and fine rules
- Large display typography
- Restrained motion
- Approximately 1328px editorial rail

**Network Diagnostics contribution**

- 1360px analytical rail
- Sticky product header
- Test-control panel and segmented selector
- Terracotta run action
- Progress stage and metric cards
- Monospace measurements
- Semantic data colors and chart patterns

**RolePacket contribution**

- Wide-screen sidebar concept
- Dense application rows
- 24px working panels
- Review statuses and provenance
- Before/proposed comparisons
- Version and workflow metadata
- Forms and action bars

**Newly derived shared rules**

- Accessible text accent and muted colors
- 3:1 semantic borders
- Inverse surface tokens
- Dual focus rings
- Typed DTCG tokens and generated CSS
- Pointer-target policy
- Non-color chart cues
- Responsive transformation and validation rules

## 3. Principles

1. **Warm, not rustic.** Warm neutrals and terracotta pair with precise spacing and geometry.
2. **Technical, not sterile.** Monospace is reserved for measurements and compact metadata.
3. **Quiet by default.** Color appears only for brand emphasis, data, state, or action.
4. **Structure before decoration.** Spacing and rules precede cards, shadows, and glows.
5. **Recompose instead of shrink.** Layout changes before content becomes cramped.
6. **One authoritative value.** Components consume tokens instead of inventing nearby values.
7. **Meaning survives without color.** Labels, shapes, icons, and line styles preserve meaning.

## 4. Tokens

`tokens/tokens.tokens.json` is the sole editable source. It follows the Design Tokens Community Group 2025.10 structure with `$value`, `$type`, typed colors, dimensions, durations, shadows, font families, and cubic Bézier values.

CSS-specific fluid expressions are stored in the namespaced `com.johnnyli.css` extension. `tokens/tokens.css` is generated and MUST NOT be edited manually.

### Color rules

- Canvas is warm paper.
- Primary text is near-black ink.
- Terracotta is the only decorative text color.
- Semantic colors are reserved for status and data.
- Normal text and controls use the accessible accent, not the lighter decorative terracotta.
- Status and chart meaning MUST survive grayscale.
- Semantic components use the complete text/surface/border triplet.
- Shared raw colors MUST NOT appear outside the token source or generated output.

### Typography

The system intentionally uses platform fonts rather than requiring Inter:

- UI: system sans
- Editorial emphasis: Iowan/Palatino/Georgia stack
- Measurements: system monospace

The serif MUST remain selective and MUST NOT become the default interface body typeface.

### Background

```css
background:
  radial-gradient(var(--jl-color-canvas-dot) 0.55px, transparent 0.7px),
  var(--jl-color-canvas);
background-size: 5px 5px;
```

Do not combine the dot texture with a visible grid. Use at most one restrained warm glow in a major viewport region.

### Radius and elevation

- 8px: compact controls and badges
- 12px: buttons and fields
- 18px: analytical cards
- 24px: major panels and dialogs
- Pill: statuses and filters only

Portfolio sections SHOULD remain mostly flat. Network Diagnostics and RolePacket MAY use low elevation for major working surfaces.

## 5. Responsive behavior

| Available width | Target composition |
| --- | --- |
| Below 480px | Single-column phone |
| 480–767px | Large phone or compact tablet |
| 768–1023px | Tablet |
| 1024–1439px | Laptop or desktop |
| 1440px and above | Capped content rail |

Components SHOULD use container queries when their own width matters more than the viewport.

Required transformations:

- Two-column heroes become one column.
- Four-column metric grids become two, then one.
- Multi-column forms become one before labels or errors become cramped.
- Sidebars become an accessible compact drawer or an equivalent explicitly documented navigation transformation.
- Before/proposed comparisons stack vertically.
- Genuine tables MAY scroll, but essential summaries remain available without scrolling.
- No page may have document-level overflow at 320px.
- Core workflows MUST remain usable at 200% zoom.

### Wrapping and truncation

- Primary titles MAY clamp to two lines in dense list rows.
- Full titles MUST appear in details and accessible names.
- Statuses and primary navigation MUST NOT truncate.
- URLs MUST break safely.
- File names MAY middle-truncate only when the extension remains visible.

## 6. Focus, targets, and accessibility

Target WCAG 2.2 AA.

- Controls MUST meet the 24×24 CSS-pixel target requirement or an applicable exception.
- Primary, icon, and touch-oriented controls SHOULD expose a 44×44 target.
- Focus uses a dual ring on light, dark, and terracotta surfaces.
- Sticky UI MUST NOT fully obscure focused components.
- Global shells MUST set suitable scroll padding.
- Every essential action MUST support keyboard use.
- Normal text requires 4.5:1 contrast.
- Meaningful UI and graphic boundaries require 3:1 where non-text contrast applies.
- State and errors MUST remain understandable without color.
- Reduced-motion and forced-colors modes MUST preserve functionality.
- Dialogs MUST contain and restore focus.
- Responsive stacking MUST preserve logical DOM order.

PDF exports are not assumed to be fully tagged until validated. Accessible HTML remains the authoritative accessible alternative.

## 7. Component system

Every canonical component defines:

- Purpose and anatomy
- Variants and states
- Sizing and responsive behavior
- Keyboard and screen-reader behavior
- Content limits
- Canonical and prohibited examples

Shared inventory:

- Global header, site identity, and site switcher
- Navigation and menus
- Links and buttons
- Fields and selectors
- Panels and ruled rows
- Status badges
- Disclosures and dialogs
- Toasts, loading, errors, and empty states

### State requirements

| State | Requirement |
| --- | --- |
| Default | Clear affordance |
| Hover | Reinforcement only |
| Focus | Dual ring and logical order |
| Active | Immediate feedback and single invocation |
| Current | Persistent text plus visual cue |
| Disabled | Legible and noninteractive |
| Loading | Stable size and duplicate prevention |
| Error | Written reason and recovery |
| Success | Persistent when important; not toast- or color-only |

### Global header and navigation

Every owned website page MUST use the shared `jl-global-header` component contract. Product adapters MUST NOT redefine the header rail, owner/product typography, Sites control geometry, or menu styling.

Canonical identity labels:

- `Johnny Li / Portfolio`
- `Johnny Li / Network Diagnostics`
- `Johnny Li / RolePacket`

The shared desktop header uses:

- 82px minimum height
- The shared 1328px inner rail and responsive gutters
- Owner/product identity in the first column
- Optional product navigation in the middle column
- The Sites control in the final column
- An exact 88×44px Sites control with 13px/700 UI typography and a CSS-drawn chevron

At compact widths the header becomes 68px high, hides the owner and separator while retaining the product identity, and keeps the Sites control at 88×40px. Product navigation that no longer fits MUST remain reachable through a product-owned compact navigation pattern rather than disappearing.

Every owned site MUST reach the other two within two interactions. Owned-site links open in the same tab. External destinations MAY open in a new tab.

## 8. Product patterns

Detailed business logic, state machines, authentication internals, and extension behavior belong in product repositories. This public system defines the visual and interaction patterns only.

### Portfolio

Preserve:

- Open editorial sections
- Large display type
- Fine structural rules
- Selective terracotta and serif emphasis
- Exact dot texture
- Minimal card use
- Dark inverse contact section

TARGET:

- Hero becomes one reading column.
- Work rows stack as metadata, title, description, and action.
- Product navigation remains accessible without turning the portfolio into application chrome.
- Portfolio case studies use the same global header and shared foundations as the homepage.

### Network Diagnostics

Preserve:

- Sticky product header
- Terracotta primary test action
- Monospace measurements
- Full-width analytical sections
- Clear methodology and privacy language
- Data colors with line, marker, and label cues

Canonical patterns:

- Test selector: name, duration, and data cap
- Progress stage: phase, progress, measurements, and cancel
- Metric card: label, exact value, unit, and context
- Grade: written grade and threshold explanation
- Chart: bounded aspect ratio, exact values outside tooltip, text summary
- Privacy: precise text such as “Stored in this browser,” never an unlabeled green dot

Stable chart mapping:

| Role | Color | Additional cue |
| --- | --- | --- |
| Download | Accent | Solid line or filled bar |
| Upload | Information | Dashed line or marker |
| Idle latency | Ink | Solid thin line or circle |
| Download-loaded latency | Violet | Dashed line or square |
| Upload-loaded latency | Warning | Dotted line or triangle |
| Loss/failure | Danger | Cross marker or hatch |
| Healthy threshold | Success | Labeled reference line |

### RolePacket

Preserve:

- Dense review-first workflow
- Sidebar at wide widths and accessible drawer at compact widths
- Ruled application rows
- Explicit status and provenance
- Before/proposed comparisons
- Version and review metadata
- Terracotta dominant workflow action
- Neutral action where brand emphasis is unnecessary

Canonical patterns:

- Application row: role, company, location, written status, updated time, and action
- Fit verdict: written eligibility, alignment, confidence, and rationale
- Requirement coverage: `Strong`, `Partial`, or `Missing`
- Resume change: before, proposed, state, accept, and keep-original
- Action bar: current-step actions only; returns to document flow when sticky positioning obstructs content
- Authentication: product identity, reason access is required, and route back to portfolio

Detailed application status transitions remain in RolePacket.

## 9. Content and interaction

### Voice

The interface is direct, calm, specific, and technically honest.

- Name the object, action, and consequence.
- Prefer plain language to implementation terms.
- State uncertainty and limitations.
- Avoid hype and vague reassurance.
- Do not claim privacy, security, completion, or success without defining the boundary.

Use sentence case.

### Action labels

| Avoid | Use |
| --- | --- |
| Submit | Save application or Submit application |
| Continue | Review changes |
| OK | Close |
| Yes | Delete application |
| Process | Import resume |
| Start | Run test |
| Retry | Try test again |

### Errors and async states

Every error answers:

1. What failed?
2. What was preserved?
3. What can the user do next?

Loading names the current operation. Controls retain stable dimensions and prevent duplicate activation. User-authored text remains after failure. Background refresh MUST NOT overwrite active edits. Partial success states both outcomes and retries only the failed portion.

### Trust and provenance

Use exact labels:

- Stored in this browser
- Uploaded to RolePacket
- User-provided
- AI-proposed
- User-approved
- Exported locally
- Requires Cloudflare Access

AI-proposed content MUST remain distinct from approved content until approval. Generic secure/private dots are prohibited.

## 10. Engineering

### Browser support

The machine-readable policy is `.browserslistrc`:

- Last two Chrome, Edge, Firefox, Safari, and iOS versions
- Browsers not marked dead by Browserslist
- Review every six months

Product extensions SHOULD record an exact minimum browser version in their own repository.

### CSS architecture

```css
@layer reset, tokens, base, layout, components, features, utilities, overrides;
```

`overrides` is temporary and requires a documented exception. Permanent `hotfixes.css`, `polish.css`, or equivalent files are prohibited after migration.

### Performance

Core Web Vitals good thresholds are TARGETS for public pages:

- LCP ≤ 2.5 seconds
- INP ≤ 200 milliseconds
- CLS ≤ 0.1

Evaluate p75 separately for mobile and desktop when sufficient field data exists.

Bundle and transfer budgets are not mandatory until production builds are measured. `ci/performance-baselines.json` records pending baselines. Test payloads are excluded from ordinary Network Diagnostics page-load transfer.

### Validation

`make validate` checks:

- DTCG structure
- Generated-token drift
- Contrast
- CSS override syntax
- Markdown structure and links
- Specimen assets and CSS variables
- Raw colors outside token files
- Explicit release-package contents
- Sensitive filenames and common credential patterns
- Private network addresses, local home paths, and Cloudflare identifiers
- Public exposure of internal commit snapshots and private source paths

GitHub Actions runs the same command on pushes and pull requests.

## 11. Governance and conformance

### Versioning

- Patch: clarification or fix with no intentional design change
- Minor: backward-compatible token, pattern, or component
- Major: changed token meaning, removed component, or coordinated migration

### Shared changes

A shared change includes:

1. Problem statement
2. Sites and components affected
3. Accessibility and responsive impact
4. Before/after evidence
5. Migration and rollback

### Exceptions

No exceptions are approved for version 1.3.4. Future exceptions MUST record the rule, repository/component, rationale, owner, review date, removal issue, and accessibility impact.

### Conformance checklist

- Generated tokens match the DTCG source.
- No unapproved raw shared colors exist.
- No undocumented permanent override exists.
- 320px overflow and 200% zoom checks pass.
- Keyboard order and focus restoration pass.
- Sticky UI does not fully obscure focus.
- Status and chart meaning survive grayscale.
- Sensitive actions state the data, destination or consequence, reversibility, and next step.
- PDF accessibility limitations are disclosed where applicable.
