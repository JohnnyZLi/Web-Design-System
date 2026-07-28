#!/usr/bin/env python3
"""Validate and release the consumable Web Design System package contract."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "package.json"
VERSION = ROOT / "version.json"
TOKENS_JSON = ROOT / "tokens" / "tokens.tokens.json"
TOKENS_CSS = ROOT / "tokens" / "tokens.css"
STYLE_ROOT = ROOT / "styles"
SITE_IDENTITY = STYLE_ROOT / "site-identity.css"
CONTENT = STYLE_ROOT / "content.css"
CONTENT_GUARD = STYLE_ROOT / "content-guard.css"
CONTENT_PRIMITIVES = STYLE_ROOT / "content-primitives.css"
SITE_CONTROLS = ROOT / "scripts" / "site-controls.js"
SITE_CONTROL_TYPES = ROOT / "scripts" / "site-controls.d.ts"
DEPLOYMENT_SMOKE = ROOT / "scripts" / "smoke-deployments.mjs"
EXPECTED_NAME = "@johnnyzli/web-design-system"
EXPECTED_FILES = {
    "LICENSE",
    "README.md",
    "version.json",
    "tokens/tokens.css",
    "tokens/tokens.tokens.json",
    "styles/index.css",
    "styles/foundations.css",
    "styles/site-identity.css",
    "styles/content.css",
    "styles/content-guard.css",
    "styles/content-primitives.css",
    "scripts/site-controls.js",
    "scripts/site-controls.d.ts",
}
RELEASE_ADDITIONS = {
    "package.json",
    "version.json",
    "scripts/validate_package.py",
    "scripts/site-controls.js",
    "scripts/site-controls.d.ts",
    "scripts/smoke-deployments.mjs",
    "styles/index.css",
    "styles/foundations.css",
    "styles/site-identity.css",
    "styles/content.css",
    "styles/content-guard.css",
    "styles/content-primitives.css",
}
EXPECTED_EXPORTS = {
    ".": "./styles/index.css",
    "./tokens.css": "./tokens/tokens.css",
    "./tokens.json": "./tokens/tokens.tokens.json",
    "./foundations.css": "./styles/foundations.css",
    "./site-identity.css": "./styles/site-identity.css",
    "./content.css": "./styles/content.css",
    "./content-guard.css": "./styles/content-guard.css",
    "./content-primitives.css": "./styles/content-primitives.css",
    "./site-controls.js": {
        "types": "./scripts/site-controls.d.ts",
        "default": "./scripts/site-controls.js",
    },
    "./version.json": "./version.json",
    "./package.json": "./package.json",
}
RAW_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\(")
TOKEN_DEFINITION = re.compile(r"(--jl-[a-z0-9-]+)\s*:")
TOKEN_USE = re.compile(r"var\((--jl-[a-z0-9-]+)")
IMPORT = re.compile(r"@import\s+[\"']([^\"']+)[\"']")


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def token_version() -> str:
    return read_json(TOKENS_JSON)["$extensions"]["com.johnnyli.meta"]["version"]


def require_fragments(content: str, fragments: tuple[str, ...], label: str) -> None:
    for fragment in fragments:
        if fragment not in content:
            fail(f"{label} is incomplete: {fragment}")


def validate_export_path(relative: object, key: str) -> None:
    if isinstance(relative, str):
        if not relative.startswith("./") or not (ROOT / relative[2:]).is_file():
            fail(f"invalid export {key}: {relative}")
        return
    if isinstance(relative, dict):
        for condition, target in relative.items():
            validate_export_path(target, f"{key}.{condition}")
        return
    fail(f"invalid export {key}")


def validate() -> None:
    package = read_json(PACKAGE)
    version = read_json(VERSION)
    current_version = token_version()

    if package.get("name") != EXPECTED_NAME or version.get("name") != EXPECTED_NAME:
        fail("unexpected package name")
    if package.get("private") is not False:
        fail("package must remain installable")
    if package.get("version") != current_version or version.get("version") != current_version:
        fail("package, version metadata, and token source must use the same version")
    if version.get("tokenSource") != "tokens/tokens.tokens.json":
        fail("version metadata points to the wrong token source")

    package_files = set(package.get("files", []))
    if package_files != EXPECTED_FILES:
        fail(f"package files drifted: missing={sorted(EXPECTED_FILES - package_files)}, extra={sorted(package_files - EXPECTED_FILES)}")
    missing = sorted(path for path in EXPECTED_FILES | RELEASE_ADDITIONS if not (ROOT / path).is_file())
    if missing:
        fail("package references missing files: " + ", ".join(missing))

    exports = package.get("exports", {})
    if exports != EXPECTED_EXPORTS:
        fail("package exports drifted from the approved contract")
    for key, relative in exports.items():
        validate_export_path(relative, key)

    defined = set(TOKEN_DEFINITION.findall(TOKENS_CSS.read_text(encoding="utf-8")))
    used: set[str] = set()
    for path in sorted(STYLE_ROOT.glob("*.css")):
        css = path.read_text(encoding="utf-8")
        if css.count("{") != css.count("}"):
            fail(f"unbalanced CSS braces: {path.relative_to(ROOT)}")
        if RAW_COLOR.search(css):
            fail(f"raw shared color in {path.relative_to(ROOT)}")
        used.update(TOKEN_USE.findall(css))
        for target in IMPORT.findall(css):
            if target.startswith(("http://", "https://")) or not (path.parent / target).resolve().is_file():
                fail(f"invalid CSS import {target} in {path.relative_to(ROOT)}")
    missing_tokens = sorted(used - defined)
    if missing_tokens:
        fail("shared styles use undefined tokens: " + ", ".join(missing_tokens))

    site_identity = SITE_IDENTITY.read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", site_identity):
        fail("global header must remain unlayered")
    require_fragments(site_identity, (
        ".jl-site-switcher__button",
        ".jl-header-menu-toggle",
        ".jl-global-header__nav.jl-header-menu--open",
        "right: var(--jl-layout-gutter);",
        "left: var(--jl-layout-gutter);",
    ), "shared header")

    controls = SITE_CONTROLS.read_text(encoding="utf-8")
    require_fragments(controls, (
        "export const OWNED_SITES",
        "export function installDisclosureMenu",
        "export function installSiteSwitcher",
        "export function installHeaderMenu",
        'event.key === "ArrowDown"',
        'event.key === "ArrowUp"',
        'event.key === "Escape"',
        'event.key === "Home"',
        'event.key === "End"',
    ), "shared site controls")
    if "http://" in controls:
        fail("shared site controls contain an insecure URL")

    control_types = SITE_CONTROL_TYPES.read_text(encoding="utf-8")
    require_fragments(control_types, (
        "export type OwnedSiteId",
        "export interface DisclosureController",
        "export function installSiteSwitcher",
        "export function installHeaderMenu",
    ), "shared site-control types")

    content = CONTENT.read_text(encoding="utf-8")
    require_fragments(content, (
        ".jl-page__inner",
        ".jl-panel",
        ".jl-process-list",
        ".jl-metric-grid",
        ".jl-callout--success",
        ".jl-button--primary",
        ".jl-table-region",
        ".jl-empty-state",
    ), "shared content contract")

    guard = CONTENT_GUARD.read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", guard):
        fail("content guard must remain unlayered")

    primitives = CONTENT_PRIMITIVES.read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", primitives):
        fail("content primitives must remain unlayered")
    require_fragments(primitives, (
        "--jl-button-min-height",
        "--jl-button-hover-background",
        ".jl-button--compact",
        ".jl-button--danger",
        "--jl-callout-padding",
        ".jl-callout--info",
        "--jl-empty-state-padding",
        "--jl-table-region-border-width",
        "@media (forced-colors: active)",
    ), "adaptable content primitives")

    root_styles = (STYLE_ROOT / "index.css").read_text(encoding="utf-8")
    imports = [
        '@import "./content.css";',
        '@import "./content-guard.css";',
        '@import "./content-primitives.css";',
    ]
    positions = [root_styles.index(value) for value in imports]
    if positions != sorted(positions):
        fail("content primitives must load after content and its guard")

    smoke = DEPLOYMENT_SMOKE.read_text(encoding="utf-8")
    require_fragments(smoke, (
        "https://johnnyli.dev",
        "https://network.johnnyli.dev",
        "https://rolepacket.johnnyli.dev",
        "ROLEPACKET_ACCESS_CLIENT_ID",
        "CF-Access-Client-Id",
        "Deployed-site smoke checks passed.",
    ), "deployment smoke checks")

    generated_header = f"Design-system version: {current_version} */"
    if generated_header not in TOKENS_CSS.read_text(encoding="utf-8"):
        fail("generated token CSS version header drifted")

    print(f"Package validation passed for {EXPECTED_NAME} v{current_version}.")


def append_release() -> None:
    validate()
    version = token_version()
    archive = ROOT / "dist" / f"Johnny_Li_Web_Design_System_v{version}.zip"
    if not archive.is_file():
        fail("base release archive is missing; run the design-system release first")
    prefix = Path(f"Web-Design-System-v{version}")
    with zipfile.ZipFile(archive, "a", zipfile.ZIP_DEFLATED) as output:
        existing = set(output.namelist())
        for relative_text in sorted(RELEASE_ADDITIONS):
            destination = (prefix / relative_text).as_posix()
            if destination not in existing:
                output.write(ROOT / relative_text, destination)
    print(f"Added package contract to {archive.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="validate", choices=["validate", "release"])
    args = parser.parse_args()
    {"validate": validate, "release": append_release}[args.command]()


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, TypeError, ValueError, zipfile.BadZipFile) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
