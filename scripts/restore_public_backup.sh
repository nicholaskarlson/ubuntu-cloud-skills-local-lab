#!/usr/bin/env bash
set -euo pipefail

archive="${1:-}"

if [[ -z "$archive" ]]; then
  echo "Usage: scripts/restore_public_backup.sh backups/YYYYMMDD-HHMMSS-public-site.tar.gz" >&2
  exit 2
fi

if [[ ! -f "$archive" ]]; then
  echo "ERROR: backup archive not found: $archive" >&2
  exit 1
fi

mkdir -p .tmp
stamp="$(date +%Y%m%d-%H%M%S)"
contents=".tmp/${stamp}-restore-contents.txt"
pre_restore=".tmp/${stamp}-pre-restore-public.tar.gz"

tar -tzf "$archive" > "$contents"

if grep -Eq '(^/|(^|/)\.\.(/|$))' "$contents"; then
  echo "ERROR: refusing to restore archive with unsafe paths" >&2
  exit 1
fi

if ! grep -qx 'public/index.html' "$contents"; then
  echo "ERROR: archive does not contain public/index.html" >&2
  exit 1
fi

if ! grep -qx 'public/styles.css' "$contents"; then
  echo "ERROR: archive does not contain public/styles.css" >&2
  exit 1
fi

tar -czf "$pre_restore" public

tar -xzf "$archive" public

echo "Restored public/ from: $archive"
echo "Pre-restore safety copy: $pre_restore"
echo "Validated archive contents list: $contents"
