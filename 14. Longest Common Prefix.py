# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        max_len = 201
        if len(strs) <= 1:
            return strs[0]
        
        for i in range(len(strs)):
            if len(strs[i]) <= max_len:
                max_len = len(strs[i])
                pref = strs[i]
                if pref == "":
                    return pref

        for j in range(len(pref)):
            for i in range(len(strs)):
                if strs[i][j] != pref[j]:
                        return pref[:j]
        return pref