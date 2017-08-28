class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, [], 0, 0, word)
        return res

    def dfs(self, res, path, count, idx, word):
        if idx == len(word):
            if count > 0:
                path.append(str(count))
                res.append(''.join(path))
                path.pop()
            else:
                res.append(''.join(path))
            return

        # abbr to digit
        self.dfs(res, path, count + 1, idx + 1, word)
        # keep char
        ch = word[idx]
        if count > 0:
            path.append(str(count) + ch)
        else:
            path.append(ch)
        self.dfs(res, path, 0, idx + 1, word)
        path.pop()