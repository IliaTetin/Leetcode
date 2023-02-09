
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].


class Solution:
    def vowelStrings(self, words, queries):
        vowels = 'aeiou'
        prefix = [0]
        cnt = 0
        for word in range(len(words)):
            if words[word][0] in vowels and words[word][-1] in vowels:
                cnt += 1
            prefix.append(cnt)
        
        out = []
        for i in queries:
            out.append(prefix[i[1]+1] - prefix[i[0]])
        return out
        