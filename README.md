# Ubuntu Cloud Skills Local Lab

A free, local-first companion lab for the NEKpress.ca series:

**Ubuntu Cloud Skills for Independent Creators**

This repo teaches practical cloud-adjacent skills without requiring a paid cloud account.

You will learn how to run a small website-like stack locally, inspect logs, manage files, use Docker, connect to a second Ubuntu machine over a private LAN, and build habits that later transfer to a real public server if you choose to rent one.

## Book 1 readers

This repository is the public companion lab for **Book 1** of *Ubuntu Cloud Skills for Independent Creators*:

**Your First Local Cloud Lab with Ubuntu and Docker**

If you are reading Book 1, use the matching companion-code release instead of assuming the latest `main` branch is identical to the printed book:

- Book 1 code tag: `book1-v1.0.0`
- Book 1 release: <https://github.com/nicholaskarlson/ubuntu-cloud-skills-local-lab/releases/tag/book1-v1.0.0>
- Exact Book 1 code commit: `88ff6452419bd027f31cb6e7a6799f5ed0695765`

The `main` branch may continue to change as the series grows. The Book 1 tag preserves the lab version that matches the commands and lessons in the book.

See [Book 1 Companion Code](docs/book1-companion-code.md) for clone, checkout, and source-ZIP instructions.

## Quickstart

Start here:

- [Quickstart](docs/quickstart.md)
- [Lesson 1: Local Publishing Stack](lessons/01-local-publishing-stack.md)
- [Lesson 2: Files, Logs, and the Container Lifecycle](lessons/02-files-logs-container-lifecycle.md)
- [Lesson 3: Local Backups and Restore](lessons/03-local-backups-and-restore.md)
- [Proof Receipts](docs/proof-receipts.md)
- [Learning Contract](docs/learning-contract.md)
- [Book Series Plan](docs/book-series-plan.md)
- [Series Roadmap](docs/series-roadmap.md)
- [Software Architecture](docs/software-architecture.md)
- [Release and Tagging Policy](docs/release-and-tagging-policy.md)
- [Secret Safety](docs/secret-safety.md)

The first labs run locally with Docker and do not require a paid cloud account.

## Series foundation

This repository is organized as the continuing companion repo for the Ubuntu Cloud Skills series. Book-specific tags preserve the exact code for a printed or Kindle book, while `main` can continue to evolve in small, tested increments.

Foundation references:

- [Series Roadmap](docs/series-roadmap.md)
- [Software Architecture](docs/software-architecture.md)
- [Release and Tagging Policy](docs/release-and-tagging-policy.md)
- [Secret Safety](docs/secret-safety.md)

Useful safe inspection commands:

```bash
make doctor
make repo-map
make series-status
```

`make doctor` runs safe, non-deploying checks and prints next recommended commands. It does not start Docker, write receipts, create backups, deploy to a server, connect by SSH, or require a paid cloud account.

## Book 2 LAN-first pivot

Book 2 is now pivoting from a cloud-provider-first VPS path to a safer LAN-first Ubuntu server lab.

Working Book 2 title:

**Your First Ubuntu Server Lab**

Working promise:

> Practice VPS-style skills safely at home before renting a cloud server.

The default Book 2 path uses two machines on the same private network:

- a client machine, such as your Ubuntu desktop, and
- a server machine, such as an Ubuntu laptop, old desktop, mini PC, or VM.

This lets readers practice SSH, users, updates, firewall posture, logs, deployment, backup, restore, and receipts without DigitalOcean, AWS, a domain name, router port forwarding, or public exposure.

Book 2 references:

- [Book 2 Companion Code](docs/book2-companion-code.md)
- [Book 2 LAN Server Lab](docs/book2-lan-server-lab.md)
- [Book 2 Server Safety Boundary](docs/book2-server-safety-boundary.md)
- [Book 2 Optional VPS Checklist](docs/book2-vps-checklist.md)
- [Lesson 4: First Ubuntu Server Safety](lessons/04-first-ubuntu-server-safety.md)

Safe Book 2 inspection commands:

```bash
make book2-doctor
make book2-check-inputs
make book2-lan-ip-help
```

These commands do not connect to a server, install packages, change firewall rules, deploy files, open router ports, or write receipts. They prepare the reader path for later explicit SSH and deployment drop-ins.

## Lessons

- [Lesson 1: Local Publishing Stack](lessons/01-local-publishing-stack.md)
- [Lesson 2: Files, Logs, and the Container Lifecycle](lessons/02-files-logs-container-lifecycle.md)
- [Lesson 3: Local Backups and Restore](lessons/03-local-backups-and-restore.md)
- [Lesson 4: First Ubuntu Server Safety](lessons/04-first-ubuntu-server-safety.md)

Lesson 1 turns the simple web server into a tiny independent creator publishing demo. It introduces the key pattern for the series: edit local site files, run the site in Docker, verify the result, inspect logs, save receipts, and stop the lab cleanly.

Lesson 2 slows down the workflow and teaches the daily rhythm of small server administration: inspect files, check service status, read logs, save log receipts, run a full container lifecycle receipt, and cleanly stop the lab.

Lesson 3 introduces local backup and restore habits. It treats the `public/` site folder as a small publishing asset, saves a timestamped archive, records a checksum, and practices restoring the site before any real VPS or paid cloud account enters the picture.

Lesson 4 starts Book 2 carefully. It explains how to think about a LAN-first Ubuntu server lab before any command connects to another machine or changes a remote system.

## Who this is for

This lab is for independent creators, writers, students, small publishers, and careful beginners who want to understand the tools behind small web platforms and digital storefronts.

You do not need a paid cloud account to begin.

## Primary learning path

The main path assumes:

- Ubuntu LTS
- Git
- Docker Engine
- Docker Compose
- A terminal

For Book 2, the preferred path adds one of these:

- a second Ubuntu machine on the same home network,
- an old laptop or desktop running Ubuntu,
- a mini PC running Ubuntu,
- a Linux VM, or
- a rented VPS only as an optional later path.

A Windows path using WSL2 Ubuntu may be added later.

## What this repo is not

This is not a Docker Pro course.

This is not a DigitalOcean-only course.

This is not an AWS-only course.

This is not a router port-forwarding guide.

This is a local-first Ubuntu cloud-skills lab. Later books may show how the same concepts move to public hosting, DigitalOcean, AWS, or another provider, but those are optional migrations rather than the starting point.

## First goal

Run a tiny local publishing stack:

- a web server container
- a simple static creator site
- local logs
- a repeatable Makefile workflow
- proof receipts showing what worked

## Proof-first habit

Each chapter should leave behind small receipts:

- command output
- version checks
- test results
- cleanup checks

Do not save secrets, tokens, private keys, passwords, public account details, or customer data in receipts.
