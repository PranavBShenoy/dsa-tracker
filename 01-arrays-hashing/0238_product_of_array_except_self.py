# Problem: 238. Product of Array Except Self (Medium)
# Link: https://neetcode.io/problems/products-of-array-discluding-self/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n) | Space: O(1) auxiliary (O(n) output)
# Key Insight: Multiply left-side product and right-side product for each index without division.


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
