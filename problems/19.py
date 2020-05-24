from utils.utils import container, random_str
from collections import defaultdict
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_chain(nums):
    if len(nums) == 0:
        return ListNode(None)

    head = ListNode(nums[0])
    ptr = head
    for item in nums[1:]:
        ptr.next = ListNode(item)
        ptr = ptr.next
    return head


def display_chain(head):
    ptr = head
    results = ''
    while ptr:
        results += str(ptr.val) + '->'
        ptr = ptr.next
    results = results[:-2]
    return results


def func(head, n):
    ptr = head
    collect = {}
    i = 0
    while ptr:
        collect[i] = ptr
        ptr = ptr.next
        i += 1
    return head


container(func, build_chain([1, 2, 3, 4, 5]), 2, display=display_chain)
