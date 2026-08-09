# Consumer performance baselines

Performance evidence belongs to each product repository because the products have different rendering models, assets, and runtime responsibilities. The Web Design System defines a common evidence standard rather than one universal timing threshold.

## Evidence standard

A consumer baseline is recorded for one immutable consumer commit when it includes:

- A production-equivalent build or static artifact inventory
- Raw and gzip-compressed asset totals
- Provenance for the largest generated assets
- At least three browser samples at desktop and compact or mobile widths
- Median navigation, paint, layout-shift, long-task, transfer, resource-count, and DOM-size measurements
- The runner environment, Node.js version, viewport, motion preference, and application fixture or state
- A JSON report and a human-readable report
- An assertion that the intended application fixture or state actually rendered before timings are accepted
- Failure on uncaught browser page errors instead of silently recording a partial shell
- Human review for obvious fixture, loading, or measurement errors

The first valid reviewed report establishes a reference point. It does not become a blocking budget automatically. Repeated runs should be used to estimate normal runner variance before regression limits are adopted.

## Consumer implementations

### Website

The portfolio recorder serves the static site locally, discovers every HTML page, inventories production files, records desktop and mobile samples, and uploads JSON and Markdown reports. Its public workflow runs for relevant pull requests, manual dispatch, and a monthly schedule.

### Network Diagnostics

The Network Diagnostics recorder builds the production Vite application, inventories `dist`, and measures the idle browser application at desktop and mobile widths. Application-shell performance remains separate from throughput and latency measurements. Its public workflow runs for relevant pull requests, manual dispatch, and a monthly schedule.

### RolePacket

The RolePacket recorder reuses the production client build, measures a deterministic authenticated workspace at desktop and mobile widths, inventories generated client assets, and uploads performance evidence beside the functional, visual, conformance, and security results from its repository-scoped macOS workflow. The recorder now uses a schema-current profile fixture, requires the authenticated `.app-shell` and a nontrivial DOM before accepting measurements, and fails on uncaught browser page errors.

## Interpretation

These reports can show whether built assets, resource count, DOM complexity, layout shift, or main-thread work changed materially on the same controlled runner. They are not real-user field data and do not replace actual 200 percent zoom, forced-colors, assistive-technology, or product-specific accuracy review.

A green workflow is not sufficient evidence when the fixture itself is wrong. Suspicious values such as an unexpectedly tiny DOM, missing paint metrics, or an unexpected application state must be investigated before manual performance approval is recorded.

## Review and budget adoption

For each product:

1. Generate the initial report on a clean immutable commit.
2. Prove the intended application state rendered and that no uncaught browser error invalidated the sample.
3. Rerun on the same environment to estimate normal variance.
4. Review the largest assets and any missing or unstable browser metric.
5. Record the accepted reference report or durable summary.
6. Adopt blocking budgets only for stable values or timing changes with sufficient tolerance.
7. Re-record after intentional architecture, framework, or rendering-state changes.

### Current acceptance record

The Website and Network Diagnostics initial reports were generated and reviewed on 2026-07-29 and remain accepted engineering references. Both products also produced fresh reports after their v1.9.0 appearance/header work, satisfying the re-record requirement for the changed rendering state. Their `DS-PERF-001` declarations remain `manual-passed`.

The RolePacket report originally accepted on 2026-07-29 was invalidated during the 2026-08-09 close-out audit. Its hand-written profile mock predated the current `CandidateProfile` shape, so the application failed before the authenticated workspace rendered; the recorder silently measured a partial shell with 18 DOM nodes and no Largest Contentful Paint. The corrected recorder produced a full authenticated workspace with 99 DOM nodes and nonzero Largest Contentful Paint at both audited viewports, but that corrected report still requires human review. RolePacket therefore records `DS-PERF-001` as `manual-pending` rather than preserving the stale approval.

Accepted reports are engineering references, not universal field-performance guarantees or rigid blocking budgets.
