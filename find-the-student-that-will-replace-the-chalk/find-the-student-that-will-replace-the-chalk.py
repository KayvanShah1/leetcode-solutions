class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        n = k%sm
        
        for i in range(len(chalk)):
            if n-chalk[i] >= 0:
                n=n-chalk[i]
            else:
                return i