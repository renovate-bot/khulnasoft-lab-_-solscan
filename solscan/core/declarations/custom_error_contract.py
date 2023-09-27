from typing import TYPE_CHECKING
from solscan.core.declarations.contract_level import ContractLevel


from solscan.core.declarations.custom_error import CustomError

if TYPE_CHECKING:
    from solscan.core.declarations import Contract


class CustomErrorContract(CustomError, ContractLevel):
    def is_declared_by(self, contract: "Contract") -> bool:
        """
        Check if the element is declared by the contract
        :param contract:
        :return:
        """
        return self.contract == contract
