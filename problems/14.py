from utils.utils import container, random_str
from collections import defaultdict
import random


def func(strs):
    if len(strs) == 0:
        return ''
    ans = strs[0]
    for s in strs:
        if len(s) == 0:
            return ''
        i = 0
        for i in range(min(len(ans), len(s))):
            if ans[i] != s[i]:
                break
        else:
            i += 1
        ans = ans[:i]
        if len(ans) == 0:
            return ''
    return ans


container(func, [["abab","aba",""]])




