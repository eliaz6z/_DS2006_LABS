import dice

# Player class to store info
class Player:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country
        self.wins = 0
        self.rolls = []

    # Adding rolls for each player
    def add_roll(self, roll):
        self.rolls.append(roll)

    # Adding wins for each player
    def add_win(self):
        self.wins += 1

# Game class
class Game:
    def __init__(self, winning_score=3):
        self.players = []
        self.rounds = 0
        self.gameover = False
        self.winning_score = winning_score

    # Adding each player
    def add_player(self, player):
        self.players.append(player)

    # Playing each round
    def play_round(self):
        self.rounds += 1
        input(f"Round {self.rounds}:\nPress ENTER to continue...")

        current_rolls = []
        # Rolling the dice for each player
        for player in self.players:
            roll = dice.RollD6()
            current_rolls.append(roll)
            player.add_roll(roll)
            print(f"Player {player.name} rolled: {roll}")

        # Finding a round winner
        max_roll = max(current_rolls)
        winners = []
        for player in self.players:
            if player.rolls[-1] == max_roll:
                player.add_win()
                print(f"Player {player.name} won round {self.rounds}!")
                winners.append(player.name)
        print(f"Winner(s) of this round: {winners}")

        # Finding a game winner
        for player in self.players:
            if player.wins >= self.winning_score:
                print(f"\n{player.name} is our champion!")
                self.gameover = True

        if not self.gameover:
            print("This Battle of dices is still going on!")

    # Saving the game scores to a file
    def save_score(self, filename):
        with open(filename, "w") as file:
            file.write("Player information:\n")
            for player in self.players:
                file.write(
                    f"Name: {player.name}\n"
                    f"E-mail: {player.email}\n"
                    f"Country: {player.country}\n"
                    f"Wins: {player.wins}\n\n"   
                )
            file.write("Game rounds: \n")
            for r in range(self.rounds):
                rolls_str = ""
                for i, player in enumerate(self.players):
                    rolls_str += f"{player.name} rolled {player.rolls[r]}"
                    if i < len(self.players) -1:
                        rolls_str += ","
                file.write(f"Round {r+1}:\n{rolls_str}\n")
        print("\nGame over, results saved successfully!")

# The actual game
print("Welcome to the Battle of Dices multiplayer!")
print("This game will be played with a D6 dice 🎲")
# Creating a new game
game = Game(winning_score=3)

# Adding players
number_of_players = int(input("How many are playing today? "))
for i in range(number_of_players):
    name = input(f"What is the name of player {i+1}? ")
    email = input(F"What is the e-mail address of player {i+1}? ")
    country = input(f"What country is player {i+1} from? ")
    game.add_player(Player(name, email, country))

# Running the game
while not game.gameover:
    game.play_round()

# Saving the results
filename = input("Enter a .txt filename to save the results: ")
game.save_score(filename)