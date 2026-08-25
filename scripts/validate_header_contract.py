#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
css = (root / "styles" / "site-identity.css").read_text(encoding="utf-8")
theme_css = (root / "styles" / "theme-control.css").read_text(encoding="utf-8")
controls = (root / "scripts" / "site-controls.js").read_text(encoding="utf-8")
specimen = (root / "specimen" / "index.html").read_text(encoding="utf-8")
required = (
    "grid-template-columns: 104px var(--jl-control-height-md);",
    ".jl-site-switcher__button {\n  width: 104px;",
    "min-width: 104px;",
    ".jl-site-menu {\n  width: 104px;",
    "grid-column: 1;",
    "justify-self: stretch;",
    ".jl-site-menu a {\n  width: 100%;",
    "white-space: normal;",
    "justify-content: center;",
    "text-align: center;",
    ".jl-site-disclosure,\n.jl-settings-disclosure {",
    "grid-template-rows: var(--_jl-disclosure-trigger-height) 0fr;",
    "grid-template-rows: var(--_jl-disclosure-trigger-height) 1fr;",
    "max-height: none;",
    "box-shadow: inset 0 0 0 1px var(--jl-color-rule-strong);",
    ".jl-site-disclosure > .jl-site-switcher__button,",
    ".jl-settings-disclosure > .jl-settings-button",
    "min-height: 0;",
    "overflow: hidden;",
    "transition: grid-template-rows 190ms cubic-bezier(0.2, 0.8, 0.2, 1),",
    "@keyframes jl-attached-menu-reveal",
    "animation: jl-attached-menu-reveal 170ms 20ms cubic-bezier(0.2, 0.8, 0.2, 1) both;",
    "clip-path: inset(0 0 100% 0);",
    "clip-path: inset(0);",
    ".jl-site-menu a:focus-visible {",
    "box-shadow: inset 0 0 0 2px var(--jl-color-focus-ring);",
    "@media (max-width: 420px)",
    "width: calc(100% - 8px);",
    "grid-template-columns: 104px 40px;",
    ".jl-global-header__actions {\n    gap: calc(var(--jl-space-1) / 2);",
    ".jl-header-menu-toggle {\n    min-width: 40px;",
    "grid-template-columns: 96px 40px;",
    "width: 96px;",
)
for fragment in required:
    if fragment not in css:
        raise SystemExit(f"Extreme-compact header contract is incomplete: {fragment}")

chevron_required = (
    ".jl-site-switcher__chevron {",
    ".jl-site-switcher__content {",
    "display: inline-grid;",
    "grid-template-columns: max-content 0.85em;",
    "column-gap: 0.55em;",
    ".jl-site-switcher__label {",
    "width: 0.85em;",
    "height: 0.85em;",
    "overflow: visible;",
    ".jl-site-switcher__chevron path {",
    "transform-box: fill-box;",
    "transform-origin: center;",
    "stroke: currentColor;",
    "stroke-linecap: round;",
    "stroke-linejoin: round;",
    "transform: rotate(0deg);",
    "transform: rotate(180deg);",
    '[aria-hidden="true"]:not(svg)',
)
for fragment in chevron_required:
    if fragment not in css:
        raise SystemExit(f"Sites chevron contract is incomplete: {fragment}")

for fragment in (
    '<svg class="jl-site-switcher__chevron" viewBox="0 0 12 12" aria-hidden="true" focusable="false">',
    '<span class="jl-site-switcher__content">',
    '<span class="jl-site-switcher__label">Sites</span>',
    '<path d="M2.5 5.25 6 8.75 9.5 5.25"></path>',
):
    if fragment not in specimen:
        raise SystemExit(f"Specimen Sites trigger is missing canonical SVG markup: {fragment}")

wide_header_required = (
    "/* Shared wide-desktop header rail.",
    "@media (min-width: 1024px)",
    "width: 100%;",
    "grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);",
    "padding-left: 40px;",
    "padding-right: 20px;",
    "transform: translateX(-10px);",
)
for fragment in wide_header_required:
    if fragment not in css:
        raise SystemExit(f"Wide-desktop header rail contract is incomplete: {fragment}")

