import sys
from solscan.solscan import Solscan


if len(sys.argv) != 2:
    print("python function_called.py contract.sol")
    sys.exit(-1)

# Init solscan
solscan = Solscan(sys.argv[1])

for contract in solscan.contracts:
    for function in contract.functions + contract.modifiers:
        filename = f"{sys.argv[1]}-{contract.name}-{function.full_name}.dot"
        print(f"Export {filename}")
        function.slithir_cfg_to_dot(filename)
