class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in d:
                start = max(start, d[s[i]] + 1)
            d[s[i]] = i
            curr_len = i - start + 1
            if curr_len > l:
                l = curr_len
        return l