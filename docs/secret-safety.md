# Secret Safety

This repo teaches cloud, publishing, backup, restore, payment, and provider-specific habits. Those topics can eventually touch sensitive information.

The rule is simple:

Do not put secrets in Git, receipts, logs, examples, screenshots, support requests, or lesson output.

## Never commit these

Never commit:

- passwords,
- API tokens,
- SSH private keys,
- cloud access keys,
- Stripe secrets,
- webhook signing secrets,
- database passwords,
- customer names tied to orders,
- private customer email lists,
- payment details,
- full account numbers, or
- screenshots of credential pages.

## Receipts must be safe

Receipts should prove what happened without exposing private material.

Good receipt content:

```text
Command: make lab-smoke
Result: local web lab responded at http://localhost:8080
Cleanup: make down completed
```

Bad receipt content:

```text
STRIPE_SECRET_KEY=...
AWS_SECRET_ACCESS_KEY=...
-----BEGIN OPENSSH PRIVATE KEY-----
```

## Logs must be treated carefully

Logs can accidentally contain sensitive information. Before saving or sharing logs, inspect them.

For later books, any workflow that introduces public servers, payments, cloud accounts, or customer data should include a preflight reminder about safe logs and safe receipts.

## Environment files

If later books need local environment variables, use ignored local files such as:

```text
.env.local
```

and provide safe examples such as:

```text
.env.example
```

Examples should use fake placeholder values only.

## When in doubt

If a value grants access, identifies a private account, exposes a private person, or could be abused if copied, do not save it in the repo or in a receipt.

Use the proof-first rule with a safety filter:

```text
prove what happened, but do not reveal private access.
```
