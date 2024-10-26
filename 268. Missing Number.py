class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_value = 0
        for i in range(n):
            sum_value += i
            sum_value -= nums[i]
        sum_value += n
        return sum_value
        