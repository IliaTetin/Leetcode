# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021


class Solution:
    def addToArrayForm(self, num, k):
        s = ''
        s = s.join(map(str, num))
        res = list(str(int(s) + k))
        return [int(x) for x in res]
