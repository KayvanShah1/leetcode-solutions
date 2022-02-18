class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for each in nums: 
            unique ^= each   
        return unique