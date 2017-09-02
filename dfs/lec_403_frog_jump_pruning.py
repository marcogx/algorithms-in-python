class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:
            return False
        # the first jump must be unit 1
        tbls = [{} for _ in xrange(len(stones))]
        return self.dfs(stones, 0, 0, tbls)


    def dfs(self, stones, idx, k, tbls):
        sz = len(stones)
        if idx == sz - 1:
            return True
        ret = tbls[idx].get(k)
        if ret is not None:
            return ret

        for i in xrange(idx + 1, sz):
            dis = stones[i] - stones[idx]
            if dis < k - 1:
                continue
            elif dis > k + 1:
                break
            else:
                if self.dfs(stones, i, dis, tbls):
                    tbls[idx][k] = True
                    return True

        tbls[idx][k] = False
        return False

