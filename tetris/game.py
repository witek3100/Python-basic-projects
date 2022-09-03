import random
import math

from board import Board
from brick import Brick

class Game:

    def __init__(self):
        self.speed = 50
        self.score = 0
        self.game_board = Board()
        self.current_brick = None

    def new_brick(self):
        self.current_brick = Brick(30 * random.randint(1,13), 0)

    def brick_fell(self):
        for i in self.current_brick.brick_fields:
            m = self.game_board.board[math.floor(i[1] / 30) + 1, math.floor(i[0] / 30)]
            if m == 1 or m == 2:  # sprawdzenie czy klocek spadl
                for j in self.current_brick.brick_fields:
                    self.game_board.board[math.floor(j[1] / 30), math.floor(j[0] / 30)] = 1
                self.current_brick = None
                break

