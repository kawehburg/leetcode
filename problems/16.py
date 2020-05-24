from utils.utils import container, random_str
from collections import defaultdict
import random


def func(nums, target):
    if len(nums) < 3:
        return []
    collect = defaultdict(int)
    for item in nums:
        collect[item] += 1
    nums = sorted(list(set(nums)))

    def epoch(tar):
        for i in range(len(nums)):
            if collect[nums[i]] > 1:
                start = i
            else:
                start = i + 1
            for j in range(start, len(nums)):
                f = tar - nums[i] - nums[j]
                if nums[j] > f:
                    break
                if f in collect:
                    if f == nums[j] and collect[f] < 2:
                        pass
                    elif f == nums[j] == nums[i] and collect[f] < 3:
                        pass
                    else:
                        return True
        return False
    if epoch(target):
        return target
    m = 0
    while True:
        if epoch(target + m):
            return target + m
        if epoch(target - m):
            return target - m
        m += 1


container(func, [-1, 2, 1, -4], 1)
