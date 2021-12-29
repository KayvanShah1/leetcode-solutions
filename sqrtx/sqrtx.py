class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        low = 1
        high = x
        
        while low < high:
            mid = (low + high) // 2
            next = mid + 1
            if mid*mid <= x and next*next > x:
                return mid
            elif mid*mid > x:
                high = mid
            else:
                low = mid