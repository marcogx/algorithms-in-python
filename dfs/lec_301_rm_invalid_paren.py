class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # if not s:
        #     return [""]
        rm_l, rm_r = self.min_rm_paren(s)
        res = set()
        self.dfs(res, [], 0, s, rm_l, rm_r, 0)
        return list(res)

    # diff: l_paren - r_paren in the curr path
    # rm_l: min of removal of l_paren
    def dfs(self, res, path, idx, s, rm_l, rm_r, diff):
        if idx == len(s) and diff == 0 and rm_l == 0 and rm_r == 0:
            res.add(''.join(path))
            return
        if idx >= len(s) or rm_l < 0 or rm_r < 0 or diff < 0:
            return

        ch = s[idx]
        if ch == '(':
            # remove
            self.dfs(res, path, idx + 1, s, rm_l - 1, rm_r, diff)
            # select
            path.append(ch)
            self.dfs(res, path, idx + 1, s, rm_l, rm_r, diff + 1)
            path.pop()
        elif ch == ')':
            # remove
            self.dfs(res, path, idx + 1, s, rm_l, rm_r - 1, diff)
            # select
            path.append(ch)
            self.dfs(res, path, idx + 1, s, rm_l, rm_r, diff - 1)
            path.pop()
        else:
            # select
            path.append(ch)
            self.dfs(res, path, idx + 1, s, rm_l, rm_r, diff)
            path.pop()

    def min_rm_paren(self, s):
        rm_l, rm_r = 0, 0
        for ch in s:
            if ch == '(':
                rm_l += 1
            elif ch == ')':
                if rm_l > 0:
                    rm_l -= 1
                else:
                    rm_r += 1

        return rm_l, rm_r