"""
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) < 3 or not grid[0] or len(grid[0]) < 3:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set()

        def is_closed_island_dfs(i, j):
            if not (0 < i < n - 1 and 0 < j < m - 1):
                return grid[i][j] == 1

            if (i, j) in visited or grid[i][j] == 1:
                return True

            visited.add((i, j))

            return (is_closed_island_dfs(i - 1, j) and is_closed_island_dfs(i + 1, j) and
                    is_closed_island_dfs(i, j - 1) and is_closed_island_dfs(i, j + 1))

        n_islands = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if is_closed_island_dfs(i, j):
                        n_islands += 1
        return n_islands


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    target = 2
    output = Solution().closedIsland(grid)
    assert target == output, f'Expected = {target}; Got = {output}'

    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    target = 5
    output = Solution().closedIsland(grid)
    assert target == output, f'Expected = {target}; Got = {output}'
