# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        hs = set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False

#class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        hm = {}
#        for i, val in enumerate(nums):
#            if val not in hm:
#                hm[val] = 1
#            else:
#                return True
#        return False
        