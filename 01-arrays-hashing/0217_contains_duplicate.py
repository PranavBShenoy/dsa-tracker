# Problem: 217. Contains Duplicate (Easy)
# Link: https://neetcode.io/problems/duplicate-integer/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n) | Space: O(n)
# Key Insight: Track seen numbers in a set for O(1) lookup; return True on first repeat.


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
