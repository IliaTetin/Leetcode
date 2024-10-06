class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] inQ v:
                while s[r] not in v:
                    r -= 1
                s[r], s[l] = s[l], s[r]
                l += 1
                r -= 1
            else:
                l += 1
        return("".join(s))
        