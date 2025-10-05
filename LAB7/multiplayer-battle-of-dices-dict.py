import dice
import copy
print("\n🎲 Welcome to the Battle of Dices multiplayer! 🎲")
print("Today's game will be played with a D6 dice!")
winning_score = 3
rounds = 0
gameover = False
# Dictionary for storing player info
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}
# List for storing the dicts for each player
players = []
# Obtaining number of players
number_of_players = int(input("How many players? "))
# for loop for obtaining player info
for i in range(number_of_players):
    # Making a deep copy since we have a list/mutable object within our original dict.
    player = copy.deepcopy(player_info)
    # Asking and storing the information about each player
    player["name"] = input(f"What is the name of player {i+1}? ")
    player["email"] = input(f"What is the e-mail of player {i+1}? ")
    player["country"] = input(f"What country is player {i+1} from? ")
    # Appending the information above about each player into our list
    players.append(player)
# The game
while gameover is False:
    rounds += 1
    input(f"Round {rounds}:\nPress ENTER to continue...")
    # Each player's roll for the current round
    current_rolls = []
    # Rolling the dice for each player and adding it to current_rolls
    for each_player in players:
        roll = dice.RollD6()
        current_rolls.append(roll)
        # Adding each player's current roll into the list of rolls
        each_player["rolls"].append(roll)
        print(f"Player {each_player['name']} rolled: {roll}")
    max_roll = max(current_rolls)
    winners = []
    # Adding each player who got the highest roll into the winners list every round
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            each_player["wins"] += 1
            print(f"{each_player['name']} won round {rounds}")
            winners.append(each_player['name'])
    print(f"Winners of this round: {winners}")
    # Checking for winner(s)
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n{each_player['name']} is our newest champion!")
            gameover = True
    if gameover is False:
        print("This heated Battle of Dices is still going on! Who will win at the end?")
# Save the results
filename = input("Enter a .txt filename to save the results: ")
with open(filename, "w") as file: # "w"= write mode
    file.write("Player information:\n")
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"E-mail: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n\n"
        )
    file.write("Game rounds: \n")
    # Round history
    for r in range(rounds):
        rolls_str = ""
        # Going through each player and building the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            # Add a comma unless it's the last player
            if i < len(players) - 1:
                rolls_str += ", "
        # Now write the full round info to the file
        file.write(f"Round {r+1}:\n{rolls_str}\n")
    print("\nGame over! Results saved successfully.")