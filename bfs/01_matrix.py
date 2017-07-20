from collections import deque


def update_matrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    if not matrix or not matrix[0]:
        return None

    queue = deque()
    row, col = len(matrix), len(matrix[0])
    for i in xrange(row):
        for j in xrange(col):
            if matrix[i][j] == 0:
                # queue.append(i * col + j)
                queue.append((i, j))

    dist = 0
    # res = [[0] * col] * row  # TERRIBLE MISTAKE! IT WILL RETURN THE SAME REFERENCE OF THE NESTED LIST!
    res = [[0 for _ in xrange(col)] for _ in xrange(row)]
    diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        sz = len(queue)
        for _ in xrange(sz):
            cur = queue.popleft()
            for diff in diffs:
                # r, c = cur / col + diff[0], cur % col + diff[1]
                r, c = cur[0] + diff[0], cur[1] + diff[1]
                if (0 <= r < row and 0 <= c < col and matrix[r][c] == 1
                        and res[r][c] == 0):
                    res[r][c] = dist + 1
                    queue.append((r, c))
        dist += 1

    return res


def main():
    test = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    res = update_matrix(test)
    print res


if __name__ == '__main__':
    main()
