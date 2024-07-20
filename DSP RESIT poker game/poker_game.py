from card import Card, Deck
from treys import Evaluator, Card as TreysCard 

class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hands = [[], []]  
        self.community_cards = []
        self.evaluator = Evaluator()

    def deal_hole_cards(self):
        for player in range(2):
            self.player_hands[player] = self.deck.deal(2)

    def deal_flop(self):
        self.community_cards = self.deck.deal(3)

    def deal_turn(self):
        self.community_cards.append(self.deck.deal(1)[0])

    def deal_river(self):
        self.community_cards.append(self.deck.deal(1)[0])

    def convert_card(self, card):
        rank = card.rank
        suit = card.suit.lower()
        return TreysCard.new(f"{rank}{suit}")

    def evaluate_hands(self):
        board = [self.convert_card(card) for card in self.community_cards]
        hands = [[self.convert_card(card) for card in hand] for hand in self.player_hands]
        scores = [self.evaluator.evaluate(board, hand) for hand in hands]
        return scores
