import sys
from solscan.solscan import Solscan

if len(sys.argv) != 2:
    print("python functions_called.py functions_called.sol")
    sys.exit(-1)

# Init solscan
solscan = Solscan(sys.argv[1])

# Get the contract
contracts = solscan.get_contract_from_name("Contract")
assert len(contracts) == 1
contract = contracts[0]

# Get the variable
entry_point = contract.get_function_from_signature("entry_point()")
assert entry_point

all_calls = entry_point.all_internal_calls()

all_calls_formated = [f.canonical_name for f in all_calls]

# Print the result
print(f"From entry_point the functions reached are {all_calls_formated}")
