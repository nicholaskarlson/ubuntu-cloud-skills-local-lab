#!/usr/bin/env bash
set -euo pipefail

echo "Ubuntu Cloud Skills doctor"
echo

echo "Purpose: safe, non-deploying repo health checks."
echo "This command does not start Docker, write receipts, create backups, deploy to a server, or require a paid cloud account."
echo

missing=0
check_file() {
  local path="$1"
  if [[ -e "$path" ]]; then
    echo "OK: $path"
  else
    echo "ERROR: missing $path" >&2
    missing=1
  fi
}

echo "Repository contract tests:"
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
echo

echo "Foundation files:"
check_file README.md
check_file Makefile
check_file compose.yaml
check_file docs/book1-companion-code.md
check_file docs/book-series-plan.md
check_file docs/series-roadmap.md
check_file docs/software-architecture.md
check_file docs/release-and-tagging-policy.md
check_file docs/secret-safety.md
check_file scripts/doctor.sh
check_file scripts/repo_map.sh
check_file tests/test_series_foundation.py

if [[ "$missing" -ne 0 ]]; then
  echo
  echo "ERROR: doctor found missing foundation files." >&2
  exit 1
fi

echo

echo "Tool readiness:"
if command -v git >/dev/null 2>&1; then
  echo "OK: git -> $(git --version)"
else
  echo "WARN: git not found"
fi

if command -v python3 >/dev/null 2>&1; then
  echo "OK: python3 -> $(python3 --version)"
else
  echo "ERROR: python3 not found" >&2
  exit 1
fi

if command -v docker >/dev/null 2>&1; then
  echo "OK: docker command is available -> $(docker --version)"
else
  echo "INFO: docker command not found. That is acceptable for make doctor; run make check-env before Docker labs."
fi

if command -v curl >/dev/null 2>&1; then
  echo "OK: curl -> $(curl --version | head -n 1)"
else
  echo "INFO: curl not found. Install it before local web smoke checks."
fi

echo

echo "Book tag policy:"
echo "OK: Book 1 stable tag remains book1-v1.0.0."
echo "OK: main may evolve, but book-specific tags should preserve the code that matches each book."

echo

echo "Secret safety reminder:"
echo "Do not put passwords, API tokens, SSH private keys, cloud credentials, Stripe secrets, customer data, or credential screenshots in Git, logs, receipts, or examples."

echo

echo "Next useful commands:"
echo "  make repo-map"
echo "  make series-status"
echo "  make check-env      # when ready to check Docker availability"
echo "  make up             # starts the local web lab; not run by doctor"
echo

echo "OK: doctor completed"
