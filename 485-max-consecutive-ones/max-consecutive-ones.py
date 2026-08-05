class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mx = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                if count > mx:
                    mx = count
                count = 0
        if mx > count:
            return mx
        else:
            return count
