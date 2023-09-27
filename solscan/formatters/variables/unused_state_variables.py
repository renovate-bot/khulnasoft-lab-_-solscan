from typing import Dict

from solscan.core.compilation_unit import SolscanCompilationUnit
from solscan.formatters.utils.patches import create_patch


def custom_format(compilation_unit: SolscanCompilationUnit, result: Dict) -> None:
    elements = result["elements"]
    for element in elements:
        if element["type"] == "variable":
            _patch(
                compilation_unit,
                result,
                element["source_mapping"]["filename_absolute"],
                element["source_mapping"]["start"],
            )


def _patch(
    compilation_unit: SolscanCompilationUnit, result: Dict, in_file: str, modify_loc_start: int
) -> None:
    in_file_str = compilation_unit.core.source_code[in_file].encode("utf8")
    old_str_of_interest = in_file_str[modify_loc_start:]
    old_str = (
        old_str_of_interest.decode("utf-8").partition(";")[0]
        + old_str_of_interest.decode("utf-8").partition(";")[1]
    )

    create_patch(
        result,
        in_file,
        int(modify_loc_start),
        # Remove the entire declaration until the semicolon
        int(modify_loc_start + len(old_str_of_interest.decode("utf-8").partition(";")[0]) + 1),
        old_str,
        "",
    )
