# Software Architecture

This repo is intentionally modest. It should feel like a teaching lab first and an application platform second.

The architecture grows in layers:

```text
Book 1: local files + Docker Compose + receipts + backup/restore
Book 2: same habits on a LAN-first Ubuntu server lab
Book 3: creator website content and deploy rhythm, local first
Book 4: bookstore-shaped product and download workflows, local first
Book 5: Stripe Checkout test-mode payment workflow
Book 6: portable cloud migration skills, with AWS as optional rather than required
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

## Current Book 2 LAN-first layer

Book 2 has pivoted to a LAN-first server lab.

The default model is:

```text
Ubuntu client machine -> SSH later -> Ubuntu server machine on the same private LAN
```

The server machine can be a spare laptop, old desktop, mini PC, VM, or other Ubuntu host. A rented VPS remains optional later, but is not required for the core Book 2 path.

The current layer adds:

- the Book 2 companion-code note,
- the LAN server lab guide,
- the server safety boundary,
- the optional VPS checklist,
- the first Book 2 lesson,
- a `book2/env.example` file for local non-secret settings,
- safe Book 2 readiness and input-check scripts,
- Makefile targets that do not connect to a server, and
- contract tests that keep the pivot visible in the repo map and doctor workflow.

This is deliberate. The repo should define the reader path before adding commands that connect to, deploy to, or mutate another machine.

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
- router port forwarding in the beginner path,
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

Book 2 should stay LAN-first by default. It can teach VPS-style habits without public exposure, router port forwarding, paid hosting, or provider-specific accounts.

Book 3 can add real website maintenance, but should still be source-controlled and locally previewable.

Book 4 can introduce digital-product workflows, but should avoid careless customer-data handling.

Book 5 can introduce Stripe, but should use hosted checkout, test mode first, webhook verification, idempotent fulfillment, no card storage, and safe receipts.

Book 6 can introduce cloud providers, but should use named profiles where relevant, least-privilege thinking, cost awareness, and cleanup receipts. AWS should be optional, not required for the core series.
