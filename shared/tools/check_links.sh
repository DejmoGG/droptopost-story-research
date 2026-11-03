#!/usr/bin/env bash
# Check every markdown link in a report. Prints non-200 links and a summary.
# Usage: bash shared/tools/check_links.sh <report.md>
f="$1"
[ -f "$f" ] || { echo "no file: $f"; exit 1; }
total=0; bad=0
while read -r u; do
  total=$((total + 1))
  c=$(curl -s -o /dev/null -L -m 15 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120" -w "%{http_code}" "$u")
  if [ "$c" != "200" ]; then bad=$((bad + 1)); echo "$c $u"; fi
done < <(grep -oE '\]\(https?://[^)]+\)' "$f" | sed -E 's/^\]\(//; s/\)$//' | sort -u)
echo "checked=$total not_200=$bad"
