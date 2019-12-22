from collections import defaultdict


class Solution(object):
    def __find_generic_states(self, wordList):
        generic_states = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                generic_states[key].append(word)

        return generic_states

    def __bfs_words(self, start, target, graph):
        q, visited = [(start, 1)], set()

        while q:
            word, level = q.pop(0)

            if word not in visited:
                visited.add(word)

                for i in range(len(word)):
                    node = word[:i] + "*" + word[i + 1:]

                    for con_node in graph[node]:
                        if con_node == target:
                            return level + 1
                        elif con_node not in visited:
                            q.append((con_node, level + 1))
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        generic_states = self.__find_generic_states(set(wordList))
        return self.__bfs_words(beginWord, endWord, generic_states)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = Solution().ladderLength(beginWord, endWord, wordList)
    assert result == 5, f'Expected 5, but got {result}'

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "dot"]
    result = Solution().ladderLength(beginWord, endWord, wordList)
    assert result == 3, f'Expected 3, but got {result}'
