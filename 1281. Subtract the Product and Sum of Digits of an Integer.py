# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = [int(i) for i in str(n)]
        prod_ = 1
        sum_ = 0
        for i, v in enumerate(s):
            prod_ *= v
            sum_ += v
        return prod_ - sum_
