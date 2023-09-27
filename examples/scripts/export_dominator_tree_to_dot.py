import sys
from solscan.solscan import Solscan


if len(sys.argv) != 2:
    print("python export_dominator_tree_to_dot.py contract.sol")
    sys.exit(-1)

# Init solscan
solscan = Solscan(sys.argv[1])

for contract in solscan.contracts:
    for function in list(contract.functions) + list(contract.modifiers):
        filename = f"{sys.argv[1]}-{contract.name}-{function.full_name}_dom.dot"
        print(f"Export {filename}")
        function.dominator_tree_to_dot(filename)
