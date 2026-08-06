# Shared appearance and dark mode

The shared design system supports three user preferences: `system`, `light`, and `dark`.

## Required load order

Load the theme bootstrap synchronously in the document head before styles that paint the page:

```html
<script src="/theme-bootstrap.js"></script>
<link rel="stylesheet" href="/tokens.css">
<link rel="stylesheet" href="/theme.css">
```

The bootstrap reads the `jl_theme` cookie first, then `jl-theme-preference` from local storage, and writes both `data-theme-preference` and the resolved `data-theme` to the root element before first paint.

## Runtime controller

```js
import {
  installThemeControl,
  installThemeController,
} from "@johnnyzli/web-design-system/theme.js";

const controller = installThemeController();
installThemeControl(document.querySelector("[data-site-switcher-menu]"), controller);
```

The control is appended to the shared Sites menu. Hosted consumers persist the preference to a `.johnnyli.dev` cookie so it follows the user between Portfolio, Network Diagnostics, and RolePacket. Local development also uses local storage.

When the preference is `system`, the controller follows `prefers-color-scheme` and updates live when the operating-system preference changes. Explicit light and dark preferences remain stable.

## Product ownership

Products continue to use shared semantic color roles or documented aliases. They must not maintain parallel light and dark component implementations or hard-code alternative palettes in product stylesheets.

Product-owned analytical colors may define dark equivalents where necessary, but their meaning must remain accessible without color alone.

Print output always resolves to the approved light paper palette.
