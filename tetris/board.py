import numpy as np

class Board:

    def __init__(self):
        self.board = np.vstack((np.zeros((18, 15)), [2 for i in range(15)]))

    def update_board(self):
        for c,i in enumerate(self.board):
            if np.array_equal(i, np.ones(15)):
                self.board = np.delete(self.board, c, 0)
                self.board = np.insert(self.board, 0, np.zeros(15), 0)

