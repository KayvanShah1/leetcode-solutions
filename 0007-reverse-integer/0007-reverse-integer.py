class Solution:
    def reverse(self, x: int) -> int:
        MIN=-2**31
        MAX=(2**31)-1
        res = 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rem = x % 10
            x //= 10

            if res > MAX//10 or (res==MAX//10 and rem > MAX%10):
                return 0
            if res < MIN//10 or (res==MIN//10 and rem < MIN%10):
                return 0

            res = res * 10 + rem
        
        return sign*res