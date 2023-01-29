# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Input: num = 38
# Output: 2
# xplanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.


class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        if len(s) <= 1:
            return num
        while len(s) > 1:
            res = 0
            for i in range(len(s)):
                res += int(s[i])
            s = str(res)
        
        return res
                