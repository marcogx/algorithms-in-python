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
        mem = [[None for _ in xrange(sz_p + 1)] for _ in xrange(sz_s + 1)]
        mem[sz_s][sz_p] = True
        return self.dfs(s, 0, p, 0, mem)

    def dfs(self, s, idx_s, p, idx_p, mem):
        if mem[idx_s][idx_p] is not None:
            return mem[idx_s][idx_p]
        sz_s, sz_p = len(s), len(p)
        if idx_p == sz_p:
            mem[idx_s][idx_p] = idx_s == sz_s
            # return mem[idx_s][idx_p]
        elif idx_p == sz_p - 1 or p[idx_p + 1] != '*':
            if idx_s < sz_s and p[idx_p] in (s[idx_s], '.'):
                mem[idx_s][idx_p] = self.dfs(s, idx_s + 1, p, idx_p + 1, mem)
            else:
                mem[idx_s][idx_p] = False
                # return mem[idx_s][idx_p]
        else:
            i = idx_s - 1
            while i < sz_s and (i == idx_s - 1 or p[idx_p] in (s[i], '.')):
                if self.dfs(s, i + 1, p, idx_p + 2, mem):
                    mem[idx_s][idx_p] = True
                    return mem[idx_s][idx_p]
                i += 1
            mem[idx_s][idx_p] = False
        return mem[idx_s][idx_p]



