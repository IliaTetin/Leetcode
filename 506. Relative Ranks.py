class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        
        for i in range(len(score)):
            heapq.heappush(heap, [-score[i], i])
        
        out = [0] * len(score) 
        cnt = 1
        for i in range(len(heap)):
            ind = heapq.heappop(heap)[1]
            if cnt == 1:
                out[ind] = "Gold Medal"
            elif cnt == 2:
                out[ind] = "Silver Medal"
            elif cnt == 3:
                out[ind] = "Bronze Medal"
            else:
                out[ind] = str(cnt)
            cnt += 1
        return out