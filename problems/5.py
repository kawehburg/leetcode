from utils.utils import container, random_str
from collections import defaultdict
import random


def func(s):
    # cache记录每个字符在s中位置，center记录每个中心扩散出的回文串长度
    cache = defaultdict(list)
    center = defaultdict(int)
    for i, item in enumerate(s):
        for last in cache[item]:
            c = (last + i) / 2
            hl = i - last + 1
            if hl - center[c] <= 3:
                center[c] = hl
        cache[item].append(i)
    max_c = 0
    keys = list(center.keys())
    for c in keys:
        if center[c] > center[max_c]:
            max_c = c
    if center[max_c] == 0:
        center[max_c] = 1
    return s[int(max_c - center[max_c] / 2 + 0.5): int(max_c + center[max_c] / 2 + 0.5)]


container(func, 'abc')
