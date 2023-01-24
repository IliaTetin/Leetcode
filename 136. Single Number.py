# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [4,1,2,1,2]
# Output: 4


class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[-1]
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[-1]
        