#!/usr/bin/env bash
set -euo pipefail

tmp="$(mktemp)"
cleanup() {
  rm -f "$tmp"
}
trap cleanup EXIT

{
  echo "Public site backup receipt"
  echo
  date -Iseconds
  echo
  echo "Command: make backup-receipt"
  echo
  bash scripts/backup_public.sh
} | tee "$tmp"

bash scripts/write_receipt.sh public-site-backup < "$tmp"
