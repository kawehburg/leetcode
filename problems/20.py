from utils.utils import container, random_str
from collections import defaultdict
import random


def func(s):
    t = ['']
    close = {')': '(', '}': '{', ']': '['}
    for item in s:
        if item in close and t[-1] == close[item]:
            t.pop()
        elif item in close:
            return False
        else:
            t.append(item)
    if len(t) == 1:
        return True
    return False


def ref(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''


container(func, '{[]}')
