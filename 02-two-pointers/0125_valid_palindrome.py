# Problem: 125. Valid Palindrome (Easy)
# Link: https://neetcode.io/problems/is-palindrome/question\?list\=neetcode150
# Status: Green | Pattern: Two Pointers
# Time: O(n) | Space: O(n)
# Key Insight: Filter alphanumeric lowercase chars and move left/right pointers inward.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
