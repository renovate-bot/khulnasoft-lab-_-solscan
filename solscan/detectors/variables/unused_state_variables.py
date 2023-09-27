"""
Module detecting unused state variables
"""
from typing import List, Optional, Dict

from solscan.core.compilation_unit import SolscanCompilationUnit
from solscan.core.declarations import Function
from solscan.core.declarations.contract import Contract
from solscan.core.solidity_types import ArrayType
from solscan.core.variables import Variable
from solscan.core.variables.state_variable import StateVariable
from solscan.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from solscan.formatters.variables.unused_state_variables import custom_format
from solscan.utils.output import Output
from solscan.visitors.expression.export_values import ExportValues


def detect_unused(contract: Contract) -> Optional[List[StateVariable]]:
    # Get all the variables read in all the functions and modifiers

    all_functions = [
        f
        for f in contract.all_functions_called + list(contract.modifiers)
        if isinstance(f, Function)
    ]
    variables_used = [x.state_variables_read for x in all_functions]
    variables_used += [
        x.state_variables_written for x in all_functions if not x.is_constructor_variables
    ]

    array_candidates_ = [x.variables for x in all_functions]
    array_candidates: List[Variable] = [i for sl in array_candidates_ for i in sl]
    array_candidates += contract.state_variables
    array_candidates = [
        x.type.length for x in array_candidates if isinstance(x.type, ArrayType) and x.type.length
    ]
    array_candidates = [ExportValues(x).result() for x in array_candidates]
    array_candidates = [i for sl in array_candidates for i in sl]
    array_candidates = [v for v in array_candidates if isinstance(v, StateVariable)]

    # Flat list
    variables_used = [item for sublist in variables_used for item in sublist]
    variables_used = list(set(variables_used + array_candidates))

    # Return the variables unused that are not public
    return [x for x in contract.variables if x not in variables_used and x.visibility != "public"]


class UnusedStateVars(AbstractDetector):
    """
    Unused state variables detector
    """

    ARGUMENT = "unused-state"
    HELP = "Unused state variables"
    IMPACT = DetectorClassification.INFORMATIONAL
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = "https://github.com/khulnasoft-lab/solscan/wiki/Detector-Documentation#unused-state-variable"

    WIKI_TITLE = "Unused state variable"
    WIKI_DESCRIPTION = "Unused state variable."
    WIKI_EXPLOIT_SCENARIO = ""
    WIKI_RECOMMENDATION = "Remove unused state variables."

    def _detect(self) -> List[Output]:
        """Detect unused state variables"""
        results = []
        for c in self.compilation_unit.contracts_derived:
            if c.is_signature_only():
                continue
            unusedVars = detect_unused(c)
            if unusedVars:
                for var in unusedVars:
                    info: DETECTOR_INFO = [var, " is never used in ", c, "\n"]
                    json = self.generate_result(info)
                    results.append(json)

        return results

    @staticmethod
    def _format(compilation_unit: SolscanCompilationUnit, result: Dict) -> None:
        custom_format(compilation_unit, result)
