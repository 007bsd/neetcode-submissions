class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        best_length = 0

        for right in range(len(s)):
            current_char = s[right]
            
            while current_char in char_set:
                char_set.remove(s[left])
                
                left = left + 1

            char_set.add(current_char)

            window_size = right - left + 1

            best_length = max(best_length, window_size)
        return best_length

        