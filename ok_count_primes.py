""" 204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Details
Runtime: 172 ms, faster than 95.79% of Python3 online submissions for Count Primes.
Memory Usage: 36 MB, less than 58.62% of Python3 online submissions for Count Primes.
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
            2 -> 4, 6, 8, 10, ...
            3 -> 6!, 9, 12, ...
            5 -> 10!, 15!, 20!, 25! => starting from 5*5
        """
        if n < 3:
            return 0

        is_prime = [1 for _ in range(n)]

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                is_prime[p * p: n: p] = [0] * len(is_prime[p * p: n: p])

        return sum(is_prime) - 2


def _main():
    from utils import check_result
    
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    targets = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]

    check_result(Solution().countPrimes)(inputs, targets)


if __name__ == '__main__':
    _main()
