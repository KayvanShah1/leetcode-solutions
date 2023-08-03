class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index = 0
        direction = -1

        for char in s:
            result[index] += char
            if index == 0 or index == numRows - 1:
                direction *= -1
            index += direction

        return ''.join(result)
