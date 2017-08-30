from collections import deque
from string import lowercase as alphabet


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        begin_word, end_word, word_set = beginWord, endWord, set(wordList)

        if not begin_word or not end_word or not word_set or end_word not in word_set:
            return 0

        queue = deque()
        queue.append(begin_word)
        min_len = 1

        while queue:
            sz = len(queue)
            for _ in xrange(sz):
                cur = queue.popleft()
                chars = list(cur)
                for i, ch in enumerate(chars):
                    # for code in xrange(ord('a'), ord('z') + 1):
                    # if chr(code) != ch:
                    for letter in alphabet:
                        if letter != ch:
                            # chars[i] = chr(code)
                            chars[i] = letter
                            word = ''.join(chars)
                            if word == end_word:
                                return min_len + 1
                            if word in word_set:
                                word_set.remove(word)
                                queue.append(word)
                            if not word_set:
                                return 0
                            chars[i] = ch
            min_len += 1

        return 0
