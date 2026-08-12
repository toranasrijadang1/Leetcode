class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1 = 0
        prefix = []
        for i in range(len(nums)):
            sum1 += nums[i]
            prefix.append(sum1)
        return prefix
