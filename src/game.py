# Imports
import toml
from random import choice


# Game class
class Game:
    def __init__(self):
        self.file = toml.load("game_settings.toml") # file loader
        self.items = items = list(self.file.keys()) # loads each item name

        print("Welcome to Modifiable Rock Paper Scissors!\n\nSelect your choice against the AI:")
        self.list_choices()

        try:
            self.player_choice = int(input("\nEnter your choice (default is 1): "))
            if self.player_choice < 1 or self.player_choice > 3:
                self.player_choice = 1

        except ValueError:
            self.player_choice = 1

        print(f"You chose {self.items[self.player_choice-1].title()}.")

    def list_choices(self):

        for i in range(3):
            print(f"\t{i+1}. {self.items[i].title()}")

a = Game()