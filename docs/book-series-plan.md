# Ubuntu Cloud Skills for Independent Creators

Working series plan for NEKpress.ca.

This repository should grow as one coherent proof-first software line, not as disconnected demos. Each book adds one carefully bounded layer, preserves the habits from earlier books, and receives a stable book-specific tag when the companion code is ready for publication.

For the fuller implementation roadmap, see [Series Roadmap](series-roadmap.md). For release discipline, see [Release and Tagging Policy](release-and-tagging-policy.md).

## Book 1 — Your First Local Cloud Lab with Ubuntu and Docker

Local Docker lab, static creator page, logs, receipts, backup, restore, and cleanup.

Reader promise: learn cloud-style habits without a paid cloud account.

Release tag:

```text
book1-v1.0.0
```

## Book 2 — Your First Ubuntu Cloud Server

Move the same habits to a real Ubuntu VPS: SSH keys, non-root user, updates, firewall, Caddy or Nginx, public IP or domain, HTTPS, deploy from Git, server logs, server smoke test, server backup, restore drill, cost cleanup, and deployment receipts.

Planned release tag:

```text
book2-v1.0.0
```

Current scaffold: Book 2 planning docs and Lesson 4 now define the safety boundary before live VPS automation is added.

## Book 3 — Publish Your Creator Website on Ubuntu

Grow the static creator site: content files, simple site generation, book/product/resource pages, local preview, link checking, accessibility smoke checks, deploy to VPS, maintenance receipts, backup, and restore.

Planned release tag:

```text
book3-v1.0.0
```

## Book 4 — Build a DIY Digital Bookstore

Add bookstore-shaped workflows carefully: product metadata, static product pages, protected or semi-protected download concepts, order/fulfillment concepts, receipt records, backup, restore, and safer customer-data boundaries.

Planned release tag:

```text
book4-v1.0.0
```

## Book 5 — Stripe Checkout for Independent Creators

Add payments only when the reader is ready: hosted checkout, test mode first, webhook verification, idempotent fulfillment, safe receipt/log design, no card storage, refund/support workflow, secret scanning/checks, and a test-mode preflight.

Planned release tag:

```text
book5-v1.0.0
```

## Book 6 — AWS Skills for Ubuntu Creators

Add provider-specific cloud skills carefully: AWS CLI, named profiles, IAM basics, S3, free-tier-aware practice, safe cleanup, receipts, cost awareness, and no secret leakage.

Planned release tag:

```text
book6-v1.0.0
```

## Boundary for future bonus software

A future separate repo may teach AI-assisted creator/builder workflows, React component thinking, debugging, diff review, accessibility, shipping small, and portfolio case-study habits.

That bonus app should stay separate from this Ubuntu Cloud Skills repo unless there is a clear reason to connect them later.
