class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for elem in s:
            if (elem in d) is False:
                d[elem] = 1
            else:
                d[elem] += 1
            
        for e, elem in enumerate(s):
            if d[elem] == 1:
                return e
        return -1