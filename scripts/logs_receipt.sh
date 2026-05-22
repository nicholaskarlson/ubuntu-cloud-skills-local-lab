#!/usr/bin/env bash
set -euo pipefail

tmp="$(mktemp)"
cleanup() {
  rm -f "$tmp"
}
trap cleanup EXIT

{
  echo "Container logs receipt"
  echo
  date -Iseconds
  echo
  echo "Command: make logs-receipt"
  echo
  echo "Compose status:"
  docker compose ps || true
  echo
  echo "Recent web logs:"
  docker compose logs --no-color --tail=80 web || true
} | tee "$tmp"

bash scripts/write_receipt.sh container-logs < "$tmp"
