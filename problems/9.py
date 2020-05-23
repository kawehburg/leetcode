from utils.utils import container, random_str
from collections import defaultdict
import random


def func(x):
    x = str(x)
    reverse_x = x[::-1]
    return x == reverse_x


container(func, -121)
