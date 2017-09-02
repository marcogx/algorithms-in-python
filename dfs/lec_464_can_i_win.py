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

        return self.dfs([True] * max_int, 0, target)

    def dfs(self, pool, total, target):
        for i in xrange(len(pool)):
            if pool[i]:
                if total + i + 1 >= target:
                    return True
                pool[i] = False
                other_can_win = self.dfs(pool, total + i + 1, target)
                pool[i] = True
                if not other_can_win:
                    return True

        return False