# Imports
import toml
from random import randint


# Game class
class Game:
    def __init__(self):
        # Initialization of variables
        self.file = toml.load("items.toml") # loads the file containing each item
        self.items = list(self.file.keys()) # loads each item name
        self.player_index_choice = self.computer_index_choice = None # default assignment
        self.player_item_choice = self.computer_item_choice = None # same as above

        # Introduction message and choice listing
        print("Select your choice against the AI:")
        self.list_choices()

        # Gathering choices
        self.player_item_choice, self.player_index_choice = self.player_pick() # choices from the player
        self.computer_item_choice, self.computer_index_choice = self.computer_pick() # choices from the AI

        # Analyzing results and printing them out
        print(f"You chose {self.items[self.player_index_choice-1].title()}.\n")

        self.final_result = self.analyze_results()
        input("Continuing...\n") # this is necessary because since the game class is run multiple times, you will need to see the results before having them closed


    def list_choices(self):
        for i in range(3):
            print(f"\t{i+1}. {self.items[i].title()}")


    def player_pick(self):
        try:
            player_input = int(input("\nEnter your choice (1, 2, 3 or anything else for random): "))
            if player_input < 1 or player_input > 3:
                raise ValueError

        except ValueError:
            player_input = randint(1, 3)

        return self.items[player_input-1], player_input


    def computer_pick(self):
        computer_selection = randint(1, len(self.items))
        return self.items[computer_selection-1], computer_selection


    def compare_choices(self, player, ai):
        if player == self.file[ai]["beats"] and ai == self.file[player]["falls_to"]:
            return "ai"
        elif ai == self.file[player]["beats"] and player == self.file[ai]["falls_to"]:
            return "player"
        else:
            return "draw"


    def analyze_results(self):
        result = self.compare_choices(self.player_item_choice, self.computer_item_choice)
        print(f"RESULT\nYou chose {self.player_item_choice} (index of {self.player_index_choice}).\nThe AI chose {self.computer_item_choice} (index of {self.computer_index_choice}).")

        # Printing out what happens (from "messages.toml")
        self.print_victory_message(result, self.player_item_choice, self.computer_item_choice)

        # Printing out decisive message
        if result == "player":
            print("Congratulations! You won!")
            return "player"

        elif result == "ai":
            print("What a game! The AI has won.")
            return "ai"

        else:
            print("Draw! No-one gets the victory.")
            return "draw"


    def print_victory_message(self, status: str, player_item=None, ai_item=None) -> None:
        messages = toml.load("messages.toml")

        if status == "draw":
            print(messages["draw"])

        elif status == "player":
            print(messages[f"player-{player_item}-beats-{ai_item}"])

        else:
            print(messages[f"ai-{ai_item}-beats-{player_item}"])

