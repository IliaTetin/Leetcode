class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = nums
        for i in range(1, len(nums)):
            self.pref[i] += self.pref[i-1]
        print(self.pref)

    def sumRange(self, left: int, right: int) -> int:
        if left >= 1:
            return self.pref[right] - self.pref[left-1]
        else:
            return self.pref[right]