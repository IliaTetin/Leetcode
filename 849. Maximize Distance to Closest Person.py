class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occ = []
        res = 0
        for i, val in enumerate(seats):
            if val == 1:
                occ.append(i)
                try:
                    if (occ[-1] - occ[-2]) % 2 != 0:
                        res = max(res, (occ[-1] - occ[-2] ) // 2 )
                    else:
                        res = max(res, (occ[-1] + 1  - occ[-2] ) // 2 )
                except:
                    res = max(res, 1)

        if occ[0] == 0 and occ[-1] == i:
            pass
        else:
            res = max(res, (occ[0] - 0))
            res = max(res, (i - occ[-1]))
        return res