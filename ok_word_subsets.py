"""
916. Word Subsets
Medium

We are given two arrays A and B of words.  Each word is a string of lowercase letters.
Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.
For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a.
Return a list of all universal words in A.  You can return the words in any order.


Example 1:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].


Naive approach:
    1. count characters in every b word and then find maxs of each words
    2. iterate over every A word:
        2.1.    count all characters in `a` and check is ch_b in ch_a
"""
from collections import defaultdict


class Solution:
    def wordSubsets(self, A, B):
        output = []
        b_chs_count = defaultdict(lambda: [0 for _ in range(len(B))])
        for i, b in enumerate(B):
            for ch in b:
                b_chs_count[ch][i] += 1

        b_chs_count = {ch: max(counts) for ch, counts in b_chs_count.items()}

        for a in A:
            a_ch_count = defaultdict(int)
            for ch in a:
                a_ch_count[ch] += 1

            is_valid = True
            for ch in b_chs_count.keys():
                if ch not in a_ch_count.keys() or b_chs_count[ch] > a_ch_count[ch]:
                    is_valid = False
                    break
            if is_valid:
                output.append(a)

        return output


if __name__ == '__main__':
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]
    target = ["facebook", 'google', "leetcode"]
    output = Solution().wordSubsets(A, B)
    assert target == output, f'Expected: {target}, but got {output}'

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["l", "e"]
    target = ["apple", "google", "leetcode"]
    output = Solution().wordSubsets(A, B)
    assert target == output, f'Expected: {target}, but got {output}'

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "oo"]
    target = ["facebook", "google"]
    output = Solution().wordSubsets(A, B)
    assert target == output, f'Expected: {target}, but got {output}'

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["ec", "oc", "ceo"]
    target = ["facebook", "leetcode"]
    output = Solution().wordSubsets(A, B)
    assert target == output, f'Expected: {target}, but got {output}'
