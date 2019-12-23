"""
92. Reverse Linked List II
Medium

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Runtime: 24 ms, faster than 96.70% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        def reverse(head: ListNode, k: int) -> ListNode:
            p_node = None
            t_node = head

            while k >= 0 and t_node:
                f_node = t_node.next
                t_node.next = p_node
                p_node = t_node
                t_node = f_node

                k -= 1

            head.next = t_node
            return p_node

        k = n - m
        if k == 0:
            return head

        node = head

        if m == 1:
            return reverse(node, k)

        while m > 2:  # since arr starts from 1
            node = node.next
            m -= 1

        node.next = reverse(node.next, k)
        return head


if __name__ == '__main__':
    def get_list_repr(node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return '->'.join(map(str, values))

    head = ListNode(1)
    node = head
    for x in range(2, 3):
        node.next = ListNode(x)
        node = node.next

    print('Before:', get_list_repr(head))
    head = Solution().reverseBetween(head, 1, 2)
    print('After: ', get_list_repr(head))


