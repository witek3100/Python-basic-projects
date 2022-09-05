from field import Field
import ships

class Game:

    def __init__(self):
        self.player_ships_board = [[Field(x, y) for x in range(12)] for y in range(12)]
        self.enemy_ships_board = [[Field(x, y) for x in range(12)] for y in range(12)]
        self.player_ships = [[]]
        self.enemy_ships = [[]]
