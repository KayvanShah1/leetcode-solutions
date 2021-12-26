class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            if x >= 0:
                rev = int(str(x)[::-1])
            else:
                rev = -1*int(str(-1*x)[::-1])
                
            if rev >= 2**31-1 or rev <= -2**31:
                return 0
            else:
                return rev