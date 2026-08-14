#!/usr/bin/env bash
set -euo pipefail
export THINK_NAME="${THINK_NAME:-SEAT}"
export THINK_PORT="${THINK_PORT:-8199}"
export THINK_PRIMARY="${THINK_PRIMARY:-kimi}"
export THINK_TRIBE_TOOLBELT=true
export THINK_HOST=127.0.0.1
# load secrets...
exec /opt/alloyscape/tribe-think/start-with-identity.sh "$THINK_NAME" "$THINK_PRIMARY" \
  /opt/alloyscape/tribe-think/think-server.mjs \
  /opt/alloyscape/tribe-think
