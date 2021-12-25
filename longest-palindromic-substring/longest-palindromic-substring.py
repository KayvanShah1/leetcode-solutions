class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Assuming the first character as palindrome str
        maxSubString = s[0]
        
        for i in range(len(s)):
            for j in range(i + len(maxSubString), len(s) + 1):
                pivotLength = ((j - i) // 2) + 1
                subString = s[i:j]
                if subString[:pivotLength] == subString[-pivotLength:][::-1]:
                    if len(subString) > len(maxSubString):
                        maxSubString = subString
        return maxSubString