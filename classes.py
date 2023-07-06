# A support file containing the classes to use in the adventure.py PokeGame
# # File contains classes for locations and trainers

import random

TOWNS = ["Pallet Town", "Celadon City", "Pewter City", "Cerulean City",
         "Lavender Town", "Fuchsia City", "Viridian City",
         "Vermilion City", "Saffron City", "Cinnabar Island"]

LEADERS = {"Pallet Town": None, "Celadon City": "Erika", "Pewter City": "Brock", "Cerulean City": "Misty",
           "Lavender Town": None, "Fuchsia City": "Koga", "Viridian City": "Giovanni",
           "Vermilion City": "Surge", "Saffron City": "Sabrina", "Cinnabar Island": "Blaine"}


class Town(object):
    """A town in Kanto"""

    def __init__(self, town, leader):
        self.town = town
        self.leader = leader

    @staticmethod
    def choose_town():
        town_name = input("Which town would you like to go to?: ").lower()
        return town_name

    def visit_town(self):
        """Welcome the player into town."""
        input(f"Welcome to {self.town} Trainer. We hope you enjoy your stay! ")

    def leave_town(self):
        """Give a farewell to the trainer as they leave town."""
        print(f"""Thank you for staying at {self.town},
              we hope you enjoyed your stay. Please return again.""")

    def visit_gym(self):
        """Greet the player when they enter the gym."""
        print(f"""You have entered, {self.town}'s gym.
        Prepare to face {self.leader}!""")

    def face_leader(self):
        """Randomly decide if the player wins or loses against the gym leader."""
        win_lose = random.randint(0, 1)
        if win_lose == 0:
            print(f"""A crushing victory by {self.leader}.
            You have rushed to the PokeCenter in worry!""")

        elif win_lose == 1:
            print("A stunning victory for our challenger. "
                  "Give a round of applause for such an incredible performance.")

        else:
            print("There is an error with your range.")

    def visit_center(self):
        """Greet the play when they enter the pokecenter."""
        print(f"Welcome to {self.town}'s PokeCenter.")

    @staticmethod
    def lost_battle():
        """Create a method for if the player loses to the gym leader."""
        print("Oh my!! Please, allow me to take your pokemon.")
        print("...")
        print("Here are your pokemon. Please take better care of them!")

    @staticmethod
    def heal_pokemon():
        """What Nurse Joy will do when you enter the pokecenter"""
        print("I'll take a look at your pokemon.")
        print("...")
        print("Here are your pokemon. Please return if they ever need healing!")

    def visit_mart(self):
        """Greet the player when they enter the pokemart"""
        input(f"Welcome to {self.town}'s PokeMart.")

    @staticmethod
    def buy_pokeballs(balls):
        """Allow the player to buy as many pokeballs as they want, with funny dialogue for flavor."""
        if balls > 5:
            print("So many!!")
        elif 0 < balls <= 5:
            print("Here you go.")
        elif balls == 0:
            print("You wish to buy 0 pokeballs?")
            Town.buy_pokeballs(balls)
        else:
            print("Do you mean you wish to sell?")
            Town.buy_pokeballs(balls)

    @staticmethod
    def sell_pokeballs(balls):
        """Allow the player to sell as many pokeballs as they want, with funny dialogue for flavor."""
        if balls > 5:
            print("So many!!")
        elif 0 < balls <= 5:
            print("Here is your Poke-Yen.")
        elif balls == 0:
            print("You wish to sell 0 pokeballs?")
        else:
            print("Do you mean you wish to buy?")
