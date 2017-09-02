class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        max_int, target = maxChoosableInteger, desiredTotal
        if max_int < 1 or sum(xrange(1, max_int + 1)) < target:
            return False

        return self.dfs(2 ** max_int - 1, 0, max_int, target)

    def dfs(self, bitmap, total, max_int, target):
        for i in xrange(1, max_int + 1):
            mask = 1 << (i - 1)
            if bitmap & mask & 0xFFFFFFFF != 0:
                if total + i >= target:
                    return True
                other_can_win = self.dfs(bitmap - mask, total, max_int, target)
                if not other_can_win:
                    return True

        return False


solution = Solution()
print solution.canIWin(4, 6)