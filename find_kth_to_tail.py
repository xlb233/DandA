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
    for _ in range(k - 1):
        if fast.next:
            fast = fast.next
        else:
            return None
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow
