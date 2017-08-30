class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        sz_s, sz_p = len(s), len(p)

        # matching s[i:sz_s] with p[j:sz_p]
        dp = [[False for _ in xrange(sz_p + 1)] for _ in xrange(sz_s + 1)]
        dp[sz_s][sz_p] = True

        k = sz_p - 2
        while k >= 0:
            if p[k + 1] == '*':
                dp[sz_s][k] = True
            else:
                break
            k -= 2

        for i in reversed(xrange(sz_s)):
            for j in reversed(xrange(sz_p)):
                if j == sz_p - 1 or p[j + 1] != '*':
                    dp[i][j] = dp[i + 1][j + 1] if p[j] in (s[i], '.') else False
                else:
                    k = i - 1
                    while k < sz_s and (k == i - 1 or p[j] in (s[k], '.')):
                        if dp[k + 1][j + 2]:
                            dp[i][j] = True
                            break
                        k += 1

        return dp[0][0]



