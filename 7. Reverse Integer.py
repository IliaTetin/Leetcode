# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Input: x = -123
# Output: -321

# Input: x = 123
# Output: 321

# Input: x = 120
# Output: 21
  
class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        min_range = -2147483648 
        max_range = 2147483647
        if x == 0:
            return 0
        if x < 0:
            minus = True
            x = -1*x
        s = str(x)
        l = [i for i in s]
        while l[-1] == '0':
            l.pop(-1)
        l.reverse()
        if minus:
            out = -1 * int(''.join(l))
            if out < min_range:
                return 0
            return out 
        else:
            out = int(''.join(l))
            if out > max_range:
                return 0
            return out