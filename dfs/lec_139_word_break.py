class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        word_dict = set(wordDict)
        max_len = max([len(w) for w in word_dict])
        sz = len(s)
        dp = [False] * (sz + 1)
        dp[sz] = True

        for i in reversed(xrange(sz)):
            for j in xrange(i, min(sz, i + max_len)):
                if s[i:j + 1] in word_dict and dp[j + 1]:
                    dp[i] = True
                    break
        return dp[0]
