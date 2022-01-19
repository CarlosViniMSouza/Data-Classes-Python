from dataclasses import dataclass
from datetime import date


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
