# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        if len_nums == 1:
            return [nums]
        cum_sum = nums.copy()
        for i in range(1, len_nums):
            cum_sum[i] = cum_sum[i-1] + nums[i]
        return cum_sum
