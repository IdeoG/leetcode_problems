"""
211. Add and Search Word - Data structure design
Medium

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or `.`.
A `.` means it can represent any one letter.

Note:
You may assume that all words are consist of lowercase letters a-z.

Details
Runtime: 276 ms, faster than 82.23% of Python3 online submissions for Add and Search Word - Data structure design.
Memory Usage: 23.2 MB, less than 91.30% of Python3 online submissions for Add and Search Word - Data structure design.
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.trie
        return self.__search_dfs(word, 0, node) is True

    def __search_bfs(self, word: str, trie) -> bool:
        """ 332 - 360 ms """
        q = [(trie, 0)]
        while q:
            node, i = q.pop(0)

            if i == len(word):
                if '#' in node:
                    return True
                else:
                    continue

            if word[i] == '.':
                for k in node.keys():
                    if k != '#':
                        q.append((node[k], i + 1))
            elif word[i] in node:
                q.append((node[word[i]], i + 1))

        return False

    def __search_dfs(self, word, w_idx, trie):
        """ 272 ms """
        if w_idx == len(word):
            return '#' in trie

        if word[w_idx] == '.':
            for k in trie:
                if k != '#' and self.__search_dfs(word, w_idx + 1, trie[k]):
                    return True
        elif word[w_idx] in trie and self.__search_dfs(word, w_idx + 1, trie[word[w_idx]]):
            return True


def _main():
    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')
    assert not wd.search('pad')
    assert wd.search('bad')
    assert wd.search('.ad')
    assert wd.search('b.d')
    assert wd.search('b..')
    assert not wd.search('b...')
    assert wd.search('...')
    assert not wd.search('.at')
    wd.addWord('bat')
    assert wd.search('.at')


if __name__ == '__main__':
    _main()
