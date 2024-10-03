class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [[intervals[0][0], intervals[0][1]]]
        for i, val in enumerate(intervals):
            left, right = intervals[i][0], intervals[i][1]
            cur = [left, right]
            if left <= out[-1][1]:
                out[-1][1] = max(right, out[-1][1])
            else:
                out.append(cur)
        return out