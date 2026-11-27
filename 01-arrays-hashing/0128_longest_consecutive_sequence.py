# Problem: 128. Longest Consecutive Sequence (Medium)
# Link: https://neetcode.io/problems/longest-consecutive-sequence/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n) | Space: O(n)
# Key Insight: Put values in a set and only expand streaks from sequence starts ((num - 1) not in set).


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                current = num
                streak = 1

                while (current + 1) in num_set:
                    current += 1
                    streak += 1

                if streak > longest:
                    longest = streak

        return longest
