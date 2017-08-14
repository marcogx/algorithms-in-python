from collections import deque


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        queue = deque()
        row, col = len(matrix), len(matrix[0])
        can_pac = [[False for _ in xrange(col)] for _ in xrange(row)]
        can_atl = [[False for _ in xrange(col)] for _ in xrange(row)]

        # process Pacific
        # 小心重复添加 bfs 初始元素
        # left
        for i in xrange(row):
            queue.append((i, 0))
            can_pac[i][0] = True
        # top
        for j in xrange(1, col):
            queue.append((0, j))
            can_pac[0][j] = True

        res = []
        self.bfs(res, matrix, queue, can_pac, can_atl)

        # process Atlantic
        # right
        for i in xrange(row):
            queue.append((i, col - 1))
            can_atl[i][col - 1] = True
        # bottom
        for j in xrange(col - 1):
            queue.append((row - 1, j))
            can_atl[row - 1][j] = True

        self.bfs(res, matrix, queue, can_atl, can_pac)

        return res

    def bfs(self, res, matrix, queue, can_this, can_that):
        row, col = len(matrix), len(matrix[0])
        diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            cur = queue.popleft()
            cr, cc = cur[0], cur[1]
            if can_that[cr][cc]:
                res.append([cr, cc])
            for diff in diffs:
                r, c = cr + diff[0], cc + diff[1]
                if (0 <= r < row and 0 <= c < col and
                            matrix[r][c] >= matrix[cr][cc] and
                        not can_this[r][c]):
                    can_this[r][c] = True
                    queue.append((r, c))

