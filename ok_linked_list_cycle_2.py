"""
142. Linked List Cycle II
Medium

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.

Details
Runtime: 44 ms, faster than 96.37% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None
