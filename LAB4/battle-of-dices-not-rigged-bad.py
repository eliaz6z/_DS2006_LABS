# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws one D6.
# The player with the highest roll wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds = 0


# Round 1

player1_round1_roll = random.randint(1, 6)
player2_round1_roll = random.randint(1, 6)

rounds += 1

input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_round1_roll)

print("Player 2 rolled: ", player2_round1_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round1_roll > player2_round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round1_roll," is greater than ", player2_round1_roll)
elif player1_round1_roll == player2_round1_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round1_roll," is greater than ", player1_round1_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is now our undisputed dice rolling champion, give them a round of applause!")
elif player2_wins == 3:
    print("Player 2 is now our undisputed dice rolling champion, give them a round of applause!")
else:
    print("This legendary battle is still ongoing, we're gonna have more rounds to have a champion")

# Round 2

player1_round2_roll = random.randint(1, 6)
player2_round2_roll = random.randint(1, 6)

rounds += 1

input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_round2_roll)

print("Player 2 rolled: ", player2_round2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round2_roll > player2_round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round2_roll," is greater than ", player2_round2_roll)
elif player1_round2_roll == player2_round2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round2_roll," is greater than ", player1_round2_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is now our undisputed dice rolling champion, give them a round of applause!")
elif player2_wins == 3:
    print("Player 2 is now our undisputed dice rolling champion, give them a round of applause!")
else:
    print("This legendary battle is still ongoing, we're gonna have more rounds to have a champion")

    # Round 3

player1_round3_roll = random.randint(1, 6)
player2_round3_roll = random.randint(1, 6)

rounds += 1

input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_round3_roll)

print("Player 2 rolled: ", player2_round3_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round3_roll > player2_round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round3_roll," is greater than ", player2_round3_roll)
elif player1_round3_roll == player2_round3_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round3_roll," is greater than ", player1_round3_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player   1 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll}")
elif player2_wins == 3:
    print("Player 2 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll}")
else:
    print("This legendary battle is still ongoing, we're gonna have more rounds to have a champion")

    # Round 4

player1_round4_roll = random.randint(1, 6)
player2_round4_roll = random.randint(1, 6)

rounds += 1

input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_round4_roll)

print("Player 2 rolled: ", player2_round4_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round4_roll > player2_round4_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round4_roll," is greater than ", player2_round4_roll)
elif player1_round4_roll == player2_round4_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round4_roll," is greater than ", player1_round4_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3 - 4")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll} - {player1_round4_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll} - {player2_round4_roll}")
elif player2_wins == 3:
    print("Player 2 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3 - 4")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll} - {player1_round4_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll} - {player2_round4_roll}")
else:
    print("This legendary battle is still ongoing, we're gonna have more rounds to have a champion")

    # Round 5

player1_round5_roll = random.randint(1, 6)
player2_round5_roll = random.randint(1, 6)

rounds += 1

input(f"\nRound {rounds}: \nPress ENTER to roll the dice...")

print("Player 1 rolled: ", player1_round5_roll)

print("Player 2 rolled: ", player2_round5_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_round5_roll > player2_round5_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_round5_roll," is greater than ", player2_round5_roll)
elif player1_round5_roll == player2_round5_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_round5_roll," is greater than ", player1_round5_roll)

# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3 - 4 - 5")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll} - {player1_round4_roll} - {player1_round5_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll} - {player2_round4_roll} - {player2_round5_roll}")
elif player2_wins == 3:
    print("Player 2 is now our undisputed dice rolling champion, give them a round of applause!")
    print("\nRound:   1 - 2 - 3 - 4 - 5")
    print(f"Player1: {player1_round1_roll} - {player1_round2_roll} - {player1_round3_roll} - {player1_round4_roll} - {player1_round5_roll}")
    print(f"Player2: {player2_round1_roll} - {player2_round2_roll} - {player2_round3_roll} - {player2_round4_roll} - {player2_round5_roll}")
else:
    print("This legendary battle is still ongoing, we're gonna have more rounds to have a champion")