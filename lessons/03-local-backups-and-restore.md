# Lesson 3: Local Backups and Restore

In Lesson 1, you served a tiny creator publishing site from `public/`.

In Lesson 2, you inspected files, service status, logs, and the container lifecycle.

In this lesson, you add a publishing habit that matters before any real cloud server exists:

```text
site files -> backup archive -> checksum -> restore test -> receipt
```

A creator storefront is not just a web page. It is a set of files, product notes, styles, and future fulfillment logic. If you cannot back up and restore the small local version, you are not ready to trust the larger hosted version.

## What you will learn

By the end of this lesson, you should understand:

- why `public/` is treated as a publishing asset,
- where local backup archives are written,
- why backup files are ignored by Git,
- how a checksum helps prove which archive was created,
- how to restore the local site from a backup archive,
- why restore practice matters more than backup theory, and
- how to save a backup receipt without exposing secrets.

## 1. Verify the repository

Run:

```bash
make verify
```

This checks the repository contract. It should not require Docker to be running.

## 2. Inspect the current site files

Run:

```bash
make inspect-stack
```

For this lesson, focus on the `public/` files. At this stage, they are the local publishing asset.

## 3. Create a local backup

Run:

```bash
make backup-public
```

This creates a timestamped archive under:

```text
backups/
```

The backup target also writes a checksum file next to the archive.

The archive and checksum are intentionally ignored by Git. They are local operational evidence, not source files for the public repo.

## 4. List your backups

Run:

```bash
make backup-list
```

You should see one or more files shaped like:

```text
backups/YYYYMMDD-HHMMSS-public-site.tar.gz
```

## 5. Save a backup receipt

Run:

```bash
make backup-receipt
```

This creates a backup and saves a receipt under:

```text
receipts/
```

The receipt should tell you:

- when the backup was made,
- which command ran,
- where the backup archive was written,
- where the checksum was written, and
- which files were included.

## 6. Restore from the latest backup

To restore from the latest local backup archive, run:

```bash
make restore-public BACKUP="$(ls -1 backups/*-public-site.tar.gz | tail -n 1)"
```

The restore script checks that the archive looks like a `public/` backup before it extracts anything. It also saves a pre-restore copy under `.tmp/` as a local safety net.

## 7. Prove the site still works

Run:

```bash
make lab-smoke
```

Then stop the lab:

```bash
make down
```

## 8. Check what Git sees

Run:

```bash
git status --short
```

Your backup archives and local receipts should not appear as files to commit.

That is intentional. The public repo should contain the lesson, scripts, and sample receipts. Your personal backup archives belong on your machine.

## Why this matters

A real Ubuntu VPS will eventually raise the same questions:

- What files matter?
- Can I back them up?
- Can I restore them?
- Did I test the restore, or did I merely hope the backup worked?
- Can I prove what happened without saving secrets?

This local lesson keeps the stakes low while building a serious habit: a backup is not real until you have practiced restoring it.
