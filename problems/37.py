from utils.utils import container, random_str
from collections import defaultdict
import random


def func(board):
    delete = [[set() for j in range(9)] for i in range(9)]
    for i in range(9):
        d = set(board[i])
        for j in range(9):
            delete[i][j].update(d)
    for j in range(9):
        d = set([board[i][j] for i in range(9)])
        for i in range(9):
            delete[i][j].update(d)
    for k in [0, 3, 6]:
        for m in [0, 3, 6]:
            d = set([board[i][j] for i in range(k, k + 3) for j in range(m, m + 3)])
            for i in range(k, k + 3):
                for j in range(m, m + 3):
                    delete[i][j].update(d)

    def get_map(_delete):
        num_map = defaultdict(list)
        for i in range(9):
            for j in range(9):
                num_map[len(_delete[i][j])].append([i, j])
        return num_map



container(func,
          [
              ["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]
          ]
          )
