MIN_ID = 0

class Player:
    def __init__(self, name):
        global MIN_ID
        self.name = name
        self.id = MIN_ID + 1
        MIN_ID += 1
        self.dice = []
        # dice are added later manually

    def __repr__(self):  # ✅ Define __repr__ for lists
        return f"{self.name!r}: {self.dice!r}"

    def __str__(self):
        return __repr__()


# This is going to contain the sets of dice for each player
# Each dice set will reference a dice set - player1_dieID, player2_dieID, etc.
players = []

# Takes in name, returns the new player
def add_player(name):
    p = Player(name)
    players.append(p)
    return p

# Find the player location in dice set array
def getPlayerFromID(playerID):
    for player in players:
        if(playerID == player.id):
            return player

# Takes in number, that is the die
# Color not relevant right now
# Adds to array of dice
# Returns ID
def add_dice(playerID, number, color):
    getPlayerFromID(playerID)
    
# Remove die based on ID
def remove_die():
    print("figure this out later")
    
    
add_player("Hunter")
add_player("Rebecca")

print(players)