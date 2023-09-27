import inspect
from solscan import Solscan
from solscan.detectors import all_detectors
from solscan.detectors.abstract_detector import AbstractDetector


def _run_all_detectors(solscan: Solscan) -> None:
    detectors = [getattr(all_detectors, name) for name in dir(all_detectors)]
    detectors = [d for d in detectors if inspect.isclass(d) and issubclass(d, AbstractDetector)]

    for detector in detectors:
        solscan.register_detector(detector)

    solscan.run_detectors()
