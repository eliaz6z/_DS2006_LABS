import random

print("\n🎲 Welcome to the Battle of Dices! 🎲")
print("\nToday's contenders are Jack and John, give them a round of applause!")

# Variables to keep track of the score:
jack_wins = 0
john_wins = 0
rounds = 0

GameOver = False

def RollD7():
    """"Roll a 7-sided dice.

    Returns:
        int: a random number between 1 and 7"""

    return random.randint(1, 7)

# Round 1

while not GameOver: 
    rounds += 1 
    input(f"\nRound {rounds}, \nPress ENTER to roll the dice...")

    jack_roll = RollD7()
    print(f"Jack rolled: {jack_roll}")
    john_roll = RollD7()
    print(f"John rolled: {john_roll}")

    input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

    if jack_roll > john_roll:
        jack_wins += 1
        print("Jack wins this round!")
        print(f"Because {jack_roll} is greater than {john_roll}")
    elif jack_roll == john_roll:
        print("Unbelievable! It's a tie!")
    else:
        john_wins += 1
        print("John wins this round!")
        print(f"Because {john_roll} is greater than {jack_roll}")

# We can print the game score:
    print(f"The game score is Jack {jack_wins}-{john_wins} John")

# Now we need to check if either player won.
    if jack_wins == 3:
        GameOver = True, print("Jack is now our Undisputed Dice Rolling Champion, give him a round of applause!")
        print(f"It took {rounds} rounds for Jack to win!")
    elif john_wins == 3:
        GameOver = True, print("John is now our Undisputed Dice Rolling Champion, give him a round of applause!")
        print(f"It took {rounds} rounds for John to win!")
    else:
        print("This legendary battle is still ongoing, we're gonna need more rounds to crown a winner!")

print("Game Over") 