# Book 2 VPS Checklist

This checklist defines the planned Book 2 server path before any live automation is added.

It is a teaching checklist, not a provider signup guide.

## Before creating a VPS

Confirm that the reader understands:

- Book 1 local workflow,
- `make verify`,
- `make doctor`,
- receipts,
- local backup and restore,
- Git basics,
- what an SSH key is,
- why private keys must stay private,
- that a VPS can cost money while it exists, and
- that public servers need more care than local containers.

## Minimum server expectations

A Book 2 server should be:

- Ubuntu LTS,
- reachable by SSH,
- created from a provider dashboard the reader understands,
- small and inexpensive,
- disposable for practice,
- not used for private customer data,
- not used for payment handling,
- not used as the only copy of important files.

## Planned setup phases

Book 2 should be developed in phases:

1. Readiness and safety boundary.
2. SSH connection check.
3. Non-root user and update habit.
4. Firewall inspection and basic posture.
5. Web server installation.
6. Static site deployment.
7. Smoke test.
8. Log inspection.
9. Safe receipt creation.
10. Backup archive and checksum.
11. Restore drill.
12. Cleanup and cost reminder.
13. Release tag.

## Domain and HTTPS path

Book 2 can support two paths:

- IP-only HTTP practice for early learning.
- Domain-based HTTPS practice once DNS is ready.

The HTTPS path should not be the first live step. The reader should first understand what is being served and how to stop it.

## Cost-safety reminders

Book 2 should repeatedly remind readers:

- a VPS can keep billing while it exists,
- deleting local repo files does not delete a VPS,
- shutting down a service is not always the same as destroying a VPS,
- a provider dashboard is usually where billing resources are destroyed,
- keep screenshots and notes safe, but do not commit credential or billing details.

## Done criteria for Book 2 software

Book 2 software is not complete until it includes:

- clear docs,
- safe local verification,
- explicit server input checks,
- SSH inspection,
- deployment dry-run,
- public deployment,
- smoke test,
- server log receipt,
- backup,
- restore drill,
- cleanup checklist,
- sample safe receipts,
- tests,
- release checklist, and
- `book2-v1.0.0` tagging instructions.
