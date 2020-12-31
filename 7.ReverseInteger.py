class Solution:
    def reverse(self, x: int) -> int:
        limit = 2147483648
            
        neg_sign = x < 0
        x = max(x, -x)
        
        x_rev = int(str(x)[::-1])
        
        if neg_sign:
            x_rev = - x_rev
            
        if -limit > x_rev or limit - 1 < x_rev:
            x_rev = 0
        return x_rev
        
        