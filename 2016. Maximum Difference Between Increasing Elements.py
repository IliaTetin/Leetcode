# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        out = -1
        min_el = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= min_el:
                min_el = nums[i]
            cur_dif = nums[i] - min_el
            if cur_dif > 0:
                out = max(out, cur_dif)     
        return out