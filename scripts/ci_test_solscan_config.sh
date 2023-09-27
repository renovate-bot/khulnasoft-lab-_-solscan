#!/usr/bin/env bash

### Test

if ! solscan "tests/*.json" --config "tests/config/solscan.config.json"; then
    echo "Config failed"
    exit 1
fi

