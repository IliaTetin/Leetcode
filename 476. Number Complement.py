class Solution:
    def findComplement(self, num: int) -> int:
        binnum = list(format(num ,"b"))
        for i in range(len(binnum)):
            if binnum[i] == '0':
                binnum[i] = '1'
            else:
                binnum[i] = '0'
        return int(''.join(binnum), 2)

