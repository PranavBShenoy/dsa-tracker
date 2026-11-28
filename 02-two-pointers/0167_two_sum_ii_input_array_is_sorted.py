# Problem: 167. Two Sum II - Input Array Is Sorted (Medium)
# Link: https://neetcode.io/problems/two-integer-sum-ii/question\?list\=neetcode150
# Status: Green | Pattern: Two Pointers
# Time: O(n) | Space: O(1)
# Key Insight: Use left/right pointers on a sorted array and return 1-based indices.


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1

        return []
