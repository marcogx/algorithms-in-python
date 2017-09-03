class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        sz = len(s)
        dp = [0 for _ in xrange(sz + 1)]  # min num of partition of substring [i...sz-1] == cut + 1
        palins = [[False for _ in xrange(sz)] for _ in xrange(sz)]

        for i in reversed(xrange(sz)):
            dp[i] = sz - i
            for j in xrange(i, sz):
                if i == j or (s[i] == s[j] and (j == i + 1 or palins[i + 1][j - 1])):
                    dp[i] = min(dp[i], dp[j + 1] + 1)
                    palins[i][j] = True

        return dp[0] - 1

solution = Solution()
print solution.minCut('aab')