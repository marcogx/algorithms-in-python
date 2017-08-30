class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if None in (s, p):
            return False
        return self.dfs(s, 0, p, 0)

    def dfs(self, s, idx_s, p, idx_p):
        sz_s, sz_p = len(s), len(p)
        if idx_p == sz_p:
            return idx_s == sz_s
        elif p[idx_p] != '*':
            if idx_s < sz_s and p[idx_p] in (s[idx_s], '?'):
                return self.dfs(s, idx_s + 1, p, idx_p + 1)
            else:
                return False
        else:
            i = idx_s - 1
            while i < sz_s:
                if self.dfs(s, i + 1, p, idx_p + 1):
                    return True
                i += 1
            return False


