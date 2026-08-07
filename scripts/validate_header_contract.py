#!/usr/bin/env python3
from pathlib import Path

css = (Path(__file__).resolve().parents[1] / "styles" / "site-identity.css").read_text(encoding="utf-8")
required = (
    "grid-template-columns: 88px var(--jl-control-height-md);",
    ".jl-site-switcher__button {\n  width: 88px;",
    "min-width: 88px;",
    ".jl-site-menu {\n  --_jl-site-menu-trigger-offset:",
    "width: 144px;",
    "min-width: 144px;",
    "grid-column: 1 / 3;",
    "justify-self: end;",
    ".jl-site-menu::before,\n.jl-site-menu::after {",
    "width: calc(var(--_jl-site-menu-trigger-offset) + 1px);",
    "left: calc(var(--_jl-site-menu-trigger-offset) + 88px);",
    ".jl-site-menu a {\n  width: 100%;",
    "min-width: 0;",
    ".jl-site-menu a:focus-visible {",
    "box-shadow: inset 0 0 0 2px var(--jl-color-focus-ring);",
    ".jl-site-switcher__button[aria-expanded=\"true\"]:hover,",
    "border-color: var(--jl-color-rule-strong);",
    "@media (max-width: 420px)",
    "width: calc(100% - 8px);",
    "grid-template-columns: 88px 40px;",
    ".jl-global-header__actions {\n    gap: calc(var(--jl-space-1) / 2);",
    ".jl-header-menu-toggle {\n    min-width: 40px;",
    "--_jl-site-menu-trigger-offset: 16px;",
    "white-space: nowrap;",
)
for fragment in required:
    if fragment not in css:
        raise SystemExit(f"Extreme-compact header contract is incomplete: {fragment}")

compact_block = css.split("@media (max-width: 420px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")

print("Extreme-compact header contract passed.")
