class Player:
    def __init__(self, name, id, dice):
        self.name = name
        self.id = id
        # dice are added later manually
    
        

# This is going to contain the sets of dice for each player
# Each dice set will reference a dice set - player1_dieID, player2_dieID, etc.
players = []

# Find the player location in dice set array
getPlayerFromID(playerID):
    for player in players:
        if(playerID == player.id)

# Takes in number, that is the die
# Color not relevant right now
# Adds to array of dice
# Returns ID
add_dice(playerID, number, color):
    getPlayerFromID(playerID)
    
# Remove die based on ID
remove_die()