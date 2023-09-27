from typing import List

from solscan.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from solscan.utils.output import Output


class Backdoor(AbstractDetector):
    """
    Detect function named backdoor
    """

    ARGUMENT = "backdoor"  # solscan will launch the detector with solscan.py --mydetector
    HELP = "Function named backdoor (detector example)"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = "https://github.com/khulnasoft-lab/solscan/wiki/Adding-a-new-detector"
    WIKI_TITLE = "Backdoor example"
    WIKI_DESCRIPTION = "Plugin example"
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = ".."

    def _detect(self) -> List[Output]:
        results = []

        for contract in self.compilation_unit.contracts_derived:
            # Check if a function has 'backdoor' in its name
            for f in contract.functions:
                if "backdoor" in f.name:
                    # Info to be printed
                    info: DETECTOR_INFO = ["Backdoor function found in ", f, "\n"]

                    # Add the result in result
                    res = self.generate_result(info)

                    results.append(res)

        return results
