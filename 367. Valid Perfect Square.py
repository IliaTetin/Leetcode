# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        mid = (left + right) // 2

        while left <= right:
            cur = mid ** 2
            if cur == num:
                return True
            elif cur <= num:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        return False
         