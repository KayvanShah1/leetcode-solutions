class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        small_num = []
        
        for i in num:
            while small_num and k and small_num[-1] > i:
                small_num.pop()
                k -= 1
            
            # prevent leading zeros
            if small_num or i is not '0':
                small_num.append(i)
        
        # not fully spent
        if k:
            small_num = small_num[0:-k]
            
        return ''.join(small_num) or '0'