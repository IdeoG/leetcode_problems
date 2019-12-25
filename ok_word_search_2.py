"""
212. Word Search II
Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

"""
Naive approach:
1. Build Trie
2. iter over row, col
    2.1.    use dfs to find word
    
Details 
Runtime: 292 ms, faster than 80.15% of Python3 online submissions for Word Search II.
Memory Usage: 27.1 MB, less than 100.00% of Python3 online submissions for Word Search II.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = None

        n, m = len(board), len(board[0])
        result = set()

        def dfs_search(i, j, node, path):
            if not (0 <= i < n and 0 <= j < m) or board[i][j] == '*' or board[i][j] not in node:
                return

            ch = board[i][j]
            board[i][j] = '*'
            path.append(ch)

            if '#' in node[ch]:
                result.add(''.join(path))

            dfs_search(i - 1, j, node[ch], path)
            dfs_search(i + 1, j, node[ch], path)
            dfs_search(i, j - 1, node[ch], path)
            dfs_search(i, j + 1, node[ch], path)

            path.pop()
            board[i][j] = ch

        for i in range(n):
            for j in range(m):
                dfs_search(i, j, trie, [])

        return list(result)


def _main():
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert {"eat", "oath"} == set(Solution().findWords(board, words))

    board = [["a", "a"]]
    words = ["a"]
    assert ['a'] == Solution().findWords(board, words)


if __name__ == '__main__':
    _main()