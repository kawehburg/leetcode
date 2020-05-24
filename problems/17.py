from utils.utils import container, random_str
from collections import defaultdict
import random


def func(digits):
    if len(digits) == 0:
        return []
    key = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = ['']
    for item in digits:
        collect = []
        for k in key[item]:
            collect.append([s + k for s in ans])
        ans = []
        for line in collect:
            ans.extend(line)
    return ans


container(func, '23')




