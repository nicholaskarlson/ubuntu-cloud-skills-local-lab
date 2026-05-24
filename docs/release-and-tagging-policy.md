# Release and Tagging Policy

Books are stable. Repositories evolve.

This repository uses book-specific release tags so a reader can match the code to the printed or Kindle book in front of them.

## Current stable Book 1 tag

Book 1 companion-code tag:

```text
book1-v1.0.0
```

Exact Book 1 code commit:

```text
88ff6452419bd027f31cb6e7a6799f5ed0695765
```

Book 1 readers should use that tag if they want the exact companion-code version documented in the book.

## Planned tag pattern

Use one stable tag per book release:

```text
book1-v1.0.0
book2-v1.0.0
book3-v1.0.0
book4-v1.0.0
book5-v1.0.0
book6-v1.0.0
```

Patch tags may be used only when necessary, for example:

```text
book2-v1.0.1
```

A patch tag should fix a clear problem without changing the reader promise of the book.

## Main branch policy

The `main` branch may continue to evolve as the series grows.

That means `main` can contain newer docs, scripts, tests, and lessons than an earlier book release. This is healthy as long as the README and book-specific docs clearly tell readers which tag matches their book.

## Before tagging a book release

Run the appropriate checks for that book layer. At minimum:

```bash
make verify
make doctor
```

For Book 1 local lab work, also run the relevant local Docker checks when Docker is available:

```bash
make check-env
make lab-smoke
make backup-receipt
make down
```

Later books should add their own explicit preflight and cleanup checks before tagging.

## Tag integrity rule

Do not move a published book tag casually.

If a released book tag has a serious error, prefer a new patch tag and a clear release note. Readers should be able to trust that a tag named in a book remains durable.

## Receipt rule for releases

Release receipts should prove useful facts without exposing secrets.

Safe release receipts may include:

- commit hash,
- tag name,
- test output,
- command names,
- public file checksums,
- cleanup confirmation, and
- sample local URLs such as `http://localhost:8080`.

Release receipts must not include:

- passwords,
- API tokens,
- SSH private keys,
- cloud access keys,
- payment secrets,
- customer data,
- private account identifiers, or
- screenshots of credential pages.
