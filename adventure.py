# The main file to go on a Pokémon adventure throughout Kanto Region (Red/Blue/Green)

import classes


def main():
    print("Welcome to the Kanto region!")

    town_name = input("Which town would you like to go to?: ").title()

    while town_name in classes.LEADERS:
        town = classes.Town(town_name, classes.LEADERS[town_name])
        classes.Town.visit_town(town)

        explore = None
        while explore != 0:
            print(
                """
            What would you like to do?: 
            0. Leave Town
            1. Go to the PokeCenter
            2. Go to the PokeMart
            3. Go to the Gym
            """)
            explore = int(input("What would you like to do? "))
            if explore == 0:
                classes.Town.leave_town(town)

            elif explore == 1:
                classes.Town.visit_center(town)
                classes.Town.heal_pokemon()
                classes.Town.visit_town(town)

            elif explore == 2:
                classes.Town.visit_mart(town)
                buy_sell = None
                while buy_sell != 0:
                    buy_sell = int(input(
                        """
                    What can we do for you?: 
                    1. Buy Pokeballs
                    2. Sell Pokeballs
                    """))
                    if buy_sell == 1:
                        balls = int(input("How many pokeballs would you like?: "))
                        classes.Town.buy_pokeballs(balls)
                        break
                    elif buy_sell == 2:
                        balls = int(input("How many pokeballs will you sell?: "))
                        classes.Town.sell_pokeballs(balls)
                        break
                    else:
                        print("Please choose either 1 or 2.")

            elif explore == 3:
                for key, values in classes.LEADERS.items():
                    if type(values) is str:
                        classes.Town.visit_gym(town)
                        challenge = input("Face the gym leader (y/n)?: ").lower()
                        if challenge == "y":
                            classes.Town.face_leader(town)
                            break
                        elif challenge == "n":
                            print("Maybe another day then.")
                            break
                        else:
                            print("Please type either y or n")
                    if type(values) is None:
                        print("This town has no gym, is there something else you would like to do?")
                        break

    if town_name not in classes.LEADERS:
        end = input("That's not a town in the Kanto Region, would you like to choose somewhere else (y/n)?")
        if end == "y":
            main()
        elif end == "n":
            print("You return home to fall asleep, and dream of future adventures another day.")
        else:
            print("Please select y or n")


if __name__ == "__main__":
    main()
    input("Press any key to exit program.")
