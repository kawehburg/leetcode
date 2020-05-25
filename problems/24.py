from utils.utils import container, random_str, ListNode, build_chain, display_chain
from collections import defaultdict
import random


def func(head):
    if head is None:
        return head
    root = ListNode(0)
    root.next = head
    last = root
    next_node = head.next
    while next_node:
        ptr = last.next
        if ptr is None:
            break
        next_node = ptr.next
        if next_node is not None:
            block = next_node.next
            last.next = next_node
            next_node.next = ptr
            ptr.next = block
            last = ptr

    return root.next


def ref(head):
    # 使用递归，优雅很多
    if not head or not head.next:
        return head
    res = head.next
    head.next = ref(res.next)
    res.next = head
    return res


container(ref, build_chain([1, 2, 3, 4]), display=display_chain)
