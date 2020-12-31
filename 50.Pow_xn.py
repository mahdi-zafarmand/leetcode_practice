class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        
        abs_n = max(n, -n)
        
        res = x
        p = 1

        while p * 2 <= abs_n:
            res = res * res
            p *= 2

        if n > 0:
            return res * self.myPow(x, n - p)
        else:
            return 1 / res * self.myPow(x, n + p)
        
        