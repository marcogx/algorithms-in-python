from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        queue = deque()
        row, col = len(matrix), len(matrix[0])
        res = [[0 for _ in xrange(col)] for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    queue.append(i * col + j)

        diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = 0

        while queue:
            sz = len(queue)
            for _ in xrange(sz):
                cur = queue.popleft()
                for diff in diffs:
                    r, c = cur / col + diff[0], cur % col + diff[1]
                    if 0 <= r < row and 0 <= c < col and matrix[r][c] == 1 and res[r][c] == 0:
                        res[r][c] = dist + 1
                        queue.append(r * col + c)
            dist += 1

        return res
