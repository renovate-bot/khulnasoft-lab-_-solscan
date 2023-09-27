from pathlib import Path
from solscan import Solscan

TEST_DATA_DIR = Path(__file__).resolve().parent / "test_data"


def test_function_id_rec_structure(solc_binary_path) -> None:
    solc_path = solc_binary_path("0.8.0")
    solscan = Solscan(Path(TEST_DATA_DIR, "type_helpers.sol").as_posix(), solc=solc_path)
    for compilation_unit in solscan.compilation_units:
        for function in compilation_unit.functions:
            assert function.solidity_signature
