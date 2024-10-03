class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = min(height[0], height[1])
        left = 0
        right = len(height) - 1
        while left < right:
            cur_vol = (right - left) * min(height[right],height[left])
            if cur_vol > vol:
                vol = cur_vol
            else:
                if height[left] <= height[right]:
                    left += 1
                else:
                    right -= 1
        return vol