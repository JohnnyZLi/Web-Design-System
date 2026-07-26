# Changelog

## 1.3.2 — 2026-07-25

- Changed release packaging from repository traversal to explicit file allowlists.
- Added validation for CSS-specific token overrides and malicious-syntax regression checks.
- Expanded public-safety checks for sensitive filenames, credentials, private IP addresses, local home paths, and Cloudflare identifiers.
- Pinned GitHub Actions to immutable commit SHAs and disabled persisted checkout credentials.
- Added workflow concurrency and a five-minute timeout.
- Added Dependabot updates for pinned GitHub Actions.
- Added a security policy and private vulnerability-reporting guidance.
- Added a versioned package contract for consuming tokens and shared CSS across repositories.
- Added shared accessibility foundations and site-identity styling without product-specific components.
- Added package export, token-reference, raw-color, import, and version-drift validation.
- Corrected the specimen version and aligned its Network Diagnostics profiles with the public application.

## 1.3.1 — 2026-07-25

- Converted atomic tokens to DTCG 2025.10 structure.
- Added namespaced CSS extensions for fluid values.
- Added generated CSS, executable validation, release generation, and local serving.
- Added GitHub Actions and CODEOWNERS.
- Removed the committed combined specification; releases generate it into `dist/`.
- Consolidated the public documentation into one core specification and one migration file.
- Moved detailed product logic out of the public design-system core.
- Removed private repository commit snapshots and private source paths.
- Marked unmeasured performance limits as pending baselines.
- Expanded the specimen with patterns adapted from all three sites.
- Added an all-rights-reserved license while public licensing remains undecided.

## 1.3.0 — 2026-07-25

- Split the original monolithic document into a package with tokens, tooling, governance, and a specimen.
