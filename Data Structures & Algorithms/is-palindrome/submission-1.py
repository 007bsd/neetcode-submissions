class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned = cleaned + char.lower()
        output = cleaned == cleaned[::-1]
        return output