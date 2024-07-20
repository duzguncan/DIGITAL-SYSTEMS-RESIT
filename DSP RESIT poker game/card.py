import random


RANKS = '23456789TJQKA'
SUITS = 'HDSC'  

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=1):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards
