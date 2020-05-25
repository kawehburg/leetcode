from utils.utils import container, random_str
from collections import defaultdict
import random


def func(s, numRows):
    if numRows <= 1:
        return s

    def row(x):
        tmp = x % (2 * numRows - 2)
        if tmp >= numRows:
            return 2 * numRows - 2 - tmp
        else:
            return tmp

    result = ['' for _ in range(numRows)]
    for i, item in enumerate(s):
        result[row(i)] += item
    return ''.join(result)


container(func, 'A', 5)
