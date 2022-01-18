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
