class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1

        window_counts = {}
        left = 0

        for right in range(len_s2):
            char_right = s2[right]
            window_counts[char_right] = window_counts.get(char_right, 0) + 1

            if right - left + 1 == len_s1:
                if s1_counts == window_counts:
                    return True

                char_left = s2[left]
                window_counts[char_left] -= 1
                if window_counts[char_left] == 0:
                    del window_counts[char_left]
                left += 1
        return False