"""
652. Find Duplicate Subtrees
Medium

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees,
you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.


168 / 168 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 20.2 MB
"""

from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        uid_count = defaultdict(int)
        output = []

        def dfs_subtree(node):
            if node:
                triplet = ' '.join((str(node.val), dfs_subtree(node.left), dfs_subtree(node.right)))
                uid_count[triplet] += 1

                if uid_count[triplet] == 2:
                    output.append(node)

                return triplet
            else:
                return ''

        dfs_subtree(root)
        return output
