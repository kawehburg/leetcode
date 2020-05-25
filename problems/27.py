from utils.utils import container, random_str
from collections import defaultdict
import random


def func(nums, val):
    if len(nums) == 0:
        return 0
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


container(func, [0, 1, 2, 2, 3, 0, 4, 2], 2)
