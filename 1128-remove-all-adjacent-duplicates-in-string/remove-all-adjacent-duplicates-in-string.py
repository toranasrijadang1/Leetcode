class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in range(len(s)):
            if not l:
                l.append(s[i])
            else:
                if l[-1] == s[i]:
                    l.pop()
                else:
                    l.append(s[i])
        return ''.join(l)
            