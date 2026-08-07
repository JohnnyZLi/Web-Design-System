#!/usr/bin/env python3
from pathlib import Path

css = (Path(__file__).resolve().parents[1] / "styles" / "site-identity.css").read_text(encoding="utf-8")
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
    "@keyframes jl-attached-menu-reveal",
    "animation: jl-attached-menu-reveal 190ms cubic-bezier(0.2, 0.8, 0.2, 1) both;",
    "clip-path: inset(0 0 100% 0);",
    "clip-path: inset(0);",
    "z-index: calc(var(--jl-z-menu) + 1);",
    "margin: -2px 0 0;",
    ".jl-site-menu a:focus-visible {",
    "box-shadow: inset 0 0 0 2px var(--jl-color-focus-ring);",
    ".jl-site-switcher__button[aria-expanded=\"true\"]:hover,",
    "border-color: var(--jl-color-rule-strong);",
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
):
    if fragment in css:
        raise SystemExit(f"Sites menu must remain attached to the Sites column without overlapping the trigger: {fragment}")

compact_block = css.split("@media (max-width: 420px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")

print("Extreme-compact header contract passed.")
