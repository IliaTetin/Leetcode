# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Input: digits = ""
# Output: []

# Input: digits = "2"
# Output: ["a","b","c"]

#Constraints:

#    0 <= digits.length <= 4
#    digits[i] is a digit in the range ['2', '9'].


class Solution:
    def letterCombinations(self, digits):
        out = []
        d = {}
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        if digits == '':
            return out

        if len(digits) == 1:
            return d[digits]
        
        elif len(digits) == 2:
            for i in range(len(d[digits[0]])):
                for j in range(len(d[digits[1]])):
                    out.append(d[digits[0]][i] + d[digits[1]][j])
                    
        elif len(digits) == 3:
            for i in range(len(d[digits[0]])):
                for j in range(len(d[digits[1]])):
                    for k in range(len(d[digits[2]])):
                        out.append(d[digits[0]][i] + d[digits[1]][j] + d[digits[2]][k])
        
        elif len(digits) == 4:
            for i in range(len(d[digits[0]])):
                for j in range(len(d[digits[1]])):
                    for k in range(len(d[digits[2]])):
                        for n in range(len(d[digits[3]])):
                            out.append(d[digits[0]][i] + d[digits[1]][j] + d[digits[2]][k] + d[digits[3]][n])
                     
        return out 


sol = Solution()
print(sol.letterCombinations('2334'))