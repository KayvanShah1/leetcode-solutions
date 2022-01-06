class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # empty strings
        if len(s) == 0:
            return [[]]
        
        def loops(relt, tmp, s):
            if len(s) == 0:
                relt.append(list(tmp))
                return
            
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    loops(relt, tmp+[s[:i]], s[i:])
                    
        relt = []
        loops(relt, [], s)
                    
        return relt
        