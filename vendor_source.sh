#!/usr/bin/env bash
set -euo pipefail

# Change folder to correct name
cd ags-3.1.1

cat > .npmrc <<'EOF'
node-linker=hoisted
store-dir=.pnpm-store
cache-dir=.pnpm-cache
virtual-store-dir=.pnpm
EOF

pnpm install --lockfile-only
pnpm fetch
pnpm install --offline --frozen-lockfile

ARCHIVE_NAME="ags-pnpm-offline-cache.tar.gz"
tar --mtime='2025-01-01' \
    --owner=0 --group=0 --numeric-owner \
    -czf "../$ARCHIVE_NAME" \
    package.json \
    pnpm-lock.yaml \
    .npmrc \
    .pnpm-store \
    .pnpm-cache \
    .pnpm \
    node_modules

echo "Archive created: ../$ARCHIVE_NAME"
echo "Size: $(du -h ../$ARCHIVE_NAME | cut -f1)"
