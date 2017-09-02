class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return False

        s = list(s)
        return self.dfs(s)

    def dfs(self, s):
        for i in xrange(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                s[i] = s[i + 1] = '-'
                other_can_win = self.dfs(s)
                s[i] = s[i + 1] = '+'

                if not other_can_win:
                    return True
        return False
