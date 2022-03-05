class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True
        
        m = len(s)
        n = len(t)
        
        return self.subsequence(s,t,m,n)
        
    def subsequence(self, s: str, t: str, m: int, n: int) -> str:
        if m == 0:
            return True
        if n == 0:
            return False
        
        if s[m-1] == t[n-1]:
            return self.subsequence(s,t,m-1,n-1)
        return self.subsequence(s,t,m,n-1)
        