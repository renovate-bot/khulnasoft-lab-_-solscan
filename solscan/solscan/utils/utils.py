from typing import Union, Optional

from solscan.core.variables.local_variable import LocalVariable
from solscan.core.variables.state_variable import StateVariable

from solscan.core.declarations.solidity_variables import SolidityVariable
from solscan.core.variables.top_level_variable import TopLevelVariable

from solscan.slithir.variables.temporary import TemporaryVariable
from solscan.slithir.variables.constant import Constant
from solscan.slithir.variables.reference import ReferenceVariable
from solscan.slithir.variables.tuple import TupleVariable
from solscan.core.source_mapping.source_mapping import SourceMapping

RVALUE = Union[
    StateVariable,
    LocalVariable,
    TopLevelVariable,
    TemporaryVariable,
    Constant,
    SolidityVariable,
    ReferenceVariable,
]

LVALUE = Union[
    StateVariable,
    LocalVariable,
    TemporaryVariable,
    ReferenceVariable,
    TupleVariable,
]


def is_valid_rvalue(v: Optional[SourceMapping]) -> bool:
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TopLevelVariable,
            TemporaryVariable,
            Constant,
            SolidityVariable,
            ReferenceVariable,
        ),
    )


def is_valid_lvalue(v: Optional[SourceMapping]) -> bool:
    return isinstance(
        v,
        (
            StateVariable,
            LocalVariable,
            TemporaryVariable,
            ReferenceVariable,
            TupleVariable,
        ),
    )
