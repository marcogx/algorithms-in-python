class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if None in (s, p):
            return False

        sz_s, sz_p = len(s), len(p)
        dp = [[False for _ in xrange(sz_p + 1)] for _ in xrange(sz_s + 1)]

        dp[sz_s][sz_p] = True
        j = sz_p - 1
        while j >= 0 and p[j] == '*':
            for i in xrange(sz_s + 1):
                dp[i][j] = True
            j -= 1

        for i in reversed(xrange(sz_s)):
            for j in reversed(xrange(sz_p)):
                if p[j] != '*':
                    dp[i][j] = dp[i + 1][j + 1] if p[j] in (s[i], '?') else False
                else:
                    k = i - 1
                    while k < sz_s:
                        if dp[k + 1][j + 1]:
                            dp[i][j] = True
                            break
                        k += 1

        return dp[0][0]


solution = Solution()
s= "aabbbbaaaaaaaabbbabbaabbbbbbaabaaabbbabbaabaaabababbaabababbaaaaababbbbbbababaaabbbbbabbbaabaaaaaaabbbbbbababbaaaabbababbbbabbabbabababbaabbbabbabbaabababbaaabbaabaabbbbaabaaaabbbbbbabaabaabbabaaabbbbab"
p = "a**abaaa******a*b*ba**aba***b*bbbab*bb*aab**a*bba*b*abab**aabbb***a*a**b**a*abab*ba**aa**b***aba*b****a*"

print solution.isMatch(s, p)
