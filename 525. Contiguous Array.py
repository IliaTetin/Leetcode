class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        res = 0
        cur = 0
        for i,val in enumerate(nums):
            if val == 0:
                cur -= 1
            else:
                cur += 1

            if cur in d:
                res = max(res, i - d[cur])
            else:
                d[cur] = i
        return res
