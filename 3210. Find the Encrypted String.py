class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s = list(s)
        s1 = s.copy()
        for i, val in enumerate(s):
            r = (i+k)
            print(r)
            while r >= len(s):
                r = r % len(s)
            s1[i] = s[r]
        return ''.join(s1)
