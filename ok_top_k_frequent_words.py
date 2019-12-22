"""
692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

Naive approach:
    1.  Iterate over words and count them using hash table T~O(N), M~O(M) M<N, M-unique
    2.  Now we have to reverse our hash table in next manner: T~O(N)
        2.1.    key is count, value is list of words with equal count
        2.2.    sort value in alphabetical way T~O(K*log(K)), where K is size of max bucket
    3.  Sort reversed hash table by key T~O(C), C is unique counts
    4.  Iterate over sorted list and print result
"""
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        output = []

        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1

        r_word_counts = defaultdict(list)
        for word, count in word_counts.items():
            r_word_counts[count].append(word)

        for count, words in sorted(r_word_counts.items(), key=lambda x: x[0], reverse=True):
            if k <= 0:
                break

            output.extend(sorted(words)[:k])
            k -= len(words)

        return output


if __name__ == '__main__':
    output = Solution().topKFrequent(
        ["i", "love", "leetcode", "i", "love", "coding"],
        2
    )
    target = ["i", "love"]
    assert output == target
