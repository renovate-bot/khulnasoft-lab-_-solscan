from typing import Tuple, List, Type

from solscan_my_plugin.detectors.example import Example

from solscan.detectors.abstract_detector import AbstractDetector
from solscan.printers.abstract_printer import AbstractPrinter


def make_plugin() -> Tuple[List[Type[AbstractDetector]], List[Type[AbstractPrinter]]]:
    plugin_detectors = [Example]
    plugin_printers: List[Type[AbstractPrinter]] = []

    return plugin_detectors, plugin_printers
