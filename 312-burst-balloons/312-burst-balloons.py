class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def search(nums):
            return (
                0 
                if len(nums) < 3 
                else max(
                    [
                        search(nums[:i + 1]) 
                        + search(nums[i:]) 
			            + nums[0] 
                        * nums[i] 
                        * nums[-1] 
                        for i in range(1, len(nums) - 1)
                    ]
                )
            )
        return search(tuple([1] + nums + [1]))