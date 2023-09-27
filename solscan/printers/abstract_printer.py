import abc
from logging import Logger

from typing import TYPE_CHECKING, Union, List, Optional, Dict

from solscan.utils import output
from solscan.utils.output import SupportedOutput

if TYPE_CHECKING:
    from solscan import Solscan


class IncorrectPrinterInitialization(Exception):
    pass


class AbstractPrinter(metaclass=abc.ABCMeta):
    ARGUMENT = ""  # run the printer with solscan.py --ARGUMENT
    HELP = ""  # help information

    WIKI = ""

    def __init__(self, solscan: "Solscan", logger: Logger) -> None:
        self.solscan = solscan
        self.contracts = solscan.contracts
        self.filename = solscan.filename
        self.logger = logger

        if not self.HELP:
            raise IncorrectPrinterInitialization(
                f"HELP is not initialized {self.__class__.__name__}"
            )

        if not self.ARGUMENT:
            raise IncorrectPrinterInitialization(
                f"ARGUMENT is not initialized {self.__class__.__name__}"
            )

        if not self.WIKI:
            raise IncorrectPrinterInitialization(
                f"WIKI is not initialized {self.__class__.__name__}"
            )

    def info(self, info: str) -> None:
        if self.logger:
            self.logger.info(info)

    def generate_output(
        self,
        info: Union[str, List[Union[str, SupportedOutput]]],
        additional_fields: Optional[Dict] = None,
    ) -> output.Output:
        if additional_fields is None:
            additional_fields = {}
        printer_output = output.Output(info, additional_fields)
        printer_output.data["printer"] = self.ARGUMENT

        return printer_output

    @abc.abstractmethod
    def output(self, filename: str) -> output.Output:
        pass
