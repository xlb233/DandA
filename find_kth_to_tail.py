# 《剑指offer》寻找链表的倒数第K个节点
import random


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


def find_kth_to_tail(head, k):
    fast = head
    slow = head
    if type(head) is not Node or k <= 0:
        return None
    # 这里为何快指针先走k-1呢
    # 假设链表长度为n，则倒数第k个元素即为正数的第n-k+1个元素
    # 如果需要慢指针移到最后时快指针正好到达要找的元素
    # 也就是需要相距n-（n-k+1）= k-1
    for _ in range(k - 1):
        if fast.next:
            fast = fast.next
        else:
            return None
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow
