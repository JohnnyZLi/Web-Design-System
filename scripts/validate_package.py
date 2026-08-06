#!/usr/bin/env python3
"""Validate and append the consumable Web Design System package contract."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STYLE_ROOT = ROOT / "styles"
TOKENS_JSON = ROOT / "tokens" / "tokens.tokens.json"
TOKENS_CSS = ROOT / "tokens" / "tokens.css"
EXPECTED_NAME = "@johnnyzli/web-design-system"
EXPECTED_FILES = {
    "LICENSE", "README.md", "version.json",
    "tokens/tokens.css", "tokens/tokens.tokens.json",
    "styles/index.css", "styles/foundations.css", "styles/site-identity.css",
    "styles/theme-control.css", "styles/content.css", "styles/content-guard.css", "styles/content-primitives.css",
    "conformance/contract.json", "conformance/contract.schema.json", "conformance/manifest.schema.json",
    "scripts/theme-bootstrap.js", "scripts/site-controls.js", "scripts/site-controls.d.ts", "scripts/consumer-release.mjs",
    "scripts/conformance-runner.mjs",
}
EXPECTED_EXPORTS = {
    ".": "./styles/index.css",
    "./tokens.css": "./tokens/tokens.css",
    "./tokens.json": "./tokens/tokens.tokens.json",
    "./foundations.css": "./styles/foundations.css",
    "./site-identity.css": "./styles/site-identity.css",
    "./theme-control.css": "./styles/theme-control.css",
    "./content.css": "./styles/content.css",
    "./content-guard.css": "./styles/content-guard.css",
    "./content-primitives.css": "./styles/content-primitives.css",
    "./theme-bootstrap.js": "./scripts/theme-bootstrap.js",
    "./site-controls.js": {
        "types": "./scripts/site-controls.d.ts",
        "default": "./scripts/site-controls.js",
    },
    "./consumer-release.js": "./scripts/consumer-release.mjs",
    "./conformance-runner.js": "./scripts/conformance-runner.mjs",
    "./conformance/contract.json": "./conformance/contract.json",
    "./conformance/contract.schema.json": "./conformance/contract.schema.json",
    "./conformance/manifest.schema.json": "./conformance/manifest.schema.json",
    "./version.json": "./version.json",
    "./package.json": "./package.json",
}
RELEASE_ADDITIONS = {
    "package.json", "version.json", "scripts/validate_package.py",
    "scripts/theme-bootstrap.js", "scripts/site-controls.js", "scripts/site-controls.d.ts", "scripts/smoke-deployments.mjs",
    "scripts/consumer-release.mjs", "scripts/conformance-runner.mjs",
    "conformance/contract.json", "conformance/contract.schema.json", "conformance/manifest.schema.json",
    ".github/workflows/consumer-design-system-sync.yml", ".github/workflows/consumer-conformance.yml",
    ".github/workflows/consumer-candidate-gate.yml",
    "styles/index.css", "styles/foundations.css", "styles/site-identity.css",
    "styles/theme-control.css", "styles/content.css", "styles/content-guard.css", "styles/content-primitives.css",
}
RAW_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\(")
TOKEN_DEFINITION = re.compile(r"(--jl-[a-z0-9-]+)\s*:")
TOKEN_USE = re.compile(r"var\((--jl-[a-z0-9-]+)")
IMPORT = re.compile(r"@import\s+[\"']([^\"']+)[\"']")
RULE_ID = re.compile(r"^DS-[A-Z0-9]+-[0-9]{3}$")
COMPONENT_HOOK_PREFIXES = (
    "--jl-actions-", "--jl-button-", "--jl-callout-",
    "--jl-empty-state-", "--jl-table-region-", "--jl-dialog-",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(content: str, fragments: tuple[str, ...], label: str) -> None:
    for fragment in fragments:
        if fragment not in content:
            fail(f"{label} is incomplete: {fragment}")


def validate_export(value: object, label: str) -> None:
    if isinstance(value, str):
        if not value.startswith("./") or not (ROOT / value[2:]).is_file():
            fail(f"invalid export {label}: {value}")
        return
    if isinstance(value, dict):
        for condition, target in value.items():
            validate_export(target, f"{label}.{condition}")
        return
    fail(f"invalid export {label}")


def validate_manifest_schema() -> None:
    schema = read_json(ROOT / "conformance" / "manifest.schema.json")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail("consumer manifest schema is not draft 2020-12")
    if schema.get("additionalProperties") is not False:
        fail("consumer manifest schema must reject unknown top-level properties")
    required = set(schema.get("required", []))
    if required != {"schemaVersion", "product", "rules"}:
        fail("consumer manifest schema required fields drifted")
    products = set(schema.get("properties", {}).get("product", {}).get("enum", []))
    if products != {"portfolio", "network", "rolepacket"}:
        fail("consumer manifest schema products drifted")
    evidence = schema.get("$defs", {}).get("evidence", {})
    types = set(evidence.get("properties", {}).get("type", {}).get("enum", []))
    if types != {"file-exists", "contains", "not-contains", "matches", "json-equals", "json-matches"}:
        fail("consumer manifest evidence types drifted")


def validate_conformance(token_version: str) -> None:
    contract = read_json(ROOT / "conformance" / "contract.json")
    schema = read_json(ROOT / "conformance" / "contract.schema.json")
    if contract.get("schemaVersion") != "1.0.0":
        fail("conformance contract schema version drifted")
    if contract.get("designSystemVersion") != token_version:
        fail("conformance contract design-system version drifted")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail("conformance contract schema is not draft 2020-12")
    validate_manifest_schema()
    rules = contract.get("rules")
    if not isinstance(rules, list) or not rules:
        fail("conformance contract has no rules")
    ids: set[str] = set()
    products = {"portfolio", "network", "rolepacket"}
    for rule in rules:
        rule_id = str(rule.get("id", ""))
        if not RULE_ID.fullmatch(rule_id) or rule_id in ids:
            fail(f"invalid or duplicate conformance rule: {rule_id}")
        ids.add(rule_id)
        if rule.get("severity") not in {"required", "advisory", "manual"}:
            fail(f"invalid conformance severity: {rule_id}")
        applies_to = rule.get("appliesTo")
        if not isinstance(applies_to, list) or not applies_to or not set(applies_to) <= products:
            fail(f"invalid conformance products: {rule_id}")
        source = str(rule.get("source", ""))
        if not source.startswith("docs/DESIGN-SYSTEM.md#"):
            fail(f"conformance rule lacks a canonical source: {rule_id}")

    runner = (ROOT / "scripts" / "conformance-runner.mjs").read_text(encoding="utf-8")
    require(runner, (
        "function confined(root, value, label)", "relative(root, destination)",
        "--strict-manual", "design-system.conformance.json", "conformance/contract.json",
        "validateEvidenceShape", "validateManifest", "readProvenance",
        "json-equals", "json-matches", "not-contains", "manual-pending",
        "sourceCommit", "consumerCommit", "report.json", "report.md",
        "blockingFailures", "process.exitCode = 1",
    ), "conformance runner")
    if any(fragment in runner for fragment in ("child_process", "exec(", "spawn(")):
        fail("conformance runner must not execute consumer commands")

    workflow = (ROOT / ".github" / "workflows" / "consumer-conformance.yml").read_text(encoding="utf-8")
    require(workflow, (
        "workflow_call:", "contents: read", "conformance-command:",
        "Run design-system conformance", "if: always()", "actions/upload-artifact@",
        "path: design-system-conformance", "if-no-files-found: error",
    ), "reusable consumer conformance workflow")

    candidate = (ROOT / ".github" / "workflows" / "consumer-candidate-gate.yml").read_text(encoding="utf-8")
    require(candidate, (
        "name: Consumer candidate gate", "pull_request:", "workflow_dispatch:",
        "CANDIDATE_SHA", "repository: JohnnyZLi/Website", "repository: JohnnyZLi/Network-Diagnostics-Suite",
        "repository: JohnnyZLi/RolePacket", "npm run design-system:sync", "npm run design-system:integration",
        "npm run design-system:conformance", "npm run cloud:deploy:dry",
    ), "cross-consumer candidate gate")
    if "persist-credentials: true" in candidate:
        fail("cross-consumer candidate gate persists checkout credentials")


def validate() -> None:
    package = read_json(ROOT / "package.json")
    version = read_json(ROOT / "version.json")
    token_version = read_json(TOKENS_JSON)["$extensions"]["com.johnnyli.meta"]["version"]

    if package.get("name") != EXPECTED_NAME or version.get("name") != EXPECTED_NAME:
        fail("unexpected package name")
    if package.get("private") is not False:
        fail("package must remain installable")
    if package.get("version") != token_version or version.get("version") != token_version:
        fail("package, version metadata, and token source must match")
    if set(package.get("files", [])) != EXPECTED_FILES:
        fail("package files drifted from the approved contract")
    if package.get("exports") != EXPECTED_EXPORTS:
        fail("package exports drifted from the approved contract")
    for label, value in package["exports"].items():
        validate_export(value, label)

    missing_paths = sorted(path for path in EXPECTED_FILES | RELEASE_ADDITIONS if not (ROOT / path).is_file())
    if missing_paths:
        fail("package references missing files: " + ", ".join(missing_paths))

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
    missing_tokens = sorted(name for name in used - defined if not name.startswith(COMPONENT_HOOK_PREFIXES))
    if missing_tokens:
        fail("shared styles use undefined tokens: " + ", ".join(missing_tokens))

    identity = (STYLE_ROOT / "site-identity.css").read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", identity):
        fail("global header must remain unlayered")
    require(identity, (
        ".jl-site-switcher__button", ".jl-header-menu-toggle",
        ".jl-global-header__nav.jl-header-menu--open",
    ), "shared header")

    controls = (ROOT / "scripts" / "site-controls.js").read_text(encoding="utf-8")
    require(controls, (
        "export const OWNED_SITES", "export const THEME_PREFERENCES",
        "export function installThemeControl", "export function installDisclosureMenu",
        "export function installSiteSwitcher", "export function installHeaderMenu",
        'event.key === "ArrowDown"', 'event.key === "ArrowUp"',
        'event.key === "Escape"', 'event.key === "Home"', 'event.key === "End"',
    ), "shared site controls")
    if "http://" in controls:
        fail("shared site controls contain an insecure URL")

    bootstrap = (ROOT / "scripts" / "theme-bootstrap.js").read_text(encoding="utf-8")
    require(bootstrap, (
        "prefers-color-scheme: dark", "data-theme", "data-theme-preference",
        "Domain=.johnnyli.dev", "beforeprint", "afterprint", "jl-theme-change",
    ), "pre-paint theme bootstrap")
    theme_css = (STYLE_ROOT / "theme-control.css").read_text(encoding="utf-8")
    require(theme_css, (
        ".jl-theme-menu-item", ".jl-theme-options", "aria-pressed",
        "@media (forced-colors: active)",
    ), "shared theme control")

    primitives = (STYLE_ROOT / "content-primitives.css").read_text(encoding="utf-8")
    if re.search(r"^\s*@layer\b", primitives):
        fail("content primitives must remain unlayered")
    require(primitives, (
        ".jl-actions {", "display: flex;", "flex-wrap: wrap;",
        ".jl-button {", "display: inline-flex;", "align-items: center;",
        "justify-content: center;", "text-decoration: none;", "cursor: pointer;",
        "--jl-button-min-height", "--jl-button-hover-background",
        ".jl-button--compact", ".jl-button--danger",
        "--jl-callout-padding", ".jl-callout--info",
        "--jl-empty-state-padding", "--jl-table-region-border-width",
        ".jl-dialog {", "z-index: var(--jl-z-dialog);", ".jl-dialog::backdrop",
        ".jl-dialog__surface", ".jl-dialog__title", ".jl-dialog__message",
        ".jl-dialog__actions", "--jl-dialog-compact-width",
        "@media (forced-colors: active)",
    ), "standalone adaptable content primitives")

    consumer = (ROOT / "scripts" / "consumer-release.mjs").read_text(encoding="utf-8")
    require(consumer, (
        'const REPOSITORY = "JohnnyZLi/Web-Design-System"',
        "function localPath(value)", "relation.startsWith(\"..\")",
        "export async function resolveConsumerRelease", "design-system.lock.json",
        "api.github.com/repos/${REPOSITORY}/commits/main", "raw.githubusercontent.com",
        "manifest.dependencies[PACKAGE]", "github:${REPOSITORY}#${sourceCommit}",
    ), "constrained consumer release helper")
    if any(fragment in consumer for fragment in ("child_process", "exec(", "spawn(")):
        fail("consumer release helper must not execute arbitrary commands")

    workflow = (ROOT / ".github" / "workflows" / "consumer-design-system-sync.yml").read_text(encoding="utf-8")
    require(workflow, (
        "workflow_call:", "permissions:", "contents: write", "pull-requests: write",
        "npm run design-system:update", "npm run design-system:sync",
        "mapfile -t tracked_paths", 'git add -- "${tracked_paths[@]}"',
        "automation/design-system-update", "gh pr create --draft",
    ), "reusable consumer sync workflow")

    index = (STYLE_ROOT / "index.css").read_text(encoding="utf-8")
    imports = [
        '@import "./content.css";',
        '@import "./content-guard.css";',
        '@import "./content-primitives.css";',
    ]
    positions = [index.index(item) for item in imports]
    if positions != sorted(positions):
        fail("content primitives must load after content and content guard")

    smoke = (ROOT / "scripts" / "smoke-deployments.mjs").read_text(encoding="utf-8")
    require(smoke, (
        "https://johnnyli.dev", "https://network.johnnyli.dev",
        "https://rolepacket.johnnyli.dev", "ROLEPACKET_ACCESS_CLIENT_ID",
        "CF-Access-Client-Id", "Deployed-site smoke checks passed.",
    ), "deployment smoke checks")

    validate_conformance(token_version)
    if f"Design-system version: {token_version} */" not in TOKENS_CSS.read_text(encoding="utf-8"):
        fail("generated token CSS version header drifted")
    print(f"Package validation passed for {EXPECTED_NAME} v{token_version}.")


def release() -> None:
    validate()
    version = read_json(TOKENS_JSON)["$extensions"]["com.johnnyli.meta"]["version"]
    archive = ROOT / "dist" / f"Johnny_Li_Web_Design_System_v{version}.zip"
    if not archive.is_file():
        fail("base release archive is missing; run make release")
    prefix = Path(f"Web-Design-System-v{version}")
    with zipfile.ZipFile(archive, "a", zipfile.ZIP_DEFLATED) as output:
        existing = set(output.namelist())
        for relative in sorted(RELEASE_ADDITIONS):
            destination = (prefix / relative).as_posix()
            if destination not in existing:
                output.write(ROOT / relative, destination)
    print(f"Added package contract to {archive.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="validate", choices=["validate", "release"])
    args = parser.parse_args()
    {"validate": validate, "release": release}[args.command]()


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, TypeError, ValueError, zipfile.BadZipFile) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
