"""
650. 2 Keys Keyboard
Medium

Initially on a notepad only one character 'A' is present.
You can perform two operations on this notepad for each step:
Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3

Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Note:
The n will be in the range [1, 1000].

Details
Runtime: 24 ms, faster than 93.91% of Python3 online submissions for 2 Keys Keyboard.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 2 Keys Keyboard.
"""
from collections import defaultdict


class Solution:
    def minSteps(self, n: int) -> int:
        """
            Min steps to iterate from 1 to n while have only 2 ops: copy all and paste

            n=2: 'A' -> copy -> paste -> 'AA'
            n=3: 'A' -> copy -> paste -> paste -> 'AAA'
            n=4: 'A' -> copy -> paste -> copy -> paste -> 'AAAA'
            n=5: 'A' -> copy -> paste -> paste -> paste -> paste -> 'AAAAA'
                In that case we can just paste and copy last combination, since. if we paste
                n+1 % 2 == 1 -> 1,3,5,7,.. we can paste only 1,3,5,7,.. els

                So, when we should decide is COPY possible?
            n=6: 'A' -> copy -> paste -> copy -> paste -> paste -> 'AAAAAA' 6=1*2*3
                or   -> copy -> paste -> paste -> copy -> paste -> 'AAAAAA'
            n=7: 'A' -> copy -> paste -> paste -> paste -> paste -> .. ans=7
                Note: prime numbers we can't copy multiple times! Only once when n=1
            n=8: copy->paste->copy->paste->copy->paste 8=2*4
                       'AA'         'AAAA'      'AAAAAAAA'
            n=30: 30=1,2,3,5,10,15,30

                1. build weighted graph, in forward notation: (vertex,weight or N_PASTE to achieve vertex)
                    1: (2,1), (3,2), (5,4), (10,9), (15,14), (30,29)
                    2: (6,2), (10,4), (30,14)
                    3: (15,4), (30,9)
                    5: (10,1), (15,2), (30,5)
                    6: (30,4)
                    10: (30,2)
                    15: (30,1)
                    30: (30,0)
                    Note!  and plus 1 for COPY operation
                2. use dfs to track best path:
                    so: 1->2->10->30 = 1+4+2 + 3 = 10
                            ->30 = 1+4+14 + 2 = 29
                        1->3->15->30 = 2+4+1 + 3 = 10
                            ->30 = 2+9 + 2 = 13
                        and so on

            n=27 (graph): 27=3,9,27
                    1: (3,3), (9,9), (27,27)
                    3: (9,3), (27,9)
                    9: (27,3)
                    27: None
                Q1: How to build the structure above?
                    1. Find all factors
                Q2: How to improve performance?
                    1. Can we remove weight and replace it by value//key? A: Yes => 32ms -> 24ms

        M = log(N)
        T ~ O(N + log(N)*log(N) + log(N)+K) in theory
        """
        graph = defaultdict(list)
        for num in range(2, n + 1):  # T ~ O(N) to find all factors
            if n % num == 0:
                graph[1].append(num)

        for i, vertex in enumerate(graph[1]):  # T ~ O(M*M*1), where M - number of factors; to build graph
            for v in graph[1][i + 1:]:  # O(M*1)
                if v % vertex == 0:
                    graph[vertex].append(v)

                value = v * vertex
                if value in graph[vertex]:  # O(1)
                    graph[vertex].append(value)

        params = {'min_n_steps': n}

        def backtracking(key, n_steps):
            if key == n:
                if params['min_n_steps'] > n_steps:
                    params['min_n_steps'] = n_steps
                return

            for k in graph[key]:
                backtracking(k, n_steps + k // key)

        backtracking(1, 0)  # T ~ O(M+K), where K is number of edges; for dfs
        return params['min_n_steps']


def _main():
    from utils import check_result

    inputs = [27, 30, 2, 3, 4, 5, 6, 7, 8]
    targets = [9, 10, 2, 3, 4, 5, 5, 7, 6]
    check_result(Solution().minSteps)(inputs, targets)


if __name__ == '__main__':
    _main()
