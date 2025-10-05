import dice

print("\n🎲 Welcome to the Battle of Dices multiplayer! 🎲")
print("Today's game will be played with a D6 dice!")
# Variables
winning_score = 3
rounds = 0
player_names = []
player_wins = []
gameover = False
# Here we ask how many people will be playing
number_of_players = int(input("How many are playing today?"))
# Here we ask for the name of each player and put then in a list
for i in range(number_of_players):
    name = input(f"Enter the name of player {i+1}: ")
    player_names.append(name)
# Here we put 0 for each player in the player_wins list because they have no wins to begin with
for i in range(number_of_players):
    player_wins.append(0)
#Here we create a nested list for each player's roll history
player_rolls_history = []
for i in range(number_of_players):
    player_rolls_history.append([])
# The game:
while gameover is False:
    rounds += 1
    print(f"Round {rounds}:")
    # Each player's roll for the current round
    current_rolls = []
    for i in range(number_of_players):
        input(f"'{player_names[i]}', press ENTER to roll the dice...")
        roll = dice.RollD6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"'{player_names[i]}' rolled a {roll}")
    input("Press ENTER to continue")
    # Finding the highest roll for this round
    highest_roll = max(current_rolls)
    # Store information about who won this round
    winners = []
    # Finding the players with the highest roll
    for j in range(len(current_rolls)):
        if current_rolls[j] == highest_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    print(f"Winners of this round are {winners}")
    for z in range(number_of_players):
        if player_wins[z] == winning_score:
            print(f"{player_names[z]} is the newest winner of Battle of Dices!")
            gameover = True
    if gameover is False:
        print("The scores are as followed:")
        for x in range(len(player_names)):
            print(f"{player_names[x]}: {player_wins[x]}")
        print("\nThis battle is still going on, who will win at the end?\n")
    else:
        print("The final scores:")
        for o in range(len(player_names)):
            print(f"{player_names[o]}: {player_wins[o]}")
        print("Game Over")
# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:  # "w" = write mode
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""  # Start with an empty string
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
            if i < number_of_players - 1:  # Add a comma after each, except the last one
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")