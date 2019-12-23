"""
771. Jewels and Stones
Easy

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

Details
Runtime: 20 ms, faster than 99.02% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""

from collections import defaultdict


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        unique_jewels = set(J)
        unique_stone_counts = defaultdict(int)

        for stone in S:
            unique_stone_counts[stone] += 1

        return sum([unique_stone_counts[key] for key in unique_stone_counts.keys()
                    if key in unique_jewels])
