from utils.utils import container, random_str
from collections import defaultdict
import random


def func(s):
    collect = ['M', 'CM', 'D', 'CD',
               'C', 'XC', 'L', 'XL',
               'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ptr = 0
    ans = 0
    while len(s):
        pattern = collect[ptr]
        if s[:len(pattern)] == pattern:
            ans += num[ptr]
            s = s[len(pattern):]
        else:
            ptr += 1
    return ans


container(func, 'LVIII')




