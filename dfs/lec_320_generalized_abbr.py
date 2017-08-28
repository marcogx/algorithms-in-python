class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, [], 0, word)
        return res

    def dfs(self, res, path, idx, word):
        if idx == len(word):
            res.append(self.refine(path))
            return
        for ch in ['1', word[idx]]:
            path.append(ch)
            self.dfs(res, path, idx + 1, word)
            path.pop()

    def refine(self, path):
        res = []
        count = 0
        for ch in path:
            if ch == '1':
                count += 1
            else:
                if count > 0:
                    res.append(str(count) + ch)
                    count = 0
                else:
                    res.append(ch)
        if count > 0:
            res.append(str(count))
        return ''.join(res)