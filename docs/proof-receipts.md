# Proof Receipts

A proof receipt is a small text record that shows what happened on your machine.

This project uses receipts to build careful habits. Instead of merely trusting that a command worked, you save a short record of the command, the result, and any cleanup step.

## What receipts are for

Receipts help you prove that:

- the expected tools were installed,
- the local lab started,
- the local web page responded,
- logs were available,
- cleanup happened, and
- you did not need a paid cloud account for the local lesson.

## What receipts are not for

Receipts are not a place for secrets.

Never put these in a receipt:

- passwords,
- API tokens,
- SSH private keys,
- cloud credentials,
- payment credentials,
- private customer data,
- full account numbers, or
- screenshots of credential pages.

## Where receipts go

Local receipts go in:

```text
receipts/
```

Sample receipts go in:

```text
receipts/samples/
```

The repository ignores ordinary `receipts/*.txt` files because your receipts are local evidence, not source code.

## How to save a receipt

Run the Docker version receipt:

```bash
make receipt-version
```

Run the local web smoke test and save a receipt:

```bash
make lab-smoke-receipt
```

Write a short manual note:

```bash
make receipt-note
```

## What a good receipt looks like

A good receipt is short and plain:

```text
Local web smoke-test receipt

Created: 2026-05-22T09:00:00-07:00

The local site responded at http://localhost:8080.
The web service was running in Docker Compose.
The lab was stopped afterward with make down.
```

The goal is not to make a beautiful report. The goal is to leave behind enough evidence that you can understand what you did later.
