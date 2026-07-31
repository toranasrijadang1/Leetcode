class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                res = [nums[i], nums[left], nums[right]]
                if nums[i] + nums[left] + nums[right] == 0:
                    res.sort()
                    ans.add(tuple(res))
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return list(ans)

