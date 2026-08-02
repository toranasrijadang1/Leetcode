class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        n = len(s)
        for i in range(n-1):
            d = abs(ord(s[i])-ord(s[i+1]))
            sum += d
        return sum