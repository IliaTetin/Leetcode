# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
# formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        out = 0
        nums.sort(reverse=True)
        
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if (a < b + c):
                return  a+b+c
        return out