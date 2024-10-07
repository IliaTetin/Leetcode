class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        while nums1 and nums2:
            if nums2[-1] > nums1[-1]:
                nums2.pop()
            elif nums1[-1] > nums2[-1]:
                nums1.pop()
            elif nums2[-1] == nums1[-1]:
                res.add(nums1[-1])
                nums2.pop()
                nums1.pop()
        return list(res)
