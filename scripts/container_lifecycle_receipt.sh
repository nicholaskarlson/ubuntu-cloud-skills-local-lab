#!/usr/bin/env bash
set -euo pipefail

tmp="$(mktemp)"
cleanup() {
  docker compose down >/dev/null 2>&1 || true
  rm -f "$tmp"
}
trap cleanup EXIT

{
  echo "Container lifecycle receipt"
  echo
  date -Iseconds
  echo
  echo "Command: make lifecycle-receipt"
  echo
  echo "Starting local web service..."
  docker compose up -d
  sleep 2
  echo
  echo "Fetching local page..."
  curl -fsS http://localhost:8080 > /tmp/ubuntu-cloud-skills-local-lab.html
  grep -q "Ubuntu Cloud Skills Local Lab" /tmp/ubuntu-cloud-skills-local-lab.html
  echo "OK: local page contained expected title"
  echo
  echo "Compose status:"
  docker compose ps
  echo
  echo "Recent web logs:"
  docker compose logs --no-color --tail=40 web || true
  echo
  echo "Stopping local web service..."
  docker compose down
  echo
  echo "OK: lifecycle completed and lab was stopped"
} | tee "$tmp"

bash scripts/write_receipt.sh container-lifecycle < "$tmp"
trap - EXIT
rm -f "$tmp"
