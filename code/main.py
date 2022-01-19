from collections import namedtuple
from dataclasses import dataclass
from dataclasses import make_dataclass
from datetime import date
import attr


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

"""
@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()
"""


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


Position = make_dataclass('Position', ['name', 'lat', 'lon'])

# Error: print(Position('Null Island'))

# Error: print(Position('Greenwich', lat=51.8))

print(Position('Vancouver', -123.1, 49.3))  # sucess!
