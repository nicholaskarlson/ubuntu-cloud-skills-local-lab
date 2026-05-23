# Book 1 Companion Code

This repository supports Book 1 of the NEKpress.ca series **Ubuntu Cloud Skills for Independent Creators**.

Book 1 is:

**Your First Local Cloud Lab with Ubuntu and Docker**

## Use the Book 1 release

If you are reading Book 1, use the Book 1 companion-code tag:

```text
book1-v1.0.0
```

Exact commit for this release:

```text
88ff6452419bd027f31cb6e7a6799f5ed0695765
```

Release page:

```text
https://github.com/nicholaskarlson/ubuntu-cloud-skills-local-lab/releases/tag/book1-v1.0.0
```

The main branch may continue to change as later books, corrections, and additional labs are developed. The `main` branch is still useful for current development, but Book 1 readers should use the tag. The tag above preserves the version of the public lab that lines up with Book 1.

## Option 1: Use Git

```bash
git clone https://github.com/nicholaskarlson/ubuntu-cloud-skills-local-lab.git
cd ubuntu-cloud-skills-local-lab
git checkout book1-v1.0.0
make verify
```

Then follow the book and the repository quickstart.

## Option 2: Download the source ZIP

Readers who do not want to use Git can use the release page.

1. Open the release page for `book1-v1.0.0`.
2. Download the source code ZIP.
3. Extract it on your machine.
4. Open a terminal in the extracted folder.
5. Run `make verify`.

## What Book 1 covers

The Book 1 companion release includes:

- Lesson 1: Local Publishing Stack
- Lesson 2: Files, Logs, and the Container Lifecycle
- Lesson 3: Local Backups and Restore
- proof-receipt helpers
- backup and restore scripts
- a local Docker Compose web lab

It does not require Docker Pro, a paid cloud account, AWS, DigitalOcean, Stripe, a domain name, or a public server.

## Why this matters

Books are stable. Repositories can evolve.

The Book 1 tag lets the repository keep improving while still giving readers a durable code version that matches the printed and Kindle editions of Book 1.
