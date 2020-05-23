from utils.utils import container, random_str
from collections import defaultdict
import random


def func(num):
    collect = [1000, 500, 100, 50, 10, 5, 1]
    minus = [100, 100, 10, 10, 1, 1, 0]
    collect_c = 'MDCLXVI'
    minis_c = 'CCXXII_'
    ptr = 0
    ans = ''
    while num > 0:
        if num >= collect[ptr]:
            ans += collect_c[ptr]
            num -= collect[ptr]
        elif num >= collect[ptr] - minus[ptr]:
            ans += minis_c[ptr] + collect_c[ptr]
            num -= collect[ptr] - minus[ptr]
        else:
            ptr += 1
    return ans


container(func, 1994)
