class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        p, k = 0, 0
        if m*n == len(original):
            while k != m:
                out.append([])
                for i in range(p, p+n):
                    out[k].append(original[i])
                p = p + n
                k += 1
        return out
            