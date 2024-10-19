class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            nums = []
            l1 = len(nums1)
            l2 = len(nums2)
            while nums1 and nums2:
                if nums1[-1] > nums2[-1]:
                    nums.append(nums1.pop())
                elif nums1[-1] < nums2[-1]:
                    nums.append(nums2.pop())
                else:
                    if nums1:
                        nums.append(nums1.pop())
                    if nums2:
                        nums.append(nums2.pop())
            if nums1:
                while nums1:
                    nums.append(nums1.pop())
            if nums2:
                while nums2:
                    nums.append(nums2.pop())
            if (l1 + l2) % 2 == 0:
                i = len(nums) // 2 - 1
                j = len(nums) // 2
                out = (nums[i] + nums[j]) / 2
            else:
                out = nums[len(nums) // 2]
            return out/1
            