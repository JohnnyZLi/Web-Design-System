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
}
RELEASE_ADDITIONS = {
    "package.json",
    "version.json",
    "scripts/validate_package.py",
    "styles/index.css",
    "styles/foundations.css",
    "styles/site-identity.css",
}
RAW_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\(")
TOKEN_DEFINITION = re.compile(r"(--jl-[a-z0-9-]+)\s*:")
TOKEN_USE = re.compile(r"var\((--jl-[a-z0-9-]+)")
IMPORT = re.compile(r"@import\s+[\"']([^\"']+)[\"']")


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def package_version() -> str:
    tokens = read_json(TOKENS_JSON)
    return tokens["$extensions"]["com.johnnyli.meta"]["version"]


def validate() -> None:
    package = read_json(PACKAGE)
    version_metadata = read_json(VERSION)
    token_version = package_version()

    if package.get("name") != EXPECTED_NAME:
        fail("unexpected package name")
    if package.get("private") is not False:
        fail("package must remain installable")
    if package.get("version") != token_version:
        fail("package version does not match token source")
    if version_metadata.get("name") != EXPECTED_NAME:
        fail("version metadata package name does not match")
    if version_metadata.get("version") != token_version:
        fail("version metadata does not match token source")
    if version_metadata.get("tokenSource") != "tokens/tokens.tokens.json":
        fail("version metadata points to the wrong token source")

    package_files = set(package.get("files", []))
    if package_files != EXPECTED_FILES:
        missing = sorted(EXPECTED_FILES - package_files)
        extra = sorted(package_files - EXPECTED_FILES)
        fail(f"package files changed; missing={missing}, extra={extra}")

    required_paths = EXPECTED_FILES | RELEASE_ADDITIONS
    missing_paths = sorted(path for path in required_paths if not (ROOT / path).is_file())
    if missing_paths:
        fail("package references missing files: " + ", ".join(missing_paths))

    exports = package.get("exports", {})
    for key, relative in exports.items():
        if not isinstance(relative, str) or not relative.startswith("./"):
            fail(f"invalid export {key}")
        if not (ROOT / relative[2:]).is_file():
            fail(f"export {key} references missing file {relative}")

    defined = set(TOKEN_DEFINITION.findall(TOKENS_CSS.read_text(encoding="utf-8")))
    used: set[str] = set()
    for path in sorted(STYLE_ROOT.glob("*.css")):
        content = path.read_text(encoding="utf-8")
        if content.count("{") != content.count("}"):
            fail(f"unbalanced CSS braces: {path.relative_to(ROOT)}")
        if RAW_COLOR.search(content):
            fail(f"raw shared color in {path.relative_to(ROOT)}")
        used.update(TOKEN_USE.findall(content))
        for target in IMPORT.findall(content):
            if target.startswith(("http://", "https://")):
                fail(f"remote CSS import in {path.relative_to(ROOT)}")
            if not (path.parent / target).resolve().is_file():
                fail(f"missing CSS import {target} in {path.relative_to(ROOT)}")

    missing_tokens = sorted(used - defined)
    if missing_tokens:
        fail("shared styles use undefined tokens: " + ", ".join(missing_tokens))

    site_identity = SITE_IDENTITY.read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", site_identity):
        fail("global header must remain unlayered so product resets cannot override it")
    for fragment in (
        "width: 88px;",
        "height: var(--jl-control-height-md);",
        "font-family: var(--jl-font-ui);",
        "font-size: 13px;",
        "font-weight: 700;",
        "line-height: 1;",
        ".jl-site-switcher__chevron",
        "border-right: 2px solid currentColor;",
        "border-bottom: 2px solid currentColor;",
    ):
        if fragment not in site_identity:
            fail(f"shared Sites control contract is incomplete: {fragment}")

    generated_header = f"Design-system version: {token_version} */"
    if generated_header not in TOKENS_CSS.read_text(encoding="utf-8"):
        fail("generated token CSS version header drifted")

    print(f"Package validation passed for {EXPECTED_NAME} v{token_version}.")


def append_release() -> None:
    validate()
    version = package_version()
    archive = ROOT / "dist" / f"Johnny_Li_Web_Design_System_v{version}.zip"
    if not archive.is_file():
        fail("base release archive is missing; run the design-system release first")

    prefix = Path(f"Web-Design-System-v{version}")
    with zipfile.ZipFile(archive, "a", zipfile.ZIP_DEFLATED) as output:
        existing = set(output.namelist())
        for relative_text in sorted(RELEASE_ADDITIONS):
            destination = (prefix / relative_text).as_posix()
            if destination in existing:
                continue
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
