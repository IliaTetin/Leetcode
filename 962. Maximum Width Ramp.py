class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if len(stack) == 0 or nums[stack[-1]] >= nums[i]:
                stack.append(i)
        out = 0
        for i in range(len(nums)-1, -1, -1):
            while len(stack)>0 and nums[stack[-1]] <= nums[i]:
                out = max(out, i-stack[-1])
                stack.pop()
        return out
