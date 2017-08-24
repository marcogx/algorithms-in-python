class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        res = []
        self.helper(res, [], 0, 0, 0, num, target)
        return res

    def helper(self, res, path, idx, cur_val, last_val, num, target):
        if idx == len(num) and cur_val == target:
            res.append(''.join(path))
            return
        if idx >= len(num):
            return

        for i in xrange(idx, len(num)):
            number = num[idx:i + 1]
            val = int(number)

            if len(path) == 0:
                path.append(number)
                self.helper(res, path, i + 1, cur_val + val, val, num, target)
                path.pop()
            else:
                path.append('+' + number)
                self.helper(res, path, i + 1, cur_val + val, val, num, target)
                path.pop()
                path.append('-' + number)
                self.helper(res, path, i + 1, cur_val - val, -val, num, target)
                path.pop()
                path.append('*' + number)
                self.helper(res, path, i + 1, cur_val - last_val + last_val * val, last_val * val, num, target)
                path.pop()

            # handle '045', '000' cases
            if val == 0:
                break





