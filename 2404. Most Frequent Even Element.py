# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        out = -1
        cur_max = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] not in d:
                    d[nums[i]] = 1
                    if cur_max <= 1:
                        if out % 2 == 0:
                            out = min(out, nums[i])
                        else:    
                            out = nums[i]
                            cur_max = 1
                else:
                    d[nums[i]] += 1
                    if d[nums[i]] > cur_max:
                        out = nums[i]
                        cur_max = d[nums[i]]
                    elif d[nums[i]] == cur_max:
                        out = min(out, nums[i])
        return out