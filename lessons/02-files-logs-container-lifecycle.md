# Lesson 2: Files, Logs, and the Container Lifecycle

In Lesson 1, you proved that a local web server container could serve a tiny creator publishing site.

In this lesson, you slow down and study the moving parts:

```text
site files -> mounted into container -> web request -> logs -> receipt -> clean stop
```

This is the daily rhythm of small server administration. Before you pay for a VPS, you should understand how files, services, logs, checks, and cleanup fit together.

## What you will learn

By the end of this lesson, you should understand:

- which files make up the local site,
- how the container sees those files,
- how to check whether the service is running,
- how to read basic web server logs,
- how to save a logs receipt,
- how to run a full lifecycle receipt, and
- why stopping the lab cleanly matters.

## 1. Verify the repository

Run:

```bash
make verify
```

This checks the repository contract. It should not require Docker to be running.

## 2. Inspect the local stack

Run:

```bash
make inspect-stack
```

This prints a compact overview of the local lab:

- the current directory,
- the local site files in `public/`,
- the Compose service status, and
- the configured local web address.

If the lab is not running yet, that is okay. The inspection step still teaches you where to look.

## 3. Start the web service

Run:

```bash
make up
```

Then check status:

```bash
make ps
```

You should see the `web` service running with local port `8080` mapped to the container web port.

## 4. Visit the site and create a log entry

Open:

```text
http://localhost:8080
```

Or use the terminal:

```bash
curl -fsS http://localhost:8080 > /tmp/ubuntu-cloud-skills-local-lab.html
```

That request should create a log entry inside the web container.

## 5. Read the logs

Run:

```bash
make logs
```

You should see web server log output from the `web` service.

Logs answer questions such as:

- Did a request reach the server?
- Which path was requested?
- Did the server return a successful response?
- Is the container producing errors?

For now, you do not need to understand every field in the log line. The key habit is learning where logs are and how to inspect them.

## 6. Save a logs receipt

Run:

```bash
make logs-receipt
```

This captures the current container status and recent web logs, then writes a local receipt under:

```text
receipts/
```

The receipt is ignored by Git. It is evidence for you, not source code for the public repository.

## 7. Run a full lifecycle receipt

Run:

```bash
make lifecycle-receipt
```

This command demonstrates a complete local service lifecycle:

```text
start -> request -> status -> logs -> stop -> receipt
```

A successful run ends with a local receipt and a stopped lab.

## 8. Stop the lab manually when needed

If you started the lab yourself, stop it with:

```bash
make down
```

Then check:

```bash
make ps
```

The service should no longer be running.

## Why this matters

A future real Ubuntu VPS will have the same basic questions:

- What files are being served?
- Is the service running?
- What do the logs say?
- Can I prove the site responded?
- Did I clean up or leave something running?

This local lesson builds those habits before money, domains, TLS certificates, payment systems, or cloud dashboards enter the picture.
