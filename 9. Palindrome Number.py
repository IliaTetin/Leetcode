# Given an integer x, return true if x is a palindrome, and false otherwise.

# Input: x = 121
# Output: true

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        back = ''
        for i in range(len(s)):
            back += s[-1 - i]
        if back == s:
            return True
        return False