from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return []

        wordSet = set(wordList)
        queue = deque()
        queue.append(beginWord)
        alphabet = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]
        graph = {}
        found = False
        res = []
        visited = set()

        while queue:
            sz = len(queue)
            for _ in xrange(sz):
                cur = queue.popleft()
                chars = list(cur)
                for i in xrange(len(cur)):
                    tmp = cur[i]
                    for ch in alphabet:
                        if ch == tmp:
                            continue
                        chars[i] = ch
                        word = ''.join(chars)
                        if word in wordSet:
                            if word not in visited:
                                queue.append(word)
                                visited.add(word)
                                graph[word] = [cur]
                            else:
                                graph[word].append(cur)

                            if word == endWord:
                                found = True
                    chars[i] = tmp
            # for word in visited:
            #     wordSet.remove(word)

            if found:
                self.dfs(endWord, beginWord, [endWord], res, graph)
                return res

        return res

    def dfs(self, cur, target, path, res, graph):
        if cur == target:
            res.append(path[::-1])
            return
        for next in graph[cur]:
            path.append(next)
            self.dfs(next, target, path, res, graph)
            path.pop()


s = Solution()
print s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])