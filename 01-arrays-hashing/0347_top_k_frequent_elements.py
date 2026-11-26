# Problem: 347. Top K Frequent Elements (Medium)
# Link: https://neetcode.io/problems/top-k-elements-in-list/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n log n) | Space: O(n)
# Key Insight: Count frequencies in a dict, sort keys by count descending, and slice [:k].


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return sorted_nums[:k]
