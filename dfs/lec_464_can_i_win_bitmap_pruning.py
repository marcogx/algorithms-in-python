class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        max_int, target = maxChoosableInteger, desiredTotal
        if (1 + max_int) * max_int / 2 < target:
            return False
        # if max_int < 1 or sum(xrange(1, max_int + 1)) < target:
        #     return False
        bitmap = (1 << max_int) - 1
        mem = [None] * (bitmap + 1)
        # mem = {}
        return self.dfs(bitmap, 0, max_int, target, mem)

    def dfs(self, bitmap, total, max_int, target, mem):
        # ret = mem.get(bitmap)
        ret = mem[bitmap]
        if ret is not None:
            return ret

        for i in xrange(1, max_int + 1):
            mask = 1 << (i - 1)
            if bitmap & mask != 0:
                new_bitmap = bitmap - mask
                if total + i >= target:
                    mem[new_bitmap] = True
                    return True

                other_can_win = self.dfs(new_bitmap, total + i, max_int, target, mem)
                if not other_can_win:
                    mem[bitmap] = True
                    return True

        mem[bitmap] = False
        return False

solution = Solution()
print solution.canIWin(20, 54)