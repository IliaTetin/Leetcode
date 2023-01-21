# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split(' ')
        for i in range(len(splitted)-1, -1, -1):
            out = splitted.pop(i)
            if len(out) >= 1:
                return len(out)