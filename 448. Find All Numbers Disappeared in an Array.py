class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hm = set(nums)
        out = []
        for i in range(len(nums)):
            if i+1 not in hm:
                out.append(i+1)
        return out
