"""
987. Vertical Order Traversal of a Binary Tree
Medium

Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions
(X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.

Note:
The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.

Details
Runtime: 28 ms, faster than 94.75% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

T ~ O(N + h*log(h) * v*log(v) * k*log(k)), where k is max number of nodes with the same vertical level
"""

from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vl_hl_dict = defaultdict(lambda: defaultdict(list))

        hl = 0
        q, p_item = [(root, 0), None], None
        while True:
            item = q.pop(0)

            if item is None:
                if p_item is None:
                    break
                hl += 1
                q.append(None)
            else:
                node, vl = item
                vl_hl_dict[vl][hl].append(node.val)

                if node.left:
                    q.append((node.left, vl - 1))
                if node.right:
                    q.append((node.right, vl + 1))
            p_item = item

        result = []
        for vl, hl_dict in sorted(vl_hl_dict.items(), key=lambda x: x[0]):
            vl_values = []
            for hl, values in sorted(hl_dict.items(), key=lambda x: x[0]):
                vl_values.extend(sorted(values))
            result.append(vl_values)

        return result
