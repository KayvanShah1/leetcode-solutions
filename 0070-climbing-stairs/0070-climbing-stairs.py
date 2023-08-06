class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        stack = [0] * (n+1)
        for i in range(3):
            stack[i] = i

        for i in range(3, n+1):
            stack[i] = stack[i-1] + stack[i-2]

        return stack[n]
