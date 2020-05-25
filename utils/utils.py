import time
# from memory_profiler import profile
import sys
import random


def container(run, *args, display=None, **kwargs):
    t = time.time()
    results = run(*args, **kwargs)
    print('time cost=', time.time() - t)
    if display:
        results = display(results)
    print('results =', results)


def random_str(slen=10):
    # seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    seed = 'abcdefghijklmnopqrstuvwxyz'
    sa = []
    for i in range(slen):
        sa.append(random.choice(seed))
    return ''.join(sa)


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
