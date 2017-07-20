from collections import deque


def walls_and_gates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    if not rooms or not rooms[0]:
        return

    queue = deque()
    row, col = len(rooms), len(rooms[0])
    for i in xrange(row):
        for j in xrange(col):
            if rooms[i][j] == 0:
                queue.append((i, j))
                # if tuple not supported as Java, using 2To1Dim way.
                # queue.append(i * col + j)
    dist = 0
    diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        sz = len(queue)
        for _ in xrange(sz):
            cur = queue.popleft()
            for diff in diffs:
                r, c = cur[0] + diff[0], cur[1] + diff[1]
                # r, c = cur / col + diff[0], cur % col + diff[1]
                if 0 <= r < row and 0 <= c < col and rooms[r][c] == 2 ** 31 - 1:
                    rooms[r][c] = dist + 1
                    queue.append((r, c))
        dist += 1
