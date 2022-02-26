### Description:
1. Essentially, what we asked to do here is to convert a number in the base 26 numeral system to a decimal number.
1. This is a standard algorithm, where we iterate over the digits from right to left and multiply them by the base to the power of the position of the digit.
1. To translate a letter to a number we use the Python method ord which returns the Unicode code of the letter.
1. By subtracting the code by 64, we can map letters to the numbers from 1 to 26.
​
```py
class Solution:
def titleToNumber(self, columnTitle: str) -> int:
ans, pos = 0, 0
for letter in reversed(columnTitle):
digit = ord(letter)-64
ans += digit * 26**pos
pos += 1
```
return ans