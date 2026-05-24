# Series Roadmap

This repository is the continuing companion repo for the NEKpress.ca series **Ubuntu Cloud Skills for Independent Creators**.

The line should grow slowly, with one stable software layer per book. The goal is not to impress experienced operators with clever automation. The goal is to help careful beginners build practical habits they can inspect, test, back up, restore, and explain.

## Core promises

- Local first.
- Proof first.
- Safe receipts.
- No secrets in Git.
- No secrets in receipts.
- No paid cloud required for Book 1.
- No Docker Pro requirement for readers.
- Provider portable.
- Inspect before guessing.
- Small steps.
- Clean rollback path.
- Test before trusting.
- Backup plus restore, not backup alone.
- Stop what you start.
- Add public exposure, payment, customer data, and vendor-specific services only when the reader is ready.

## Book-by-book roadmap

| Book | Software layer | Reader result | Release tag |
| --- | --- | --- | --- |
| 1 | Local Docker lab | Run, inspect, back up, restore, and stop a local creator web lab | `book1-v1.0.0` |
| 2 | Ubuntu VPS foundation | Move the same proof-first habits to a real server safely | `book2-v1.0.0` |
| 3 | Creator website | Maintain and deploy a useful creator site from source-controlled content | `book3-v1.0.0` |
| 4 | DIY digital bookstore | Model products, downloads, fulfillment records, and safer data boundaries | `book4-v1.0.0` |
| 5 | Stripe Checkout | Use hosted checkout, test mode, webhooks, idempotent fulfillment, and safe logs | `book5-v1.0.0` |
| 6 | AWS skills | Practice AWS CLI, IAM basics, S3, cleanup, and cost awareness safely | `book6-v1.0.0` |

## What stays stable

Each book release should preserve:

- the exact code tag named by the book,
- verification commands that still work for that tag,
- sample receipts that do not contain secrets,
- cleanup steps,
- restore practice where files or data are involved, and
- documentation that tells readers whether they should use a tag or the evolving `main` branch.

## What can evolve on main

The `main` branch can continue to improve as the series grows. It can add new docs, scripts, tests, and lessons for later books.

However, new work should not quietly change the meaning of an already-published book tag. If a book has shipped with a tag, that tag is the reader’s stable companion-code version.

## Book 1 boundary

Book 1 remains a local lab. It should not require:

- a paid cloud account,
- a domain name,
- public DNS,
- Stripe,
- AWS,
- Docker Pro,
- a customer database, or
- real public exposure.

Later books may add those topics, but only after the repo has made the safety boundary clear.

## First foundation commands

Use these before starting a new implementation increment:

```bash
make verify
make doctor
make repo-map
make series-status
```

These commands keep the project aligned with the NEKpress.ca style: practical, calm, reader-focused, proof-first, beginner-safe, test-driven, and conservative around secrets, public exposure, payments, and customer data.
