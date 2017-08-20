class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 4 or len(s) > 12:
            return []

        res = []
        self.dfs(res, [], s, 0, 0)
        return res

    def dfs(self, res, cur, s, idx, count):
        if idx == len(s) and count == 4:
            res.append(''.join(cur))
            return

        if idx == len(s) or count > 4:
            return

        for l in xrange(1, 4):
            if idx + l > len(s):
                break
            digits = s[idx:idx + l]
            val = int(digits)
            if 0 <= val <= 255:
                if len(cur) == 0:
                    cur.append(digits)
                else:
                    cur.append('.' + digits)
                self.dfs(res, cur, s, idx + l, count + 1)
                cur.pop()
                if val == 0:
                    break

def main():
    s = Solution()
    print s.restoreIpAddresses("25525511135")


if __name__ == '__main__':
    main()