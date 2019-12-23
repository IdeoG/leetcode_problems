"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

Details
Runtime: 24 ms, faster than 98.09% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root, None]
        paths, path = [], []
        is_left_to_right_order = True
        p_node = None

        while True:
            node = q.pop(0)

            if node is None:
                if p_node is None:
                    break

                if is_left_to_right_order:
                    paths.append(path)
                else:
                    paths.append(path[::-1])

                path = []
                is_left_to_right_order = not is_left_to_right_order
                q.append(None)
            else:
                path.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            p_node = node
        return paths
