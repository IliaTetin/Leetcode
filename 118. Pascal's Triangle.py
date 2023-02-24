# Given an integer numRows, return the first numRows of Pascal's triangle.
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(1, numRows):
            out.append([1] * (i+1))
            for j in range(1, i):
                out[i][j] = out[i-1][j] + out[i-1][j-1]
            
        return out