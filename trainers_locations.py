# A support file containing the classes to use in the adventure.py PokeGame
# File contains classes for locations and trainers

import random


class Town(object):

    TOWNS = ("pallet town", "celadon town", "pewter city",
             "lavender town", "fuchsia city", "viridian city",
             "vermilion city", "saffron city", "cinnabar island")

    GYM_LEADERS = {
        "celadon town": "Misty", "pewter City": "Brock",
        "fuchsia city": "Erika", "viridian City": "Giovanni",
        "vermilion city": "Lt.Surge", "saffron City": "Sabrina",
        "cinnabar island": "Blake"
    }

    def __init__(self, name):
        self.name = name

    def choose_town(self):
        """Ask which town to go to."""
        response = None
        while response not in Town.TOWNS:
            response = input("Which town would you like to travel to?: ").lower()
        return response

    def visit_town(self):
        """Ask what to do in a town."""
        print(f"Welcome to {self.name}. We hope you enjoy your stay!")
        explore = input(print("What would you like to do? (0-3): "))
        while explore != 0:
            if explore == 1:
                Town.visit_gym(self)
            elif explore == 2:
                Town.visit_center(self)
            elif explore == 3:
                Town.visit_mart(self)
            else:
                print("Which town would you like to travel to?")

    def visit_gym(self, name):
        """Play a random match against the Gym Leader"""
        print(f"You have entered, {self.name}'s gym. Prepare to face {name}")
        win_lose = random.randint(0, 2)
        if win_lose == 0:
            print(f"A crushing victory by {self.name}. You have rushed to the PokeCenter in worry!")

        elif win_lose == 1:
            print("A stunning victory for our challenger."
                  "Give a round of applause for such an incredible performance.")

        else:
            print("There is an error with your range.")

        return win_lose

    def visit_center(self):
        """Visit the PokeCenter, accounting for a match against the Leader"""
        if self.visit_gym(self) == 0:
            print("Here are your Pokemon. Please be more careful in the future.")

        else:
            center = input(print(f"Welcome to the {self.name} PokeCenter. How can we help you?"))
            if center == 0:
                print("Come again.")
            elif center == 1:
                print("Thank you for coming to us. Here are your Pokemon.")
            elif center == 2:
                print("[Next Day] Thank you, please come again.")

    def visit_mart(self):
        """Visit the PokeMart and purchase items or leave"""
        mart = int(input(print("What would you like to do? (0-2)")))
        while mart != 0:
            if mart == 1:
                print("Here are your PokeBalls beloved customer.")
            elif mart == 2:
                print("Here are your Health Sprays beloved customer.")
            else:
                print("That is not an option. Please choose 0, 1, or 2.")

        else:
            print("Thank you for coming. Please come again soon.")

    def leave_town(self):
        print(f"You have left {self.name}. We hope you enjoyed your visit!")
        print("Where would you like to go next?")

    def play(self):
        print("Welcome to Kanto!")

        town = Town.choose_town(self)

        town.visit_town()



def main():
    print("Welcome to Kanto!")

    town = Town.choose_town()

    town.visit_town()

    Town.play(town)


main()
input("Press any key to exit.")