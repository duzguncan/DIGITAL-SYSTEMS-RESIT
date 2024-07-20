import tkinter as tk
from poker_game import PokerGame

class PokerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Texas Hold'em Poker")
        
        self.player_chips = [100, 100]
        self.game = PokerGame()
        self.pot = 0
        self.current_player = 0
        
        self.create_widgets()
        self.start_new_round()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Welcome to Texas Hold'em Poker")
        self.info_label.pack()
        
        self.p1_label = tk.Label(self.root, text="Player 1")
        self.p1_label.pack()
        self.p1_hand_button = tk.Button(self.root, text="View Hand", command=lambda: self.show_hand(0))
        self.p1_hand_button.pack()
        
        self.p2_label = tk.Label(self.root, text="Player 2")
        self.p2_label.pack()
        self.p2_hand_button = tk.Button(self.root, text="View Hand", command=lambda: self.show_hand(1))
        self.p2_hand_button.pack()
        
        self.turn_label = tk.Label(self.root, text="")
        self.turn_label.pack()

        self.community_label = tk.Label(self.root, text="Community Cards")
        self.community_label.pack()
        self.community_hand_label = tk.Label(self.root, text="")
        self.community_hand_label.pack()
        
        self.bet_entry = tk.Entry(self.root)
        self.bet_entry.pack()
        self.bet_button = tk.Button(self.root, text="Place Bet", command=self.place_bet)
        self.bet_button.pack()
        
        self.next_button = tk.Button(self.root, text="Next Round", command=self.next_round)
        self.next_button.pack()

    def start_new_round(self):
        self.game = PokerGame()
        self.pot = 0
        self.current_player = 0
        
        self.game.deal_hole_cards()
        self.community_hand_label.config(text="")
        self.next_button.config(text="Next Round", command=self.next_round)
        
        self.update_info()

    def show_hand(self, player):
        hand_window = tk.Toplevel(self.root)
        hand_window.grab_set()  
        hand_window.title(f"Player {player + 1} Hand")
        hand_label = tk.Label(hand_window, text=f"Player {player + 1}, your hand: {self.game.player_hands[player]}")
        hand_label.pack()
        close_button = tk.Button(hand_window, text="OK", command=hand_window.destroy)
        close_button.pack()
        self.root.wait_window(hand_window)  

    def place_bet(self):
        try:
            bet = int(self.bet_entry.get())
            if 0 < bet <= self.player_chips[self.current_player]:
                self.pot += bet
                self.player_chips[self.current_player] -= bet
                self.current_player = (self.current_player + 1) % 2
                self.update_info()
            else:
                self.info_label.config(text="Invalid bet amount.")
        except ValueError:
            self.info_label.config(text="Please enter a valid number.")
    
    def next_round(self):
        if len(self.game.community_cards) == 0:
            self.game.deal_flop()
        elif len(self.game.community_cards) == 3:
            self.game.deal_turn()
        elif len(self.game.community_cards) == 4:
            self.game.deal_river()
        else:
            self.showdown()
            return
        
        self.community_hand_label.config(text=str(self.game.community_cards))
        self.update_info()
    
    def showdown(self):
        scores = self.game.evaluate_hands()
        if scores[0] < scores[1]:
            self.info_label.config(text="Player 1 wins the pot!")
            self.player_chips[0] += self.pot
        elif scores[0] > scores[1]:
            self.info_label.config(text="Player 2 wins the pot!")
            self.player_chips[1] += self.pot
        else:
            self.info_label.config(text="It's a tie! The pot is split.")
            self.player_chips[0] += self.pot // 2
            self.player_chips[1] += self.pot // 2
        
        self.update_info()
        self.check_game_over()
        self.next_button.config(text="New Round", command=self.start_new_round)

    def update_info(self):
        self.info_label.config(text=f"Player 1: {self.player_chips[0]} chips, Player 2: {self.player_chips[1]} chips, Pot: {self.pot}")
        self.turn_label.config(text=f"Player {self.current_player + 1}'s turn to bet")
        self.bet_entry.delete(0, tk.END)

    def check_game_over(self):
        if self.player_chips[0] <= 0:
            self.info_label.config(text="Player 1 is out of chips! Player 2 wins the game!")
            self.end_game()
        elif self.player_chips[1] <= 0:
            self.info_label.config(text="Player 2 is out of chips! Player 1 wins the game!")
            self.end_game()

    def end_game(self):
        end_window = tk.Toplevel(self.root)
        end_window.grab_set()  
        end_window.title("Game Over")
        end_label = tk.Label(end_window, text="Game Over! Do you want to play again?")
        end_label.pack()
        restart_button = tk.Button(end_window, text="Restart Game", command=lambda: self.restart_game(end_window))
        restart_button.pack()
        quit_button = tk.Button(end_window, text="Quit", command=self.root.quit)
        quit_button.pack()
        self.root.wait_window(end_window) 

    def restart_game(self, end_window):
        self.player_chips = [100, 100]
        end_window.destroy()
        self.start_new_round()

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerGUI(root)
    root.mainloop()
