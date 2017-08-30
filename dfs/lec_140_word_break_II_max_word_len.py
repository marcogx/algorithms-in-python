class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []
        word_dict = set(wordDict)
        res = []
        mem = [True] * (len(s) + 1)
        max_len = max([len(w) for w in word_dict])
        self.dfs(res, [], 0, s, word_dict, mem, max_len)
        return res

    def dfs(self, res, path, idx, s, word_dict, mem, max_len):
        if idx == len(s):
            res.append(' '.join(path))
            return

        sz = len(res)
        # idx that all chars between which will be included
        for i in xrange(idx, min(len(s), idx + max_len)):
            word = s[idx:i + 1]
            if word in word_dict and mem[i + 1]:
                path.append(word)
                self.dfs(res, path, i + 1, s, word_dict, mem, max_len)
                path.pop()
        if len(res) == sz:
            mem[idx] = False