full_header_required = (
    "/* Keep the complete top bar together while Sites or Settings is open.",
    ":is(.jl-global-header, .jl-site-header):has([data-site-switcher-button][aria-expanded=\"true\"])",
    ":is(.jl-global-header, .jl-site-header):has([data-settings-button][aria-expanded=\"true\"])",
    "position: fixed;",
    "z-index: calc(var(--jl-z-menu) - 1);",
    "height: calc(var(--jl-layout-header-height) + 1px);",
    "min-height: calc(var(--jl-layout-header-height) + 1px);",
    "max-height: calc(var(--jl-layout-header-height) + 1px);",
    "border-bottom: 1px solid var(--jl-color-rule);",
    "background: var(--jl-color-canvas);",
    ".jl-global-header__inner {",
    "right: 0;",
    "left: 0;",
    "margin-inline: auto;",
    "height: 69px;",
    "[data-jl-header-disclosure-exit]",
    "animation: jl-header-disclosure-exit 400ms cubic-bezier(0.4, 0, 0.2, 1) both;",
    "@keyframes jl-header-disclosure-exit",
    "top: var(--_jl-header-disclosure-exit-y, calc(-1 * var(--jl-layout-header-height)));",
)
for fragment in full_header_required:
    if fragment not in theme_css:
        raise SystemExit(f"Open disclosures must pin the complete top bar: {fragment}")

fixed_inner_block = theme_css.split(
    ':is(.jl-global-header, .jl-site-header):has([data-site-switcher-button][aria-expanded="true"]) .jl-global-header__inner,',
    1,
)[1].split("@media (max-width: 560px)", 1)[0]
for forbidden in ("left: 50%;", "transform: translateX(-50%);"):
    if forbidden in fixed_inner_block:
        raise SystemExit(f"Full-header centering must not depend on transforms: {forbidden}")

for fragment in (
    "/* Keep open Sites and Settings controls pinned to the viewport. */",
    "min-width: calc(104px + var(--jl-space-2) + var(--jl-control-height-md));",
):
    if fragment in css:
        raise SystemExit(f"Control-only disclosure pinning must not return: {fragment}")

if "/* Neutralize the older control-only pin" in theme_css:
    raise SystemExit("Full-header pinning must not depend on neutralizing an older control-only rule.")

for fragment in (
    "width: 144px;",
    "min-width: 144px;",
    "--_jl-site-menu-trigger-offset",
    ".jl-site-menu::before",
    ".jl-site-menu::after",
    "grid-column: 1 / 3;",
    "transform: translateY(-7px) scaleY(0.97);",
    "border-bottom-color: transparent;",
    "border-bottom-right-radius: 0;",
    "border-bottom-left-radius: 0;",
    "margin: -2px 0 0;",
    "max-height: 190px;",
    "transition: max-height 190ms",
    "grid-template-rows: var(--_jl-disclosure-trigger-height) auto;",
):
    if fragment in css:
        raise SystemExit(f"Sites menu must remain attached to the Sites column without overlapping the trigger: {fragment}")

for fragment in (
    "function ensureDisclosureShell",
    "\"jl-site-disclosure\"",
    "\"jl-settings-disclosure\"",
    "function installHeaderDisclosureExit",
    "data-jl-header-disclosure-exit",
    "--_jl-header-disclosure-exit-y",
    "headerExit.sync(open)",
    "onOpenChange: headerExit.sync",
):
    if fragment not in controls:
        raise SystemExit(f"Shared site controls must create unified disclosure shells: {fragment}")

compact_block = css.split("@media (max-width: 420px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")


compact_utility_required = (
    ".jl-global-header--compact-utility",
    "min-height: 72px;",
    "width: 140px;",
    "grid-template-columns: 96px var(--jl-control-height-md);",
    "background: color-mix(in srgb, var(--jl-color-surface) 42%, transparent);",
    "border-left: 1px solid var(--jl-color-rule);",
    "background: color-mix(in srgb, var(--jl-color-surface-strong) 38%, transparent);",
)
for fragment in compact_utility_required:
    if fragment not in css:
        raise SystemExit(f"Compact utility header contract is incomplete: {fragment}")

compact_utility_theme_required = (
    "compact utility header keeps a 73px",
    ".jl-global-header.jl-global-header--compact-utility",
    "height: 73px;",
)
for fragment in compact_utility_theme_required:
    if fragment not in theme_css:
        raise SystemExit(f"Compact utility pinned-header contract is incomplete: {fragment}")

print("Extreme-compact and full-header disclosure contracts passed.")
