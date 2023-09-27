from typing import Dict

from solscan.core.expressions import Literal
from solscan.core.variables.variable import Variable
from solscan.tools.mutator.mutators.abstract_mutator import AbstractMutator, FaultNature, FaultClass
from solscan.tools.mutator.utils.generic_patching import remove_assignement


class MVIV(AbstractMutator):  # pylint: disable=too-few-public-methods
    NAME = "MVIV"
    HELP = "variable initialization using a value"
    FAULTCLASS = FaultClass.Assignement
    FAULTNATURE = FaultNature.Missing

    def _mutate(self) -> Dict:

        result: Dict = {}
        variable: Variable

        for contract in self.solscan.contracts:

            # Create fault for state variables declaration
            for variable in contract.state_variables_declared:
                if variable.initialized:
                    # Cannot remove the initialization of constant variables
                    if variable.is_constant:
                        continue

                    if isinstance(variable.expression, Literal):
                        remove_assignement(variable, contract, result)

            for function in contract.functions_declared + list(contract.modifiers_declared):
                for variable in function.local_variables:
                    if variable.initialized and isinstance(variable.expression, Literal):
                        remove_assignement(variable, contract, result)

        return result
