#!/usr/bin/env bash
set -euo pipefail

mkdir -p backups .tmp

stamp="$(date +%Y%m%d-%H%M%S)"
archive="backups/${stamp}-public-site.tar.gz"
checksum="${archive}.sha256"
manifest=".tmp/${stamp}-public-site-manifest.txt"

find public -type f -print | sort > "$manifest"

tar -czf "$archive" public
sha256sum "$archive" > "$checksum"

echo "Public site backup"
echo
echo "Backup archive: $archive"
echo "Checksum file:  $checksum"
echo "Manifest file:  $manifest"
echo
echo "Files included:"
cat "$manifest"
echo
echo "Checksum:"
cat "$checksum"
