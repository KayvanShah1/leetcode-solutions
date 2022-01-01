class Solution:
    def intToRoman(self, num: int) -> str:
        numeral = ''
        
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        for i,n in enumerate(nums):
            while num >= n:
                numeral += roman[i]
                num -= n
            
                
        return numeral