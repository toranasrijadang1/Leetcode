class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first = arr[:k]
        currentSum = sum(first)
        count = 0
        if currentSum/k >= threshold:
            count += 1
        for i in range(k,len(arr)):
            currentSum = currentSum + arr[i] - arr[i-k]
            if currentSum/k >= threshold:
                count += 1
        return count