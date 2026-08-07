class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # DYNAMIC SLIDING WINDOW
        zerocount = 0
        mxlength = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerocount += 1
            # while loop makes window valid
            while zerocount > k:
                if nums[left] == 0:
                    zerocount -= 1
                left += 1
            #update mxlength only for valid window
            mxlength = max(mxlength, right-left+1)
        return mxlength