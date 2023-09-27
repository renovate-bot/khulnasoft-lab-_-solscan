from typing import TYPE_CHECKING, List, Dict, Union

from solscan.core.declarations.contract import USING_FOR_KEY, USING_FOR_ITEM
from solscan.core.solidity_types.type import Type
from solscan.core.declarations.top_level import TopLevel

if TYPE_CHECKING:
    from solscan.core.scope.scope import FileScope


class UsingForTopLevel(TopLevel):
    def __init__(self, scope: "FileScope") -> None:
        super().__init__()
        self._using_for: Dict[Union[str, Type], List[Type]] = {}
        self.file_scope: "FileScope" = scope

    @property
    def using_for(self) -> Dict[USING_FOR_KEY, USING_FOR_ITEM]:
        return self._using_for
