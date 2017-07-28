def best_meeting_pt(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid and not grid[0]:
        return 0

    row, col = len(grid), len(grid[0])
    ones = []
    for i in xrange(row):
        for j in xrange(col):
            if grid[i][j] == 1:
                ones.append((i, j))

    xs = [item[0] for item in ones]
    ys = [item[1] for item in ones]
    xs.sort()
    ys.sort()
    count = len(ones)
    meet_p = (xs[(count - 1) / 2], ys[(count - 1) / 2])

    return sum([abs(p[0] - meet_p[0]) + abs(p[1] - meet_p[1]) for p in ones])
