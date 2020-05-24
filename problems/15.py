from utils.utils import container, random_str
from collections import defaultdict
import random


def func(nums):
    if len(nums) < 3:
        return []
    collect = defaultdict(int)
    for item in nums:
        collect[item] += 1
    nums = sorted(list(set(nums)))
    ans = []
    for i in range(len(nums)):
        if collect[nums[i]] > 1:
            start = i
        else:
            start = i + 1
        for j in range(start, len(nums)):
            f = -nums[i] - nums[j]
            if nums[j] > f:
                break
            if f in collect:
                if f == nums[j] and collect[f] < 2:
                    pass
                elif f == nums[j] == nums[i] and collect[f] < 3:
                    pass
                else:
                    ans.append([nums[i], nums[j], f])

    return ans


container(func, [-1, 0, 1, 0])
