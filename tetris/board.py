import numpy as np

class Board:

    def __init__(self):
        self.board = np.vstack((np.zeros((18, 15)), [2 for i in range(15)]))

    def update_board(self) -> int:
        for c,i in enumerate(self.board):
            if np.array_equal(i, np.ones(15)):
                print(c)
                np.delete(self.board, c, 0)

