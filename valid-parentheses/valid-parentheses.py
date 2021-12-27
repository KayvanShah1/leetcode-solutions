class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            '(':')', 
            '[':']', 
            '{':'}'
        }
        res = []
        for char in s:
            if char in valid:
                res.append(char)
            else:
                if (len(res) and valid[res[-1]]==char): 
                    del res[-1]
                else:
                    return False
        return res==[]
        