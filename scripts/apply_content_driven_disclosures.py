#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
css_path = root / "styles" / "site-identity.css"
contract_path = root / "scripts" / "validate_header_contract.py"

css = css_path.read_text(encoding="utf-8")

replacements = {
    """  grid-template-rows: var(--_jl-disclosure-trigger-height) auto;\n  max-height: var(--_jl-disclosure-trigger-height);""": """  grid-template-rows: var(--_jl-disclosure-trigger-height) 0fr;\n  max-height: none;""",
    """  z-index: var(--jl-z-menu);\n  max-height: 190px;""": """  z-index: var(--jl-z-menu);\n  grid-template-rows: var(--_jl-disclosure-trigger-height) 1fr;\n  max-height: none;""",
    """  grid-column: 1;\n  grid-row: 2;\n  justify-self: stretch;\n}""": """  grid-column: 1;\n  grid-row: 2;\n  min-height: 0;\n  overflow: hidden;\n  justify-self: stretch;\n}""",
    """    transition: max-height 190ms cubic-bezier(0.2, 0.8, 0.2, 1),\n      box-shadow 120ms ease;""": """    transition: grid-template-rows 190ms cubic-bezier(0.2, 0.8, 0.2, 1),\n      box-shadow 120ms ease;""",
}

for old, new in replacements.items():
    if old not in css:
        raise SystemExit(f"Expected disclosure CSS fragment not found:\n{old}")
    css = css.replace(old, new, 1)

css_path.write_text(css, encoding="utf-8")

contract = contract_path.read_text(encoding="utf-8")
contract = contract.replace(
    '    "max-height: var(--_jl-disclosure-trigger-height);",\n    "max-height: 190px;",',
    '    "grid-template-rows: var(--_jl-disclosure-trigger-height) 0fr;",\n    "grid-template-rows: var(--_jl-disclosure-trigger-height) 1fr;",\n    "max-height: none;",',
)
contract = contract.replace(
    '    ".jl-settings-disclosure > .jl-settings-button",\n    "@keyframes jl-attached-menu-reveal",',
    '    ".jl-settings-disclosure > .jl-settings-button",\n    "min-height: 0;",\n    "overflow: hidden;",\n    "transition: grid-template-rows 190ms cubic-bezier(0.2, 0.8, 0.2, 1),",\n    "@keyframes jl-attached-menu-reveal",',
)
contract = contract.replace(
    '    "margin: -2px 0 0;",\n):',
    '    "margin: -2px 0 0;",\n    "max-height: 190px;",\n    "transition: max-height 190ms",\n    "grid-template-rows: var(--_jl-disclosure-trigger-height) auto;",\n):',
)
contract_path.write_text(contract, encoding="utf-8")

print("Applied content-driven disclosure sizing and updated the header contract.")
