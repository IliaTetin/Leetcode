# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#    I can be placed before V (5) and X (10) to make 4 and 9. 
#    X can be placed before L (50) and C (100) to make 40 and 90. 
#    C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        df = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(s) == 1:
            return df[s[-1]]
        res = df[s[0]]
        last = s[0]

        for i in range(1, len(s)):
            if s[i] == 'V' and last == 'I':
                res += 3
                last = 'V'
                i -= 1 
            elif s[i] == 'X' and last == 'I':
                res += 8
                last = 'X'
                i -= 1 
            elif s[i] == 'L' and last == 'X':
                res += 30
                last = 'X'
                i -= 1 
            elif s[i] == 'C' and last == 'X':
                res += 80
                last = 'X'
                i -= 1 
            elif s[i] == 'D' and last == 'C':
                res += 300
                last = 'C'
                i -= 1 
            elif s[i] == 'M' and last == 'C':
                res += 800
                last = 'C'
                i -= 1 
            else:
                res += df[s[i]]
                last = s[i]
        return res
        