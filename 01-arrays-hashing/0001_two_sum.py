# Problem: 1. Two Sum (Easy)
# Link: https://neetcode.io/problems/two-integer-sum/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n^2) | Space: O(1)
# Key Insight: Check all pairs (i, j) with j > i and return indices when nums[i] + nums[j] == target.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
