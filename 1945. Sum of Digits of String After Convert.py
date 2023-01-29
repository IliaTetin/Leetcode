# You are given a string s consisting of lowercase English letters, and an integer k.
# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

    # Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
    # Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
    # Transform #2: 17 ➝ 1 + 7 ➝ 8

# Return the resulting integer after performing the operations described above.
# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.



class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for x in s:
            num += str(ord(x) - ord('a') + 1)
        if len(num) <= 1:
            return int(num)

        for i in range(k):
            res = 0
            for i in range(len(num)):
                res += int(num[i])
            num = str(res)
        return int(num)
