class Solution:
    def maxPower(self, s: str) -> int:
        l = list(s)
        count = 1
        mx = 0
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                count += 1
            elif l[i] != l[i+1]:
                if count > mx:
                    mx = count
                count = 1
        return max(mx, count)