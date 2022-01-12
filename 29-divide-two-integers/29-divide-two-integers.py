class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        return sign * self._helper(abs(dividend), abs(divisor))

    def _helper(self, dividend: int, divisor: int) -> int:
        if dividend < divisor:
            return 0
        exp = 0
        while dividend > (divisor << (exp+1)):
            exp += 1
        return (1 << exp) + self._helper(dividend - (divisor << exp), divisor)