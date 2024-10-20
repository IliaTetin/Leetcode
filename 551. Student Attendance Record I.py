class Solution:
    def checkRecord(self, s: str) -> bool:
        s = list(s)
        max_A = 0
        long_L = 0

        for i, val in enumerate(s):
            if val == 'A':
                max_A += 1
                if max_A > 1:
                    return False
            if val == 'L':
                long_L += 1
                if long_L == 3:
                    return False
            else:
                long_L = 0
        
        return True