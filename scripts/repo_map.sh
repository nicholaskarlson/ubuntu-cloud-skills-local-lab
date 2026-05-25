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

Book 2 — Your First Ubuntu Server Lab
  Status: LAN-first pivot added. Safe readiness and input checks exist; no live SSH or deployment automation yet.
  Planned tag: book2-v1.0.0
  Layer: private LAN server lab, SSH readiness, server safety boundary, optional VPS migration later, logs, backup, restore, cleanup.

Book 3 — Publish Your Creator Website on Ubuntu
  Status: planned.
  Planned tag: book3-v1.0.0
  Layer: content files, site generation, local preview, link checks, accessibility smoke checks, LAN deployment first, optional public publishing later.

Book 4 — Build a DIY Digital Bookstore
  Status: planned.
  Planned tag: book4-v1.0.0
  Layer: product metadata, static product pages, download workflow concepts, fulfillment records, backup, restore, safer data boundaries.

Book 5 — Stripe Checkout for Independent Creators
  Status: planned.
  Planned tag: book5-v1.0.0
  Layer: hosted checkout, test mode first, local webhook practice, webhook verification, idempotent fulfillment, no card storage, safe logs and receipts.

Book 6 — Cloud Skills for Ubuntu Creators
  Status: planned.
  Planned tag: book6-v1.0.0
  Layer: portable cloud migration skills, optional provider paths, storage, cleanup, receipts, and cost awareness.
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
  docs/book2-companion-code.md
  docs/book2-lan-server-lab.md
  docs/book2-server-safety-boundary.md
  docs/book2-vps-checklist.md

Book 1 lessons:
  lessons/01-local-publishing-stack.md
  lessons/02-files-logs-container-lifecycle.md
  lessons/03-local-backups-and-restore.md

Book 2 LAN-first scaffold:
  docs/book2-companion-code.md
  docs/book2-lan-server-lab.md
  docs/book2-server-safety-boundary.md
  docs/book2-vps-checklist.md
  lessons/04-first-ubuntu-server-safety.md
  book2/env.example

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
  make book2-doctor
  make book2-check-inputs
  make book2-lan-ip-help

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
  scripts/book2_doctor.sh
  scripts/book2_check_inputs.sh
  scripts/book2_lan_ip_help.sh

Receipts:
  receipts/samples/    safe examples committed to Git
  receipts/*.txt       local receipts ignored by Git

Backups:
  backups/*.tar.gz         local backup archives ignored by Git
  backups/*.tar.gz.sha256  local checksums ignored by Git

Tests:
  tests/test_contract.py
  tests/test_series_foundation.py
  tests/test_foundation_repair.py
  tests/test_book2_scaffold.py
  tests/test_book2_lan_pivot.py
TEXT

echo
print_series_status
