class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if not l:
                l.append(i)
            else:
                if (i == ']' and l[-1] == '['):
                    l.pop()
                elif (i == '}' and l[-1] == '{'):
                    l.pop()
                elif (i == ')' and l[-1] == '('):
                    l.pop()
                elif i in "{([":
                    l.append(i)
                else:
                    return False
        return True if len(l) == 0 else False