# Lesson 1: Local Publishing Stack

In this lesson, you run a tiny creator publishing site on your own machine.

You are not buying a server. You are not opening a cloud account. You are learning the shape of a cloud-style workflow locally:

```text
site files -> web server container -> browser check -> logs -> receipt -> cleanup
```

## What you will learn

By the end of this lesson, you should understand:

- where the local site files live,
- how Docker Compose starts the web server,
- how to prove the site responded,
- how to inspect logs,
- how to save a receipt, and
- how to stop the lab cleanly.

## 1. Start from a clean repository

Run:

```bash
make verify
```

This checks the repository contract. It should not require Docker to be running.

Then check your tools:

```bash
make check-env
```

## 2. Read the local site files

The demo site lives in:

```text
public/index.html
public/styles.css
```

These files represent the simplest possible version of a creator website. In later lessons, this can grow into product pages, download pages, logs, backups, and eventually a safer payment workflow.

For now, it is intentionally simple.

## 3. Read the service definition

The local web service is defined in:

```text
compose.yaml
```

The important idea is that Docker serves the `public/` directory through a web server container.

When the lab is running, your browser visits:

```text
http://localhost:8080
```

## 4. Start the lab

Run:

```bash
make up
```

Open:

```text
http://localhost:8080
```

You should see the local publishing demo page.

## 5. Prove the page responded

Run:

```bash
make lab-smoke
```

This command starts the lab if needed, fetches the local page, checks for the expected title, and prints the container status.

A successful result ends with:

```text
OK: local web lab responded at http://localhost:8080
```

## 6. Save a proof receipt

Run:

```bash
make lab-smoke-receipt
```

This runs the same basic check and writes a local receipt in:

```text
receipts/
```

The receipt should stay local. It is ignored by Git.

## 7. Inspect logs

Run:

```bash
make logs
```

Logs are one of the first server-administration habits worth learning. They help you answer a simple question:

> What did the server actually do?

## 8. Stop the lab

Run:

```bash
make down
```

Then check status:

```bash
make ps
```

The web service should no longer be running.

## Why this matters

This small lab introduces the pattern behind many real deployments:

- site content lives in files,
- a server serves those files,
- a command starts the service,
- a test proves the service responded,
- logs help diagnose behavior,
- receipts preserve evidence, and
- cleanup prevents confusion and cost.

Later, the same pattern can move to a real Ubuntu VPS, but the learning starts here for free.
