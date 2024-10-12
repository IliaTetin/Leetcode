class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        cnt = 0
        while cnt != k:
            cnt += 1
            out = heapq.heappop(nums)
            if cnt == k:
                return -out
