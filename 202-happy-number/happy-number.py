def sum_of_squares(n):
    s = 0
    while n > 0:
        d = n % 10
        s += d * d
        n //= 10
    return s

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)
        return n == 1
        