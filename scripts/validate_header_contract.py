#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
css = (root / "styles" / "site-identity.css").read_text(encoding="utf-8")
theme_css = (root / "styles" / "theme-control.css").read_text(encoding="utf-8")
controls = (root / "scripts" / "site-controls.js").read_text(encoding="utf-8")
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
    "/* Keep open Sites and Settings controls pinned to the viewport. */",
    ".jl-global-header__actions {\n  min-width: calc(104px + var(--jl-space-2) + var(--jl-control-height-md));",
    "position: fixed;",
    "top: 19px;",
    "right: max(",
    "min-width: 136px;",
)
for fragment in required:
    if fragment not in css:
        raise SystemExit(f"Extreme-compact header contract is incomplete: {fragment}")

full_header_required = (
    "/* Keep the complete top bar together while Sites or Settings is open.",
    ":is(.jl-global-header, .jl-site-header):has([data-site-switcher-button][aria-expanded=\"true\"])",
    ":is(.jl-global-header, .jl-site-header):has([data-settings-button][aria-expanded=\"true\"])",
    "position: fixed;",
    "z-index: calc(var(--jl-z-menu) - 1);",
    "height: var(--jl-layout-header-height);",
    "border-bottom: 1px solid var(--jl-color-rule);",
    "background: var(--jl-color-canvas);",
    ".jl-global-header__inner {",
    "right: 0;",
    "left: 0;",
    "margin-inline: auto;",
    "/* Neutralize the older control-only pin",
    ".jl-site-switcher {",
    "position: relative;",
    "top: auto;",
    "right: auto;",
    "height: 68px;",
)
for fragment in full_header_required:
    if fragment not in theme_css:
        raise SystemExit(f"Open disclosures must pin the complete top bar: {fragment}")

fixed_inner_block = theme_css.split(
    ':is(.jl-global-header, .jl-site-header):has([data-site-switcher-button][aria-expanded="true"]) .jl-global-header__inner,',
    1,
)[1].split("/* Neutralize the older control-only pin", 1)[0]
for forbidden in ("left: 50%;", "transform: translateX(-50%);"):
    if forbidden in fixed_inner_block:
        raise SystemExit(f"Full-header centering must not depend on transforms: {forbidden}")

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
):
    if fragment not in controls:
        raise SystemExit(f"Shared site controls must create unified disclosure shells: {fragment}")

compact_block = css.split("@media (max-width: 420px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")

print("Extreme-compact and full-header disclosure contracts passed.")
