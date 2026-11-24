# Problem: 242. Valid Anagram (Easy)
# Link: https://neetcode.io/problems/is-an-anagram/question
# Status: Green | Pattern: Arrays & Hashing
# Time: O(n) | Space: O(k) (k = unique chars)
# Key Insight: Return False early if lengths differ; otherwise compare character frequency dicts.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t
