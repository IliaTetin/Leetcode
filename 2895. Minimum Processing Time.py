class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=False)
        processorTime.sort(reverse=True)
        out = 0
        while len(tasks) > 0:
            cur =  processorTime.pop() + tasks.pop()
            for i in range(3):
                tasks.pop()
            out = max(out, cur)
        return out
                