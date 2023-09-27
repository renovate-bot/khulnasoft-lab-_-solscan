#!/usr/bin/env bash

### Test solscan-prop

cd examples/solscan-prop || exit 1
solscan-prop . --contract ERC20Buggy
if [ ! -f contracts/crytic/TestERC20BuggyTransferable.sol ]; then
    echo "solscan-prop failed"
    return 1
fi
