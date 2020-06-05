from utils.utils import container, random_str
from collections import defaultdict
import random


def func(board):
    def check(line):
        s = set()
        for item in line:
            if item == '.':
                continue
            if item not in s:
                s.add(item)
            else:
                return True
        return False

    for i in range(9):
        if check(board[i]):
            return False
    for j in range(9):
        if check([board[i][j] for i in range(9)]):
            return False
    for k in [0, 3, 6]:
        for m in [0, 3, 6]:
            if check([board[i][j] for i in range(k, k + 3) for j in range(m, m + 3)]):
                return False
    return True


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
