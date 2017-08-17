from collections import deque
from string import lowercase as alphabet


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        begin_word, end_word, word_set = beginWord, endWord, set(wordList)

        if not begin_word or not end_word or not word_set or end_word not in word_set:
            return []

        queue = deque()
        queue.append(begin_word)
        word_graph = {}
        found = False

        while not found and queue:
            sz = len(queue)
            visited = set()
            for _ in xrange(sz):
                cur = queue.popleft()
                chars = list(cur)
                for i, ch in enumerate(cur):
                    for letter in alphabet:
                        if letter != ch:
                            chars[i] = letter
                            word = ''.join(chars)
                            if word == end_word:
                                found = True
                            if word in word_set:
                                if word not in word_graph:
                                    word_graph[word] = [cur]
                                else:
                                    word_graph[word].append(cur)

                                if word not in visited:
                                    visited.add(word)
                                    queue.append(word)
                            chars[i] = ch

            for w in visited:
                word_set.remove(w)

        res = []
        if found:
            self.dfs(word_graph, res, cur=[end_word], target=begin_word)
        return res

    def dfs(self, word_graph, res, cur, target):
        cur_word = cur[-1]
        if cur_word == target:
            res.append(cur[::-1])
            return

        for word in word_graph.get(cur_word, []):
            cur.append(word)
            self.dfs(word_graph, res, cur, target)
            cur.pop()

