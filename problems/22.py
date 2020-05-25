from utils.utils import container, random_str
from collections import defaultdict
import random


def func(n):
    ans = [('', n, 0)]
    for i in range(2 * n):
        collect = []
        for k in ans:
            if k[1] > 0:
                collect.append((k[0] + '(', k[1] - 1, k[2] + 1))
            if k[2] > 0:
                collect.append((k[0] + ')', k[1], k[2] - 1))
        ans = collect
    ans = [k[0] for k in ans]
    return ans


container(func, 5)




