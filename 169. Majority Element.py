# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums) -> int:
        counter = 1
        out = nums[0]
        for i in range(1, len(nums)):
            if counter == 0:
                out = nums[i]
                counter += 1
            elif nums[i] != out:
                counter -= 1
            else:
                counter += 1
        return out

sol = Solution()
sol.majorityElement([6,5,5])