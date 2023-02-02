# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums):
        nums = [x ** 2 for x in nums]
        nums.sort()
        return nums

nums = [-4,-1,0,3,10]
sol = Solution()
sol.sortedSquares(nums)
assert(sol.sortedSquares(nums) == [0,1,9,16,100])
nums = [-7,-3,2,3,11]
assert(sol.sortedSquares(nums) == [4,9,9,49,121])