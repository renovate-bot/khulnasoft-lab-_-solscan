#!/usr/bin/env bash
shopt -s extglob

### Test solscan-flat
solc-select use 0.8.19 --always-install

cd examples/flat || exit 1

if ! solscan-flat b.sol; then
    echo "solscan-flat failed"
    exit 1
fi
 
SUFFIX="@(sol)"
if ! solc "crytic-export/flattening/"*$SUFFIX; then
    echo "solc failed on flattened files"
    exit 1
fi

exit 0
