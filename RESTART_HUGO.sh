#!/bin/bash
# Script to restart Hugo with cache clearing flags

echo "Stopping any running Hugo server..."
pkill -f "hugo server" || true

echo "Clearing cache..."
rm -rf public resources/_gen

echo "Starting Hugo with cache disabled..."
hugo server --disableFastRender --ignoreCache

