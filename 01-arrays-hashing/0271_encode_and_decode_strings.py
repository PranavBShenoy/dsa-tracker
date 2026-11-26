# Problem: 271. Encode and Decode Strings (Medium)
# Link: https://neetcode.io/problems/string-encode-and-decode/question\?list\=neetcode150
# Status: Green | Pattern: Arrays & Hashing
# Time: O(m) | Space: O(m)
# Key Insight: Prefix each string with "<len>#" so decode knows exact slice length.


class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            res.append(s[start : start + length])
            i = start + length
        return res
