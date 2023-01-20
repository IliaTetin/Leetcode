# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [9]
# Output: [1,0]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in range(len(digits)):
            s += str(digits[i])
        s = int(s) + 1
        s = str(s)
        digits = []
        for i in range(len(s)):
            digits.append(int(s[i]))
        return digits