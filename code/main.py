from collections import namedtuple
from dataclasses import dataclass, field
from dataclasses import fields
from dataclasses import make_dataclass
from datetime import date
from typing import Any


@dataclass
class DataClassExample:
    rank: str
    type: str
    data: date


level = DataClassExample('E', 'wizard', 20000609)

print("\n", level)
print("\nRank: ", level.rank, "\nType: ", level.type, "\nData: ", level.data)


class RegularCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


Position = make_dataclass('Position', ['name', 'lat', 'lon'])

# Error: print(Position('Null Island'))

# Error: print(Position('Greenwich', lat=51.8))

print(Position('Vancouver', -123.1, 49.3))  # sucess!


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})


print(fields(Position))

"""
Output:

lt_factory=<dataclasses._MISSING_TYPE object at 0x000002628E5AAB30>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), Field(name='lon',type=<class 'float'>,default=0.0,default_factory=<dataclasses._MISSING_TYPE object at 0x000002628E5AAB30>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'unit': 'degrees'}),kw_only=False,_field_type=_FIELD), Field(name='lat',type=<class 'float'>,default=0.0,default_factory=<dataclasses._MISSING_TYPE object at 0x000002628E5AAB30>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'unit': 'degrees'}),kw_only=False,_field_type=_FIELD))
"""

lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)
# Output: 'degrees'
