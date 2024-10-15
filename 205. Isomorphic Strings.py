class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        set_ = set()
        for i in range(len(s)):
            if s[i] not in hm:
                if t[i] not in set_:
                    hm[s[i]] = t[i]
                    set_.add(t[i])
                else:
                    return False
            elif hm[s[i]] != t[i]:
                return False
        
        return True

sol = Solution()
print(sol.isIsomorphic('badc', 'baba'))
