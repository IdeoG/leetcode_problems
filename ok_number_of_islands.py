"""
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Runtime: 152 ms, faster than 64.70% of Python3 online submissions for Number of Islands.
Memory Usage: 18.1 MB, less than 5.13% of Python3 online submissions for Number of Islands.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set()

        def dfs_islands(i, j):
            if not (0 <= i < n and 0 <= j < m) or (i, j) in visited or grid[i][j] == '0':
                return

            visited.add((i, j))

            dfs_islands(i - 1, j)
            dfs_islands(i + 1, j)
            dfs_islands(i, j - 1)
            dfs_islands(i, j + 1)

        n_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    n_islands += 1
                    dfs_islands(i, j)

        return n_islands
