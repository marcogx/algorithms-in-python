class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return False

        board, tbl = list(s), {}
        return self.dfs(board, tbl)

    def dfs(self, board, tbl):
        s = ''.join(board)
        res = tbl.get(s)
        if res is not None:
            return res

        for i in xrange(len(board) - 1):
            if board[i] == board[i + 1] == '+':
                board[i] = board[i + 1] = '-'
                other_can_win = self.dfs(board, tbl)
                board[i] = board[i + 1] = '+'
                if not other_can_win:
                    tbl[s] = True
                    return True

        tbl[s] = False
        return False