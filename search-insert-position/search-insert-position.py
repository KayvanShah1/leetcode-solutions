class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target > nums[-1]:
            index = len(nums)
        elif target in nums:
            while nums[index] != target:
                index += 1
        else:
            while nums[index] < target:
                index += 1
        return index