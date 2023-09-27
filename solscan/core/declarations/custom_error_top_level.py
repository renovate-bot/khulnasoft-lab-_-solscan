from typing import TYPE_CHECKING

from solscan.core.declarations.custom_error import CustomError
from solscan.core.declarations.top_level import TopLevel

if TYPE_CHECKING:
    from solscan.core.compilation_unit import SolscanCompilationUnit
    from solscan.core.scope.scope import FileScope


class CustomErrorTopLevel(CustomError, TopLevel):
    def __init__(self, compilation_unit: "SolscanCompilationUnit", scope: "FileScope") -> None:
        super().__init__(compilation_unit)
        self.file_scope: "FileScope" = scope
