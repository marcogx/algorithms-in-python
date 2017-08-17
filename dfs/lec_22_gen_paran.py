class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        res = []
        self.dfs(res, [], 0, 0, n)
        return res

    def dfs(self, res, cur, l, r, n):
        if l == n and l == r:
            res.append(''.join(cur))
            return

        # add left paran
        if l < n:
            cur.append('(')
            self.dfs(res, cur, l + 1, r, n)
            cur.pop()

        # add right paran
        if l > r:
            cur.append(')')
            self.dfs(res, cur, l, r + 1, n)
            cur.pop()