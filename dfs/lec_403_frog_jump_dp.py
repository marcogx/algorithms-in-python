# discrete values of k (last jump), pruning is more natural

# class Solution(object):
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
#         if not stones:
#             return False
#         # the first jump must be unit 1
#         return self.dfs(stones, 0, 0)
#
#
#     def dfs(self, stones, idx, k):
#         sz = len(stones)
#         if idx == sz - 1:
#             return True
#
#         for i in xrange(idx + 1, sz):
#             dis = stones[i] - stones[idx]
#             if dis < k - 1:
#                 continue
#             elif dis > k + 1:
#                 break
#             else:
#                 if self.dfs(stones, i, dis):
#                     return True
#
#         return False

