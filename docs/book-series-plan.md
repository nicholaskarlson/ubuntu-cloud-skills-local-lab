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

## Book 2 — Your First Ubuntu Server Lab

Practice VPS-style skills safely at home before renting a cloud server.

The default path is LAN-first: one Ubuntu client machine connects to one Ubuntu server machine on the same private network. The server machine can be an Ubuntu laptop, old desktop, mini PC, Raspberry Pi-style Linux box, VM, or other local Ubuntu host.

Core skills: SSH readiness, users, updates, firewall posture, service inspection, logs, local-network deployment, smoke checks, backup, restore, cleanup, and safe receipts.

A rented VPS remains an optional migration path, not a requirement for the core Book 2 learning path.

Planned release tag:

```text
book2-v1.0.0
```

Current scaffold: Book 2 now has a LAN-first pivot, safety boundary, LAN lab guide, optional VPS checklist, and safe input-check targets. No live SSH, deployment, firewall mutation, DNS, HTTPS, router port-forwarding, or provider automation has been added yet.

## Book 3 — Publish Your Creator Website on Ubuntu

Grow the static creator site: content files, simple site generation, book/product/resource pages, local preview, link checking, accessibility smoke checks, deploy first to the LAN server lab, optional public publishing later, maintenance receipts, backup, and restore.

Planned release tag:

```text
book3-v1.0.0
```

## Book 4 — Build a DIY Digital Bookstore

Add bookstore-shaped workflows carefully: product metadata, static product pages, protected or semi-protected download concepts, order/fulfillment concepts, receipt records, backup, restore, and safer customer-data boundaries.

The core path should remain local-first and should not require real customer data or real public hosting.

Planned release tag:

```text
book4-v1.0.0
```

## Book 5 — Stripe Checkout for Independent Creators

Add payments only when the reader is ready: hosted checkout, test mode first, local webhook practice, webhook verification, idempotent fulfillment, safe receipt/log design, no card storage, refund/support workflow, secret scanning/checks, and a test-mode preflight.

Planned release tag:

```text
book5-v1.0.0
```

## Book 6 — Cloud Skills for Ubuntu Creators

Add cloud migration skills carefully and portably: provider comparison, public hosting options, object storage concepts, named profiles where relevant, IAM/least-privilege thinking where relevant, free-tier-aware practice, safe cleanup, receipts, cost awareness, and no secret leakage.

AWS may appear as one optional provider path. It should not be required for the core series promise.

Planned release tag:

```text
book6-v1.0.0
```

## Boundary for future bonus software

A future separate repo may teach AI-assisted creator/builder workflows, React component thinking, debugging, diff review, accessibility, shipping small, and portfolio case-study habits.

That bonus app should stay separate from this Ubuntu Cloud Skills repo unless there is a clear reason to connect them later.
