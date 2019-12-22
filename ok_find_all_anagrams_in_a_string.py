"""
438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Runtime: 108 ms, faster than 82.22% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Find All Anagrams in a String.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Naive approach:
            1.  Iterate over m - len(p) characters in s and count unique characters
                1.2.    If unique characters == unique characters in p, then save index

            Note: T~O(m*N)
        """
        p_unique_chs_count = defaultdict(int)
        for ch in p:
            p_unique_chs_count[ch] += 1

        m, n = len(p), len(s)
        indexs = []

        subset = s[:m]
        subset_unique_chs_count = defaultdict(int)
        for ch in subset:
            subset_unique_chs_count[ch] += 1

        if subset_unique_chs_count == p_unique_chs_count:
            indexs.append(0)

        for i in range(m, n):
            subset_unique_chs_count[s[i - m]] -= 1
            subset_unique_chs_count[s[i]] += 1

            if subset_unique_chs_count[s[i - m]] == 0:
                del subset_unique_chs_count[s[i - m]]

            if subset_unique_chs_count == p_unique_chs_count:
                indexs.append(i - m + 1)

        return indexs
