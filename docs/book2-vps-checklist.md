# Book 2 Optional VPS Checklist

This file keeps the earlier Book 2 VPS checklist visible, but the Book 2 default path has changed.

Book 2 is now LAN-first. A rented VPS is optional.

The core path should teach the same habits on a private local network before requiring DigitalOcean, AWS, another paid provider, a domain name, public DNS, HTTPS, or public SSH exposure.

For backward compatibility with the earlier scaffold: no live VPS automation is included yet.

## Before renting a VPS

Confirm that the reader understands:

- Book 1 local workflow,
- Book 2 LAN server workflow,
- `make verify`,
- `make doctor`,
- `make book2-doctor`,
- receipts,
- local backup and restore,
- Git basics,
- what an SSH key is,
- why SSH private keys must stay private,
- that a VPS can cost money while it exists,
- that public servers need more care than local machines, and
- that a provider dashboard is where paid resources are usually destroyed.

## Minimum optional VPS expectations

A Book 2 optional VPS should be:

- Ubuntu LTS,
- reachable by SSH,
- created from a provider dashboard the reader understands,
- small and inexpensive,
- disposable for practice,
- not used for private customer data,
- not used for payment handling,
- not used as the only copy of important files.

## Optional migration phases

If a reader chooses a VPS later, the path should still be phased:

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

A future VPS or public-hosting path can support two stages:

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
- LAN-first SSH inspection,
- deployment dry-run,
- LAN deployment,
- smoke test,
- server log receipt,
- backup,
- restore drill,
- cleanup checklist,
- sample safe receipts,
- tests,
- release checklist, and
- `book2-v1.0.0` tagging instructions.

Provider-specific public deployment can be an appendix or optional migration path, not a requirement for Book 2 completion.
