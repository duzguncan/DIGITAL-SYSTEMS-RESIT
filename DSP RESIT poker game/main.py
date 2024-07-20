from poker_game import PokerGame

def clear_screen():
    print("\n" * 100)  

def get_bet(player, chips):
    while True:
        try:
            bet = int(input(f"Player {player + 1}, enter your bet (you have {chips[player]} chips): "))
            if 0 < bet <= chips[player]:
                return bet
            else:
                print(f"Invalid bet amount. You have {chips[player]} chips.")
        except ValueError:
            print("Please enter a valid number.")

def show_hand(player, hand):
    clear_screen()
    print(f"Player {player + 1}, your hand: {hand}")
    input("Press Enter to continue...")

def prompt_bet(player, player_chips):
    clear_screen()
    print(f"Player {player + 1}, it's your turn to bet.")
    bet = get_bet(player, player_chips)
    clear_screen()
    return bet

def main():
    player_chips = [100, 100]  

    print("Welcome to 1v1 Texas Hold'em Heads-Up Poker!")
    print(f"Player 1 starts with {player_chips[0]} chips.")
    print(f"Player 2 starts with {player_chips[1]} chips.\n")

    while True:
        game = PokerGame()
        pot = 0

       
        game.deal_hole_cards()
        for player in range(2):
            show_hand(player, game.player_hands[player])

       
        for player in range(2):
            bet = prompt_bet(player, player_chips)
            pot += bet
            player_chips[player] -= bet

        
        game.deal_flop()
        print(f"Flop: {game.community_cards}")
        input("Press Enter to continue...")

        
        for player in range(2):
            bet = prompt_bet(player, player_chips)
            pot += bet
            player_chips[player] -= bet

        
        game.deal_turn()
        print(f"Turn: {game.community_cards}")
        input("Press Enter to continue...")

        
        for player in range(2):
            bet = prompt_bet(player, player_chips)
            pot += bet
            player_chips[player] -= bet

        
        game.deal_river()
        print(f"River: {game.community_cards}")
        input("Press Enter to continue...")

        
        for player in range(2):
            bet = prompt_bet(player, player_chips)
            pot += bet
            player_chips[player] -= bet

        
        clear_screen()
        for player in range(2):
            print(f"Player {player + 1} hand: {game.player_hands[player]}")
        print(f"Community cards: {game.community_cards}")

        
        scores = game.evaluate_hands()
        print(f"Scores: {scores}\n")

        if scores[0] < scores[1]:
            print("Player 1 wins the pot!")
            player_chips[0] += pot
        elif scores[0] > scores[1]:
            print("Player 2 wins the pot!")
            player_chips[1] += pot
        else:
            print("It's a tie! The pot is split.")
            player_chips[0] += pot // 2
            player_chips[1] += pot // 2

        print(f"\nUpdated Chip Counts:")
        print(f"Player 1: {player_chips[0]} chips")
        print(f"Player 2: {player_chips[1]} chips")

        
        if player_chips[0] <= 0:
            print("Player 1 is out of chips! Player 2 wins the game!")
            break
        elif player_chips[1] <= 0:
            print("Player 2 is out of chips! Player 1 wins the game!")
            break

        
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()

