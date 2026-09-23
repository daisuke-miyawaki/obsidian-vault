#!/usr/bin/env bash
# Mac のデスクトップ ~/Desktop/自分の観念について/ に .md をコピーする
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
DST="${HOME}/Desktop/自分の観念について"
mkdir -p "$DST"
for f in "$HERE"/*.md; do
  base="$(basename "$f")"
  [[ "$base" == "README.md" ]] && continue
  cp -f "$f" "$DST/"
  echo "copied: $base -> $DST/"
done
