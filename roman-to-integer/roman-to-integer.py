class Solution:
    rmap = {
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    }
    
    def romanToInt(self, s: str) -> int:
        sol = self.rmap[s[-1]]
        if len(s) > 1:
            for i in range(len(s)-2,-1,-1):
                if self.rmap[s[i]] < self.rmap[s[i+1]]:
                    sol -= self.rmap[s[i]]
                else:
                    sol += self.rmap[s[i]]
        return sol