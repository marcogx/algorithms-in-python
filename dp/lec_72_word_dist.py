class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if None in (word1, word2):
            return -1

        sz1, sz2 = len(word1), len(word2)
        dp = [[0 for _ in xrange(sz2 + 1)] for _ in xrange(sz1 + 1)]  # eidt dist of w1[:i] and w2[:j]
        for i in xrange(sz1 + 1):
            dp[i][0] = i
        for j in xrange(sz2 + 1):
            dp[0][j] = j

        for i in xrange(1, sz1 + 1):
            for j in xrange(1, sz2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[sz1][sz2]

