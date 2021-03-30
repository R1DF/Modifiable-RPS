# Built-in imports
import os

# Internal imports
from game import Game

# Simplified functions
def clear():
    result = os.system("clear" if os.name != "nt" else "cls")

def try_int_input(default, num_min_max, message=""):
    try:
        prompt = int(input(message))
        if prompt < num_min_max[0] or prompt > num_min_max[1]:
            raise ValueError
    except ValueError:
        prompt = default

    return prompt

def try_str_input(default, acceptable_values, message=""):
    prompt = input(message)
    if prompt.upper() not in acceptable_values:
        prompt = default
    return prompt.upper()

# MRPS class
class MRPS:
    def __init__(self):
        # Initialization of variables for the game
        self.necessary_files = (
            "main.py", # unnecessary but clean when included
            "game.py",
            "items.toml",
            "messages.toml"
        )
        self.player_points = self.ai_points = self.amount_of_games = self.player_wins = self.ai_wins = 0 # 0 is the default for ints
        self.games = []

        # Full game order
        self.opening()
        self.setup()
        for i in range(self.amount_of_games):
            clear()
            print(f"GAME {i+1} OUT OF {self.amount_of_games}")
            self.games.append(Game().final_result)
        final_winner = self.analyze_all_results()
        self.closing_message(final_winner)

    def opening(self):
        print("""\
WELCOME!
Welcome to Modifiable RPS, I will be your guide.
This game is simple: Just some old regular rock paper scissors.

I bet you know how to play, but just in case:
You and the AI in each round choose one out of three items: A rock, piece of paper, or scissors.

The outcome and who wins is depending on the item you and the AI chose this way:
Paper beats rock (goes over it). If you select paper and the AI chooses rock, you win!
Scissors beat paper (they cut it). If the AI selects scissors and you choose paper, you lose!
Rock beats scissors (it breaks the scissors), and you already know what happens here.

If the two items are the same, it's a draw and no-one wins.

THIS GAME IS MODIFIABLE
If you want to modify the game, go to github.com/R1DF/Modifiable-RPS and follow README.md and editing.md for details!


Now then, are you ready? (Y/N, default is Y)""")
        is_ready = try_str_input("Y", ("Y", "N"))
        if is_ready == "N":
            print("Have a good day!")
            quit()

    def setup(self):
        clear()
        # Checking if files exist
        if False in self.check_file_availability(): # gives an error message if not every file was found
            print("ERROR\nOne of more of the necessary files were not found, either they were deleted or renamed.\n"
                  "Please make sure that all of these files are inside the same directory, including this current script (main.py):")
            for i in self.necessary_files:
                print("-", i)
            print("You can also try deleting the game and reinstalling from github.com/R1DF/Modifiable-RPS.")
            quit()

        # Entering amount of game to play
        self.amount_of_games = try_int_input(5, (1, 7),
                                             "SETUP\nEnter amount of games you want to play (from 1 to 7, default is 5): ")
        clear()

    def analyze_all_results(self):
        self.player_wins = self.games.count("player")
        self.ai_wins = self.games.count("ai")
        if self.player_wins > self.ai_wins:
            return "player"
        elif self.player_wins < self.ai_wins:
            return "ai"
        else:
            return "draw"

    def closing_message(self, winner):
        clear()
        print("FINAL SCORES\n")
        print(f"Player points: {self.player_wins}\nAI points: {self.ai_wins}\n"
              f"Draws: {self.games.count('draws')}\n")
        if winner == "player":
            print(f"Well done! You won {self.player_wins} games and {round(self.player_wins / self.amount_of_games * 100)}% of the full game.")
        elif winner == "ai":
            print(f"Tough game! You won {self.player_wins} games but the AI won {round(self.ai_wins / self.amount_of_games*100)}% of the full game.")
        else:
            print("Oh wow! The scores are the same (or none of you even won a single time)! No-one wins.")

    def check_file_availability(self):
        results = []
        for i in self.necessary_files:
            results.append(True if os.path.exists(i) else False)

        for i in self.necessary_files:
            results.append(i if os.path.exists(i) else False)

        return results

# Creating MRPS game
clear() # for terminal tidiness
game = MRPS()
