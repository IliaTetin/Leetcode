class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = (n * (n + 1) / 2) ** 0.5
        
        if pivot % 1 == 0:
            return int(pivot)
        else:
            return -1
