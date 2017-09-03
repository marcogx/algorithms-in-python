class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        sz = len(s)
        # dp[i][j] min cut for s[i...j] i, j included
        dp = [[0 for _ in xrange(sz)] for _ in xrange(sz)]

        for i in reversed(xrange(sz)):
            for j in xrange(i, sz):
                if self.is_palin(s[i: j + 1]):
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        [dp[k + 1][j] + 1 for k in xrange(i, j) if self.is_palin(s[i: k + 1])]
                    )

        return dp[0][sz - 1]

    def is_palin(self, s):
        sz = len(s)
        start, end = 0, sz - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
