from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


res = make_french_deck()
print(res)

"""
Output:

[PlayingCard(rank='2', suit='♣'), PlayingCard(rank='3', suit='♣'), PlayingCard(rank='4', suit='♣'), PlayingCard(rank='5', suit='♣'), PlayingCard(rank='6', suit='♣'), PlayingCard(rank='7', suit='♣'), PlayingCard(rank='8', suit='♣'), PlayingCard(rank='9', suit='♣'), PlayingCard(rank='10', suit='♣'), PlayingCard(rank='J', suit='♣'), PlayingCard(rank='Q', suit='♣'), PlayingCard(rank='K', suit='♣'), PlayingCard(rank='A', suit='♣'), P suit='♡'), PlayingCard(rank='9', suit='♡'), PlayingCard(rank='10', suit='♡'), PlayingCard(rank='J', suit='♡'), PlayingCard(rank='Q', suit='♡'), PlayingCard(rank='K', suit='♡'), PlayingCard(rank='A', suit='♡'), PlayingCard(rank='2', suit='♠'), PlayingCard(rank='3', suit='♠'), PlayingCard(rank='4', suit='♠'), PlayingCard(rank='5', suit='♠'), PlayingCard(rank='6', suit='♠'), PlayingCard(rank='7', suit='♠'), PlayingCard(rank='8', suit='♠'), PlayingCard(rank='9', suit='♠'), PlayingCard(rank='10', suit='♠'), PlayingCard(rank='J', suit='♠'), PlayingCard(rank='Q', suit='♠'), PlayingCard(rank='K', suit='♠'), PlayingCard(rank='A', suit='♠')]
"""
