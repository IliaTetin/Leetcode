class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] =='(':
                l += 1
                cnt += 1
            else:
                if l > 0:
                    cnt -= 1
                    l -= 1
                else:
                    cnt += 1
        return cnt