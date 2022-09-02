from board import Board
from brick import Brick

class Game:

    score: int
    speed: float
    current_brick: Brick
    game_board: Board

    def __init__(self):
        self.speed = 1.5
        self.score = 0
        self.game_board = Board()
        self.current_brick = Brick(0, 0)

    def new_brick(self):
        self.current_brick = Brick(30, 30)

