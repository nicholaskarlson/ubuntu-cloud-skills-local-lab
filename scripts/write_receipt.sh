#!/usr/bin/env bash
set -euo pipefail

label="${1:-manual-note}"
safe_label="$(printf '%s' "$label" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9._-' '-' | sed 's/^-//; s/-$//')"

if [[ -z "$safe_label" ]]; then
  safe_label="manual-note"
fi

mkdir -p receipts
stamp="$(date +%Y%m%d-%H%M%S)"
outfile="receipts/${stamp}-${safe_label}.txt"

{
  echo "Ubuntu Cloud Skills Local Lab receipt"
  echo "Created: $(date -Iseconds)"
  echo "Label: ${safe_label}"
  echo
  cat
} > "$outfile"

echo "Wrote $outfile"
