class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        res = 0
        for i in xrange(row):
            for j in xrange(col):
                res = max(res, self.dfs(matrix, i, j, float('-inf')))
        return res

    def dfs(self, matrix, i, j, prev):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0

        cur = matrix[i][j]
        ret = max(
            self.dfs(matrix, i - 1, j, cur),
            self.dfs(matrix, i + 1, j, cur),
            self.dfs(matrix, i, j - 1, cur),
            self.dfs(matrix, i, j + 1, cur)
        )

        return ret + 1