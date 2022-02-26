class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in set(t):                    
            #for each unique character in t, count the number of it in each string and compare
            if s.count(c) < t.count(c):     
                #if there is more of that character in t, it is the one that was added
                return c