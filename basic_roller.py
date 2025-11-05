import random

MIN_PLAYER_ID = 0
MIN_DIE_ID = 0

class Player:
    def __init__(self, name):
        global MIN_PLAYER_ID
        self.name = name
        self.id = MIN_PLAYER_ID + 1
        MIN_PLAYER_ID += 1
        self.dice = []
        # dice are added later manually

    def __repr__(self):
        return f"{self.name!r}: {self.dice!r}"

    def __str__(self):
        return self.__repr__()
    
    def add_die(self, number, color):
        d = Die(number, color, self.id)
        self.dice.append(d)
        return d.dieID
    
    def roll(self):
        total_roll = 0
        for cubey_thingy in self.dice:
            total_roll += cubey_thingy.roll()
        return total_roll

class Die:
    def __init__(self, number, color, playerID):
        self.number = number
        self.color = color
        self.playerID = playerID
        global MIN_DIE_ID
        self.dieID = MIN_DIE_ID + 1
        MIN_DIE_ID += 1

    def __repr__(self):
        return f"{self.number!r} {self.color!r}"

    def __str__(self):
        return self.__repr__()
    
    def roll(self):
        return random.randint(1, self.number)

class DieGame:
    # This is going to contain the sets of dice for each player
    # Each dice set will reference a dice set - player1_dieID, player2_dieID, etc.
    def __init__(self):
        self.players = []

    # Takes in name, returns the new player
    def add_player(self, name):
        p = Player(name)
        self.players.append(p)
        return p

    # Find the player location in dice set array
    def get_player_from_id(self, playerID):
        for player in self.players:
            if(playerID == player.id):
                return player
        return None
    
    def remove_player(self, playerID):
        for player in self.players:
            if(playerID == player.id):
                self.players.remove(player)
                return True
    
    def get_player_ids(self):
        ids = []
        for player in self.players:
            ids.append(player.id)
        return ids

    # Takes in number, that is the die
    # Color not relevant right now
    # Adds to array of dice
    # Returns ID
    def add_dice(self, playerID, number, color):
        p = self.get_player_from_id(playerID)
        if (p == None):
            print(f"Player ID {playerID} not found.")
            return None
        p_id = p.add_die(number, color)
        return p_id

    # Remove die based on ID
    def remove_die(self, dieID):
        print("figure this out later")



# Testing
dg = DieGame()


dg.add_player("Hunter")
dg.add_player("Rebecca")

print(dg.get_player_ids())

dg.add_dice(1, 6, "red")
dg.add_dice(1, 6, "red")

print(dg.get_player_from_id(1).roll())

# dg.add_dice(dg.find_player("Hunter"), 6, "red")

# print(dg.players)

def main():
    print("<br>PHP works with this!")
    
if __name__ == "__main__":
    main()