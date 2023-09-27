from typing import Optional, List, Union

from solscan.core.declarations import Function
from solscan.core.variables import Variable
from solscan.slithir.operations.operation import Operation


class Call(Operation):
    def __init__(self) -> None:
        super().__init__()
        self._arguments: List[Variable] = []

    @property
    def arguments(self) -> List[Variable]:
        return self._arguments

    @arguments.setter
    def arguments(self, v: List[Variable]) -> None:
        self._arguments = v

    # pylint: disable=no-self-use
    def can_reenter(self, _callstack: Optional[List[Union[Function, Variable]]] = None) -> bool:
        """
        Must be called after slithIR analysis pass
        :return: bool
        """
        return False

    def can_send_eth(self) -> bool:  # pylint: disable=no-self-use
        """
        Must be called after slithIR analysis pass
        :return: bool
        """
        return False
