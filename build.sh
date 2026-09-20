#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"
out=build

args=(README.md --export "$out/index.html" --context=malinoskj2/malinoskj2)
[[ -n "${GITHUB_TOKEN:-}" ]] && args+=(--pass="$GITHUB_TOKEN")

v=$(date +%s)
rm -rf "$out"
mkdir -p "$out"
if command -v grip >/dev/null; then
  grip "${args[@]}"
else
  nix run nixpkgs#python3Packages.grip -- "${args[@]}"
fi
sed -i -E \
  -e '\#/__/grip/static/#d' \
  -e '/prefers-color-scheme: dark/d' \
  -e 's#<source media="[^"]*" #<source #g' \
  -e 's#(src|srcset)="https://camo\.githubusercontent\.com/[^"]*"([^>]*) data-canonical-src="([^"]*)"#\1="\3"\2#g' \
  -e "s#(assets/[^\"?]+\.svg)#\\1?v=$v#g" \
  -e "s#((src|srcset)=\"https?://[^\"?]*\?[^\"]*)\"#\\1\&v=$v\"#g" \
  -e "s#((src|srcset)=\"https?://[^\"?]*)\"#\\1?v=$v\"#g" \
  -e 's#<head>#<head><meta http-equiv="Cache-Control" content="no-store">#' \
  -e 's|</head>|<style>.Layout { display: block !important; } .Layout-main { width: 100% !important; }</style></head>|' \
  "$out/index.html"
cp -r assets "$out/assets"

echo "file://$PWD/$out/index.html"
