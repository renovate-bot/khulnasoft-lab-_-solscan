from typing import Dict, TYPE_CHECKING

from solscan.core.variables.top_level_variable import TopLevelVariable
from solscan.solc_parsing.variables.variable_declaration import VariableDeclarationSolc
from solscan.solc_parsing.declarations.caller_context import CallerContextExpression

if TYPE_CHECKING:
    from solscan.solc_parsing.solscan_compilation_unit_solc import SolscanCompilationUnitSolc
    from solscan.core.compilation_unit import SolscanCompilationUnit


class TopLevelVariableSolc(VariableDeclarationSolc, CallerContextExpression):
    def __init__(
        self,
        variable: TopLevelVariable,
        variable_data: Dict,
        solscan_parser: "SolscanCompilationUnitSolc",
    ) -> None:
        super().__init__(variable, variable_data)
        self._solscan_parser = solscan_parser

    @property
    def is_compact_ast(self) -> bool:
        return self._solscan_parser.is_compact_ast

    @property
    def compilation_unit(self) -> "SolscanCompilationUnit":
        return self._solscan_parser.compilation_unit

    def get_key(self) -> str:
        return self._solscan_parser.get_key()

    @property
    def solscan_parser(self) -> "SolscanCompilationUnitSolc":
        return self._solscan_parser

    @property
    def underlying_variable(self) -> TopLevelVariable:
        # Todo: Not sure how to overcome this with mypy
        assert isinstance(self._variable, TopLevelVariable)
        return self._variable
