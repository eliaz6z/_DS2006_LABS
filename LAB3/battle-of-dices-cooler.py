import random

print("\n🎲 Welcome to the Battle of Dices! 🎲")
print("\nToday's contenders are Jack and John, give them a round of applause!")

# Variables to keep track of the score:
jack_wins = 0
john_wins = 0
rounds = 0
gameover = False

# Creating a function for rolling dice of different sizes:
def roll_die(sides):
    """Return a random int between 1 and 'sides' (any number of sides)."""
    return random.randint(1, sides)

# Choosing the two sizes:
a_sides = 6
b_sides = 8

# Creating the game:
while not gameover:
    rounds += 1
    input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

    jack_r1 = roll_die(a_sides)
    jack_r2 = roll_die(b_sides)
    jack_total = jack_r1 + jack_r2
    print(f"Jack rolled {jack_r1} and {jack_r2}, his total is: {jack_total}")
    
    john_r1 = roll_die(a_sides)
    john_r2 = roll_die(b_sides)
    john_total = john_r1 + john_r2
    print(f"John rolled {john_r1} and {john_r2}, his total is: {john_total}")

    input("\nPress ENTER to continue...")

    # Deciding the round winner:
    if jack_total > john_total:
        jack_wins += 1
        print(f"\nJack wins round {rounds}, because his {jack_total} is greater than John's {john_total}")
    elif john_total > jack_total:
        john_wins += 1
        print(f"\nJohn wins round {rounds}, because his {john_total} is greater than Jack's {jack_total}")
    else:
        print(f"\nUnbelievable scenes, round {rounds} is a tie!")

    print(f"The score is Jack {jack_wins}-{john_wins} John")

    # Finding a winner, first to 3:
    if jack_wins == 3:
        print("\nJack is now the Undisputed Dice Rolling champion, give him a round of applause!")
        print(f"It took {rounds} rounds for Jack to be victorious.")
        gameover = True
    elif john_wins ==3:
        print("\nJohn is now the Undisputed Dice Rolling champion, give him a round of applause!")
        print(f"It took {rounds} rounds for John to be victorious.")
        gameover = True
    else:
        print("\nThis legendary battle is still ongoing, we need more rounds to crown a winner!")

print("Game Over")
        