# Ubuntu Cloud Skills Local Lab

A free, local-first companion lab for the NEKpress.ca series:

**Ubuntu Cloud Skills for Independent Creators**

This repo teaches practical cloud-adjacent skills without requiring a paid cloud account.

You will learn how to run a small website-like stack locally, inspect logs, manage files, use Docker, and build habits that later transfer to a real Ubuntu VPS.

## Quickstart

Start here:

- [Quickstart](docs/quickstart.md)
- [Learning Contract](docs/learning-contract.md)
- [Book Series Plan](docs/book-series-plan.md)

The first lab runs locally with Docker and does not require a paid cloud account.

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

A Windows path using WSL2 Ubuntu may be added later.

## What this repo is not

This is not a Docker Pro course.

This is not a DigitalOcean-only course.

This is not an AWS-only course.

This is a local-first Ubuntu cloud-skills lab. Later books may show how the same concepts move to DigitalOcean, AWS, or another VPS/cloud provider.

## First goal

Run a tiny local publishing stack:

- a web server container
- a simple static site
- local logs
- a repeatable Makefile workflow
- proof receipts showing what worked

## Proof-first habit

Each chapter should leave behind small receipts:

- command output
- version checks
- test results
- cleanup checks

Do not save secrets, tokens, private keys, passwords, or personal account details in receipts.
