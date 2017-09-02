class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        mem = [[0 for _ in xrange(col)] for _ in xrange(row)]
        res = 0
        for i in xrange(row):
            for j in xrange(col):
                res = max(
                    res, self.dfs(matrix, i, j, float('-inf'), mem)
                )
        return res

    def dfs(self, matrix, i, j, prev, mem):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0

        if mem[i][j] > 0:
            return mem[i][j]

        cur = matrix[i][j]
        ret = max(
            self.dfs(matrix, i - 1, j, cur, mem),
            self.dfs(matrix, i + 1, j, cur, mem),
            self.dfs(matrix, i, j - 1, cur, mem),
            self.dfs(matrix, i, j + 1, cur, mem)
        )

        mem[i][j] = ret + 1
        return ret + 1