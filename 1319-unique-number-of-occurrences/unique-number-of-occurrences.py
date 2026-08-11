class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        frequencies = list(counts.values())
        return len(frequencies) == len(set(frequencies))