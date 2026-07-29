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
- Human review for obvious fixture, loading, or measurement errors

The first report establishes a reference point. It does not become a blocking budget automatically. Repeated runs should be used to estimate normal runner variance before regression limits are adopted.

## Consumer implementations

### Website

The portfolio recorder serves the static site locally, discovers every HTML page, inventories production files, records desktop and mobile samples, and uploads JSON and Markdown reports. Its public workflow runs for relevant pull requests, manual dispatch, and a monthly schedule.

### Network Diagnostics

The Network Diagnostics recorder builds the production Vite application, inventories `dist`, and measures the idle browser application at desktop and mobile widths. Application-shell performance remains separate from throughput and latency measurements. Its public workflow runs for relevant pull requests, manual dispatch, and a monthly schedule.

### RolePacket

The RolePacket recorder reuses the production client build, measures deterministic authenticated fixtures at desktop and mobile widths, inventories generated client assets, and uploads performance evidence beside the functional, visual, conformance, and security results from its repository-scoped macOS workflow.

## Interpretation

These reports can show whether built assets, resource count, DOM complexity, layout shift, or main-thread work changed materially on the same controlled runner. They are not real-user field data and do not replace actual 200 percent zoom, forced-colors, assistive-technology, or product-specific accuracy review.

## Review and budget adoption

For each product:

1. Generate the initial report on a clean immutable commit.
2. Rerun on the same environment to estimate normal variance.
3. Review the largest assets and any missing or unstable browser metric.
4. Record the accepted reference report or durable summary.
5. Adopt blocking budgets only for stable values or timing changes with sufficient tolerance.
6. Re-record after intentional architecture, framework, or rendering-state changes.

Until reports are generated and reviewed, `DS-PERF-001` remains `manual-pending`. Adding a script or workflow alone does not prove that a product met an approved performance target.
