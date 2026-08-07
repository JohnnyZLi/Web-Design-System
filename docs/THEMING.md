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

## Shared control

`installSiteSwitcher` adds the Appearance group to the Sites menu. The three buttons expose pressed state, participate in ArrowUp, ArrowDown, Home, and End traversal, and preserve Escape dismissal and focus restoration.

The Appearance choices render as a single seamless track with one terracotta selection pill that slides between `System`, `Light`, and `Dark`. The labels remain real buttons above the visual slider, preserving the existing pressed-state, focus, keyboard, and pointer behavior while avoiding individual button borders. The motion is intentionally short and is disabled when `prefers-reduced-motion` is active. Forced-colors mode removes the decorative slider and restores explicit selected-button styling for platform accessibility.

## Product ownership

Products continue using shared semantic color roles or documented aliases. They must not maintain parallel component implementations for light and dark themes. Product-owned analytical colors may define dark equivalents when their meaning remains accessible without color alone.

Print and PDF output always use the approved light paper palette. Forced-colors behavior remains independent of the selected theme.
