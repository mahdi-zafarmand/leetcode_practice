class Solution:
    def divide(self, dividend: int, divisor: int) -> int:        
        max_val = 2 ** 31 - 1
        min_val = - 2 ** 31

        if divisor == 1:
            return min(dividend, max_val)
        if divisor == -1:
            return min(-dividend, max_val)

        negative = False
        if dividend < 0:
            negative = not negative
        if divisor < 0:
            negative = not negative
        dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        pows = []
        power = 1
        while power * divisor <= dividend:
            power = divisor ** len(pows)
            pows.append(power)

        ans = 0
        while len(pows) > 1:
            power = pows.pop()
            x = 0
            while dividend - power >= 0:
                x += 1
                dividend -= power
            ans += x * divisor ** (len(pows) - 1)

        if negative == True:
            ans = - ans

        if ans > max_val:
            return max_val
        if ans < min_val:
            return max_val

        return ans