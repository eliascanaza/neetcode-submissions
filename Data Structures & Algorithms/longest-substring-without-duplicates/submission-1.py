class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in m:
                l = max(m[s[r]] + 1, l)
            m[s[r]] = r
            longest = max(longest, r - l + 1)
        
        return longest

