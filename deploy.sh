#!/usr/bin/env bash
#
# Deploy the HCMI Lab site to the TMU production server.
#
# The TMU server (pascal.ee.torontomu.ca) requires interactive MFA
# (password + verification code), so this cannot run in CI — you run it
# locally and enter your credentials when prompted.
#
# Usage:
#   ./deploy.sh              # build, then deploy to production
#   ./deploy.sh --dry-run    # build, then show what WOULD change (no upload)
#
# Override the target if needed:
#   TMU_USER=someone ./deploy.sh
#
set -euo pipefail

# --- Config (edit if these ever change) ---
TMU_USER="${TMU_USER:-mzihayat}"
TMU_HOST="${TMU_HOST:-pascal.ee.torontomu.ca}"
TMU_PATH="${TMU_PATH:-/home/courses/hcmi/}"
BASE_URL="${BASE_URL:-http://hcmi.ee.torontomu.ca/}"

# Make sure Homebrew tools (hugo) are on PATH when run from a GUI/other shell.
export PATH="/opt/homebrew/bin:$PATH"

cd "$(dirname "$0")"

DRY=""
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY="--dry-run"
fi

echo "==> Building site (baseURL: $BASE_URL)"
rm -rf public resources/_gen
python3 scripts/fetch_linkedin_posts.py
hugo --gc --minify --baseURL "$BASE_URL"

if [[ -n "$DRY" ]]; then
  echo ""
  echo "==> DRY RUN — showing what would change on the server (nothing is uploaded):"
fi

echo ""
echo "==> Deploying to ${TMU_USER}@${TMU_HOST}:${TMU_PATH}"
echo "    (you'll be prompted for your TMU password and verification code)"
echo ""

rsync -avz --delete $DRY \
  public/ \
  "${TMU_USER}@${TMU_HOST}:${TMU_PATH}"

echo ""
if [[ -n "$DRY" ]]; then
  echo "==> Dry run complete. Re-run without --dry-run to deploy for real."
else
  echo "==> Deploy complete: http://hcmi.ee.torontomu.ca"
fi
