# Shared appearance and dark mode

The shared design system supports `System`, `Light`, and `Dark` preferences across Portfolio, Network Diagnostics, and RolePacket.

## Required load order

Load the pre-paint bootstrap synchronously before theme-aware styles:

```html
<script src="/assets/design-system/theme-bootstrap.js"></script>
<link rel="stylesheet" href="/assets/design-system/tokens.css">
<link rel="stylesheet" href="/assets/design-system/foundations.css">
<link rel="stylesheet" href="/assets/design-system/site-identity.css">
<link rel="stylesheet" href="/assets/design-system/theme-control.css">
```

The bootstrap writes the stored preference to `data-theme-preference` and the resolved light or dark state to `data-theme` before first paint.

## Persistence

Hosted consumers persist the preference through the `jl-theme` cookie scoped to `.johnnyli.dev`. Local storage mirrors the preference for local development and same-origin recovery. System mode follows `prefers-color-scheme` and updates live when the operating-system setting changes.

## Shared controls

The global header keeps navigation and preferences conceptually separate. `Sites` opens only the canonical Portfolio, Network Diagnostics, and RolePacket destinations. `installSiteSwitcher` adds an adjacent icon-only Settings control whose accessible name is `Settings`; opening it exposes the shared appearance picker.

The settings gear uses a small rotational response on hover/focus and a slightly stronger open-state rotation. This motion is disabled when `prefers-reduced-motion` is active. Opening Sites closes Settings and opening Settings closes Sites, while both preserve Escape dismissal, outside-click dismissal, ArrowUp/ArrowDown/Home/End traversal, and focus restoration.

The Appearance choices render without visible text in a compact vertical rail: monitor for `System`, sun for `Light`, and moon for `Dark`. Each real button retains an accessible label and a native hover title. A single terracotta selection pill slides vertically between the three icons, keeping the Settings popover visually distinct from the text-based Sites menu. Forced-colors mode removes the decorative slider and restores explicit selected-button styling for platform accessibility.

## Product ownership

Products continue using shared semantic color roles or documented aliases. They must not maintain parallel component implementations for light and dark themes. Product-owned analytical colors may define dark equivalents when their meaning remains accessible without color alone.

Print and PDF output always use the approved light paper palette. Forced-colors behavior remains independent of the selected theme.
