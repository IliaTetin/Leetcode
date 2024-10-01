class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, val in enumerate(list(s)):
            if val not in d:
                d[s[i]] = [1, i]
            else:
                d[s[i]] = [2, i]
        for key, item in d.items():
            if item[0] == 1:
                return item[1]
        return -1
