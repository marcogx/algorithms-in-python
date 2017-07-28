from collections import deque


def shortest_dist_buildings(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid and not grid[0]:
        return -1
    row, col = len(grid), len(grid[0])
    cost = [[0 for _ in xrange(col)] for _ in xrange(row)]

    for i in xrange(row):
        for j in xrange(col):
            if grid[i][j] == 1:
                bfs(grid, cost, i, j)

    res = float('inf')
    for i in xrange(row):
        for j in xrange(col):
            if grid[i][j] == 0 and cost[i][j] > 0:
                res = min(res, cost[i][j])

    return -1 if res == float('inf') else res


def bfs(grid, cost, i, j):
    row, col = len(grid), len(grid[0])
    visited = [[False for _ in xrange(col)] for _ in xrange(row)]
    diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    dist = 0

    while queue:
        sz = len(queue)
        for _ in xrange(sz):
            cur = queue.popleft()
            for diff in diffs:
                r, c = cur[0] + diff[0], cur[1] + diff[1]
                if (0 <= r < row and 0 <= c < col
                        and grid[r][c] == 0 and not visited[r][c]):
                    visited[r][c] = True
                    cost[r][c] += dist + 1
                    queue.append((r, c))
        dist += 1

    for i in xrange(row):
        for j in xrange(col):
            if grid[i][j] == 0 and not visited[i][j]:
                grid[i][j] = 2


