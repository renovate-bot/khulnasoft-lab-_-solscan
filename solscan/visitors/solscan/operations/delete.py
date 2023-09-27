from typing import List, Union
from solscan.slithir.operations.lvalue import OperationWithLValue

from solscan.slithir.utils.utils import is_valid_lvalue
from solscan.core.variables.state_variable import StateVariable
from solscan.slithir.variables.reference import ReferenceVariable
from solscan.slithir.variables.reference_ssa import ReferenceVariableSSA
from solscan.slithir.variables.state_variable import StateIRVariable


class Delete(OperationWithLValue):
    """
    Delete has a lvalue, as it has for effect to change the value
    of its operand
    """

    def __init__(
        self,
        lvalue: Union[StateIRVariable, StateVariable, ReferenceVariable],
        variable: Union[StateIRVariable, StateVariable, ReferenceVariable, ReferenceVariableSSA],
    ) -> None:
        assert is_valid_lvalue(variable)
        super().__init__()
        self._variable = variable
        self._lvalue = lvalue

    @property
    def read(
        self,
    ) -> List[Union[StateIRVariable, ReferenceVariable, ReferenceVariableSSA, StateVariable]]:
        return [self.variable]

    @property
    def variable(
        self,
    ) -> Union[StateIRVariable, StateVariable, ReferenceVariable, ReferenceVariableSSA]:
        return self._variable

    def __str__(self) -> str:
        return f"{self.lvalue} = delete {self.variable} "
