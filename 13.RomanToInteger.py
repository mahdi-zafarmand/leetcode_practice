class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        maybe_special = set([5, 10, 50, 100, 500, 1000])
        maybe_prefix = set([1, 10, 100])
        
        res, i = 0, 0
        while i < len(s) - 1:
            current_int = value[s[i]]
            next_int = value[s[i+1]]
            
            if next_int in maybe_special and current_int in (next_int // 5, next_int // 10):
                res += next_int - current_int
                i += 2
            else:
                res += current_int
                i += 1
                
        if i == len(s) - 1:
            res += value[s[-1]]
        return res
    
        
        
#         if len(s) == 0:
#             return 0
        
#         self.chars = ('CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I')
#         self.nums = (900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1)
        
#         index1, index2 = 0, 2
#         res = 0
        
#         while index1 < len(s):
#             found = False
            
#             for i in range(len(self.chars)):
#                 if i == 6:
#                     index2 -= 1
#                 if self.chars[i] == s[index1:index2]:
#                     res += self.nums[i]
#                     index1 = index2
#                     index2 = index1 + 2
#                     break
#         return res

