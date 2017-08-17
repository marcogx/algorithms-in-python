class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        row, col = len(board), len(board[0])
        visited = [[False for _ in xrange(col)] for _ in xrange(row)]

        for i in xrange(row):
            for j in xrange(col):
                if self.dfs(board, i, j, word, 0, visited):
                    return True

        return False

    def dfs(self, board, i, j, word, idx, visited):
        if idx == len(word):
            return True
        row, col = len(board), len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[idx] or visited[i][j]:
            return False
        visited[i][j] = True
        ret = (
            self.dfs(board, i, j + 1, word, idx + 1, visited) or
            self.dfs(board, i, j - 1, word, idx + 1, visited) or
            self.dfs(board, i + 1, j, word, idx + 1, visited) or
            self.dfs(board, i - 1, j, word, idx + 1, visited)
        )
        visited[i][j] = False
        return ret

