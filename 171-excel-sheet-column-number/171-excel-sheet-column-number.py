class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        
        for i,letter in enumerate(list(columnTitle)[::-1]):
            columnNumber += (ord(letter)-64) * (26**i)
            
        return columnNumber