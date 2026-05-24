#!/usr/bin/env bash
set -euo pipefail

series_only="no"
if [[ "${1:-}" == "--series-status" ]]; then
  series_only="yes"
fi

print_series_status() {
  cat <<'TEXT'
Ubuntu Cloud Skills series status

Book 1 — Your First Local Cloud Lab with Ubuntu and Docker
  Status: implemented as the local lab foundation.
  Stable tag: book1-v1.0.0
  Layer: local Docker lab, static creator page, logs, receipts, backup, restore, cleanup.

Book 2 — Your First Ubuntu Cloud Server
  Status: planned; do not add VPS automation until the safety boundary and reader path are explicit.
  Planned tag: book2-v1.0.0
  Layer: SSH, non-root user, updates, firewall, HTTPS, deploy from Git, server logs, backup, restore, cost cleanup.

Book 3 — Publish Your Creator Website on Ubuntu
  Status: planned.
  Planned tag: book3-v1.0.0
  Layer: content files, site generation, local preview, link checks, accessibility smoke checks, deploy and maintenance receipts.

Book 4 — Build a DIY Digital Bookstore
  Status: planned.
  Planned tag: book4-v1.0.0
  Layer: product metadata, static product pages, download workflow concepts, fulfillment records, backup, restore, safer data boundaries.

Book 5 — Stripe Checkout for Independent Creators
  Status: planned.
  Planned tag: book5-v1.0.0
  Layer: hosted checkout, test mode first, webhook verification, idempotent fulfillment, no card storage, safe logs and receipts.

Book 6 — AWS Skills for Ubuntu Creators
  Status: planned.
  Planned tag: book6-v1.0.0
  Layer: AWS CLI, named profiles, IAM basics, S3, free-tier-aware practice, cleanup, receipts, and cost awareness.
TEXT
}

if [[ "$series_only" == "yes" ]]; then
  print_series_status
  exit 0
fi

cat <<'TEXT'
Ubuntu Cloud Skills repo map

Reader-facing entry points:
  README.md
  docs/quickstart.md
  docs/book1-companion-code.md
  docs/series-roadmap.md
  docs/software-architecture.md
  docs/release-and-tagging-policy.md
  docs/secret-safety.md

Book 1 lessons:
  lessons/01-local-publishing-stack.md
  lessons/02-files-logs-container-lifecycle.md
  lessons/03-local-backups-and-restore.md

Local site files:
  public/index.html
  public/styles.css

Command surface:
  Makefile
  make verify
  make doctor
  make repo-map
  make series-status
  make check-env
  make up / make down
  make lab-smoke
  make backup-public / make restore-public

Scripts:
  scripts/check_env.sh
  scripts/show_local_stack.sh
  scripts/write_receipt.sh
  scripts/logs_receipt.sh
  scripts/container_lifecycle_receipt.sh
  scripts/backup_public.sh
  scripts/backup_receipt.sh
  scripts/restore_public_backup.sh
  scripts/doctor.sh
  scripts/repo_map.sh

Receipts:
  receipts/samples/    safe examples committed to Git
  receipts/*.txt       local receipts ignored by Git

Backups:
  backups/*.tar.gz         local backup archives ignored by Git
  backups/*.tar.gz.sha256  local checksums ignored by Git

Tests:
  tests/test_contract.py
  tests/test_series_foundation.py
TEXT

echo
print_series_status
