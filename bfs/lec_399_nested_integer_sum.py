# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0

        queue = deque()
        for ni in nestedList:
            queue.append(ni)

        res, level = 0, 1

        while queue:
            sz = len(queue)
            level_sum = 0
            for _ in xrange(sz):
                cur = queue.popleft()
                if cur.isInteger():
                    level_sum += cur.getInteger()
                else:
                    for ni in cur.getList():
                        queue.append(ni)
            res += level_sum * level
            level += 1

        return res

