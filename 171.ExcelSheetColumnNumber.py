class Solution:
    def titleToNumber(self, s: str) -> int:
        x = 0
        for n, elem in enumerate(s):
            x += (ord(elem) - ord('A') + 1) * (26 ** (len(s) - n - 1))
            
        return x