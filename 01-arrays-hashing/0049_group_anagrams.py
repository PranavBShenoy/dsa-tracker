# Problem: 49. Group Anagrams (Medium)
# Link: https://neetcode.io/problems/anagram-groups/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(m * n log n) | Space: O(m * n)
# Key Insight: Group strings under their sorted-character key in a dictionary.


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())
