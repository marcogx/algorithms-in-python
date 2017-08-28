class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        map = {}
        for c in hand:
            map[c] = map.get(c, 0) + 1
        res = [len(hand) + 1]
        self.dfs(board, map, 0, res)
        return -1 if res[0] == len(hand) + 1 else res[0]

    def dfs(self, board, map, step, res):
        sz = len(board)
        if sz == 0:
            res[0] = min(res[0], step)
            return

        if step > res[0] or all([d == 0 for d in map.values()]):
            return

        for i, color in enumerate(board):
            # insert 1 ball when 2 same color
            count = map.get(color, 0)
            if i + 1 < sz and board[i + 1] == color and count > 0:
                map[color] = count - 1
                new_board = self.refine_board(board, i - 1, i + 2)
                self.dfs(new_board, map, step + 1, res)
                map[color] = count
            # insert 2 balls when we have enough color
            elif count >= 2:
                map[color] = count - 2
                new_board = self.refine_board(board, i - 1, i + 1)
                self.dfs(new_board, map, step + 2, res)
                map[color] = count

    def refine_board(self, board, left, right):
        sz = len(board)
        while left >= 0 and right < sz:
            color, count = board[left], 0

            l = left
            while l >= 0 and board[l] == color:
                count += 1
                l -= 1

            r = right
            while r < sz and board[r] == color:
                count += 1
                r += 1

            if count >= 3:
                left, right = l, r
            else:
                break
        return board[:left + 1] + board[right:]








