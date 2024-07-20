import random
from collections import Counter


ranks = '23456789TJQKA'
suits = 'HDSC'
deck = [r + s for r in ranks for s in suits]


def card_rank(card):
    ranks = '23456789TJQKA'
    return ranks.index(card[0])

def hand_rank(hand):
    """ Return a value indicating the ranking of a hand. """
    ranks = sorted([card_rank(card) for card in hand], reverse=True)
    if len(set(card[1] for card in hand)) == 1:  
        if ranks == [12, 11, 10, 9, 8]:  
            return (8, ranks)
        return (5, ranks)
    if len(set(ranks)) == 2:  
        if ranks[0] == ranks[3] or ranks[1] == ranks[4]:
            return (7, ranks)
        return (6, ranks)
    if ranks == list(range(ranks[0], ranks[0] - 5, -1)):  
        return (4, ranks)
    if len(set(ranks)) == 3:  
        if ranks[0] == ranks[2] or ranks[1] == ranks[3] or ranks[2] == ranks[4]:
            return (3, ranks)
        return (2, ranks)
    if len(set(ranks)) == 4:  
        return (1, ranks)
    return (0, ranks)  


def determine_winner(hand1, hand2):
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)
    return 'Player 1' if rank1 > rank2 else 'Player 2' if rank2 > rank1 else 'Tie'


def bot_strategy(hand, community_cards):
    hand_strength = hand_rank(hand + community_cards)
    if hand_strength[0] >= 3:  
        return 'raise'
    elif hand_strength[0] >= 1:  
        return 'call'
    else:
        return 'fold'


def calculate_win_percentage(hand, num_simulations=10000):
    outcomes = Counter()
    for _ in range(num_simulations):
        deck = [r + s for r in ranks for s in suits if r + s not in hand]
        random.shuffle(deck)
        opponent_hand = [deck.pop() for _ in range(2)]
        community_cards = [deck.pop() for _ in range(5)]
        winner = determine_winner(hand + community_cards, opponent_hand + community_cards)
        outcomes[winner] += 1
    win_percentage = (outcomes['Player 1'] / num_simulations) * 100
    return win_percentage


example_hands = [
    ['AS', 'KD'],
    ['5H', '5C'],
    ['2D', '7S'],
    ['9H', '9D'],
    ['4S', '6S']
]


example_community_cards = [
    ['2C', '3H', '5S', '9D', 'KH'],  
    ['TS', 'JS', 'QS', 'KS', '9S'],  
    ['AH', 'KH', 'QH', 'JH', 'TH'],  
    ['2D', '2H', '2S', '5D', '5H'],  
    ['6D', '7D', '8D', '9D', 'TD']   
]


for hand in example_hands:
    for community_cards in example_community_cards:
        decision = bot_strategy(hand, community_cards)
        win_percentage = calculate_win_percentage(hand)
        print(f"Hand: {hand}, Community Cards: {community_cards}, Bot decision: {decision}, Win percentage: {win_percentage:.2f}%")
