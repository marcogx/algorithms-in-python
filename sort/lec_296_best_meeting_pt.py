class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid and not grid[0]:
            return float('inf')

        row, col = len(grid), len(grid[0])
        homes = [(i, j) for i in xrange(row) for j in xrange(col) if grid[i][j] == 1]
        xs = [pt[0] for pt in homes]
        ys = [pt[1] for pt in homes]
        xs.sort()
        ys.sort()
        meet_pt = (xs[(len(xs) - 1) // 2], ys[(len(ys) - 1) // 2])

        res = 0
        for pt in homes:
            res += abs(meet_pt[0] - pt[0]) + abs(meet_pt[1] - pt[1])
        return res
