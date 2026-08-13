class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        m = {}

        for r in range(len(s)):
            if s[r] in m:
                l = max(l, m[s[r]] + 1)
            m[s[r]] = r
            longest = max(longest, r - l +1)

        return longest