class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        hp = []
        for i in range(len(nums)):
            heapq.heappush(hp, -nums[i])
        
        while k > 0:
            k -= 1
            max_el = -heappop(hp)
            res += max_el
            heapq.heappush(hp, -math.ceil(max_el/3))
        return res
