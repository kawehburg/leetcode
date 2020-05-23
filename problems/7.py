from utils.utils import container, random_str
from collections import defaultdict
import random


def func(x):
    a = ''
    if x < 0:
        a = '-'
        x = -x
    x = str(x)
    x = a + x[::-1]
    x = int(x)
    if x > 2**31 - 1 or x < -2 ** 31:
        return 0
    return x

container(func, -120)




