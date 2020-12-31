class Solution:
    def myAtoi(self, s: str) -> int:
        max_int = 2 ** 31 - 1
        min_int = - 2 ** 31
        
        res = 0
        negative = False
        digit_seen = False
        positive_seen = False
        for element in s:
            if -1 < ord(element) - 48 < 10:
                res = res * 10 + ord(element) - 48
                digit_seen = True
            
            elif element == '-' and not digit_seen and negative == False and not positive_seen:
                negative = True
            elif element == '-':
                break
            elif element == '+' and (digit_seen or negative == True or positive_seen):
                break
            elif element == '+':
                positive_seen = True
            elif element == ' ' and (digit_seen or negative == True or positive_seen):
                break
            elif element == ' ':
                continue
            else:
                break
            
            if negative and -res <= min_int:
                return min_int

            if negative == False and res >= max_int:
                return max_int
                
        if negative:
            res = - res
        
        return res