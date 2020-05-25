from utils.utils import container, random_str
from collections import defaultdict
import random


def func(nums):
    if len(nums) == 0:
        return 0
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[j - 1]:
            nums[j] = nums[i]
            j += 1
    return j


container(func, [0])




