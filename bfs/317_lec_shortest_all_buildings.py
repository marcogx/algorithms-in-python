from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        row, col = len(grid), len(grid[0])
        dists = [[0 for _ in xrange(col)] for _ in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    self.bfs(grid, dists, i, j)

        res = float('inf')
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 0 and dists[i][j] < res:
                    res = dists[i][j]

        return -1 if res == float('inf') else res

    def bfs(self, grid, dists, i, j):
        queue = deque()
        row, col = len(grid), len(grid[0])
        queue.append(i * col + j)
        diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for _ in xrange(col)] for _ in xrange(row)]
        dist = 0

        while queue:
            sz = len(queue)
            for _ in xrange(sz):
                cur = queue.popleft()
                for diff in diffs:
                    r, c = cur / col + diff[0], cur % col + diff[1]
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 0 and not visited[r][c]:
                        dists[r][c] += dist + 1
                        visited[r][c] = True
                        queue.append(r * col + c)
            dist += 1

        # It is a must, to identify the reachable empty space.
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 0 and not visited[i][j]:
                    grid[i][j] = 2


