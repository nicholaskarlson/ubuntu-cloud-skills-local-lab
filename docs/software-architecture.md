# Software Architecture

This repo is intentionally modest. It should feel like a teaching lab first and an application platform second.

The architecture grows in layers:

```text
Book 1: local files + Docker Compose + receipts + backup/restore
Book 2: same habits on a real Ubuntu VPS
Book 3: creator website content and deploy rhythm
Book 4: bookstore-shaped product and download workflows
Book 5: Stripe Checkout test-mode payment workflow
Book 6: AWS CLI and S3 practice with cleanup and cost awareness
```

## Current Book 1 layer

Book 1 contains:

- `public/` — local creator-site files
- `compose.yaml` — the local web lab definition
- `Makefile` — the reader-friendly command surface
- `scripts/` — small shell helpers for inspection, receipts, backup, and restore
- `receipts/samples/` — safe example receipts
- `lessons/` — guided reader lessons
- `tests/` — repository contract tests

This layer teaches the core proof-first loop:

```text
edit files -> start service -> inspect -> test -> save evidence -> restore/cleanup
```

## Command surface principle

Readers should mainly use `make` targets, not memorize long commands.

Good targets should be:

- named after the reader’s task,
- inspectable in the Makefile,
- safe by default,
- documented in the lessons, and
- covered by tests when they become part of the contract.

## Script principle

Scripts should be boring and readable.

Prefer:

- Bash with `set -euo pipefail` for small system tasks,
- Python standard library for repository contract checks,
- plain text receipts,
- explicit cleanup steps,
- clear error messages, and
- small scripts that can be read in one sitting.

Avoid:

- hidden background services,
- unexplained provider-specific tools,
- secrets in command examples,
- scripts that mutate cloud resources without a dry-run or preflight mindset,
- payment or customer-data code before the reader has learned the safety model, and
- clever abstractions that make the lesson harder to inspect.

## Release layers

Each book should add a bounded layer and then receive a stable tag.

The intended sequence is:

1. add small docs/scripts/tests on a development branch,
2. run `make verify`,
3. run `make doctor`,
4. run any lesson-specific smoke checks,
5. document the reader path,
6. tag the book release when the code matches the manuscript, and
7. leave the tag alone after publication.

## Safety boundaries by layer

Book 1 should stay local.

Book 2 can introduce public server exposure, but should keep the domain, firewall, HTTPS, logs, backup, restore, and cleanup workflow explicit.

Book 3 can add real website maintenance, but should still be source-controlled and locally previewable.

Book 4 can introduce digital-product workflows, but should avoid careless customer-data handling.

Book 5 can introduce Stripe, but should use hosted checkout, test mode first, webhook verification, idempotent fulfillment, no card storage, and safe receipts.

Book 6 can introduce AWS, but should use named profiles, least-privilege thinking, cost awareness, and cleanup receipts.
