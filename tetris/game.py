import random

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

    def game_over(self) -> bool:
        for i in self.game_board.board[0]:
            if i == 1:
                return True
        return False

