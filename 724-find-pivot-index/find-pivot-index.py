class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = list(itertools.accumulate(nums,initial = 0))
        for i in range(len(nums)):
            left_sum = prefix[i]
            right_sum = prefix[len(nums)]-prefix[i+1]
            if left_sum == right_sum:
                return i
        return -1

        