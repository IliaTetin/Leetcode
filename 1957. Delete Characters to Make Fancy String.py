class Solution:
    def makeFancyString(self, s: str) -> str:
        s = list(s)
        i = 0
        out = []
        while i < len(s):
            out.append(s[i])
            if len(out) > 2:
                if out[-1] == out[-2] == out[-3]:
                    out.pop()
            i += 1
        return ''.join(out)
