class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                y = y-x
                heapq.heappush(stones, y) 
        return -stones[0] if stones else 0
        