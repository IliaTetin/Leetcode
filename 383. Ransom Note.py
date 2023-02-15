# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1

        for c in ransomNote:
            if (c not in d.keys()) or (d[c] <= 0):
                return False
            d[c] -= 1
            
        return True