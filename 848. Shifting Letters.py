class Solution:
    def fix(self, letter, t):
        res = ord(letter) +  t % 26 
        if res > 122:
            res = 96 + res - 122
        return chr(res)

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        for i in range(len(shifts)-2,-1, -1):
            shifts[i] += shifts[i+1]
            s[i] = self.fix(s[i], shifts[i])
        
        s[-1] = self.fix(s[-1], shifts[-1])
        return ''.join(s)
        