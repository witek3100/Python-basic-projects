import numpy as np

class Board:

    def __init__(self):
        upper_rows = np.zeros((18, 15))
        bottom_row = [2 for i in range(15)]
        self.board = np.vstack((upper_rows, bottom_row))
        print(self.board)
