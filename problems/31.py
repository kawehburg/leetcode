from utils.utils import container, random_str
from collections import defaultdict
import random


def func(nums):
    n = len(nums)
    if n < 2:
        return nums
    i = n - 1
    while i > 0 and nums[i - 1] >= nums[i]:  # 要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
        i -= 1
    if i == 0 and nums[i] == max(nums):  # 此数为最大数
        return nums.reverse()
    else:  # 151    i=1
        j = n - 1
        while j > i - 1 and nums[j] <= nums[i - 1]:
            j -= 1
        temp = nums[i - 1]  # i-1为小数  j为大数 交换之
        nums[i - 1] = nums[j]
        nums[j] = temp
        re = nums[i:]
        for h in range(len(re)):
            nums[n - 1 - h] = re[h]
        return nums


container(func, [1, 3, 2])
