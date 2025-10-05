import random
import dice

print("\n🎲 Welcome to the Battle of Dices! 🎲")
print("\nToday's contenders are Player1 and Player2, give them a round of applause!")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
player1_rolls = []
player2_rolls = []
rounds = 0

gameover = False

# Round 1

while not gameover: 
    rounds += 1 
    input(f"\nRound {rounds}: \nPress ENTER to roll the dice for Player1...")
    player1_roll = dice.RollD6()
    player1_rolls.append(player1_roll)

    print(f"Player1 rolled: {player1_roll}")

    input("\nPress ENTER to roll the dice for Player2...")
    player2_roll = dice.RollD6()
    player2_rolls.append(player2_roll)

    print(f"Player2 rolled: {player2_roll}")

    input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player1 wins this round!")
        print(f"Because {player1_roll} is greater than {player2_roll}")
    elif player1_roll == player2_roll:
        print("Unbelievable! It's a tie!")
    else:
        player2_wins += 1
        print("Player2 wins this round!")
        print(f"Because {player2_roll} is greater than {player1_roll}")

# We can print the game score:
    print(f"The game score is Player1 {player1_wins}-{player2_wins} Player2")

# Now we need to check if either player won.
    if player1_wins == 3:
        gameover = True, print("\nPlayer1 is now our Undisputed Dice Rolling Champion, give her a round of applause!")
        print(f"It took {rounds} rounds for Player1 to win!")
    elif player2_wins == 3:
        gameover = True, print("\nPlayer2 is now our Undisputed Dice Rolling Champion, give him a round of applause!")
        print(f"It took {rounds} rounds for Player2 to win!")
    else:
        print("This legendary battle is still ongoing, we're gonna need more rounds to crown a winner!")

# Printing the results
print("\nResults")
print("Round - Player1 - Player2")
print("--------------------------")
for i in range(len(player1_rolls)):
    print(f"{i+1:^5} - {player1_rolls[i]:^7} - {player2_rolls[i]:^7}")

# Saving the score in a file
filename = input("\nChoose a .txt file name to save the game results: ")
file = open(filename, "w")
file.write("Round - Player1 - Player2\n")
file.write("--------------------------\n")
for i in range(len(player1_rolls)):
    game_stats = f"{i+1:^5} - {player1_rolls[i]:^7} - {player2_rolls[i]:^7}\n"
    file.write(game_stats)
file.write(f"Final score: Player1 {player1_wins} - {player2_wins} Player2\n")
file.close()