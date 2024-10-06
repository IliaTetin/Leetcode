class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        l = 0
        if s == "":
            return True
        for i, val in enumerate(t):
            if val == s[l]:
                l += 1
                if l == len(list(s)):
                    return True
        return False
