from itertools import combinations


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):  
            # to have a tuple, we need at least two elements to the right
            if i >= 1 and v == nums[i-1]:  
                # avoid duplicates (only need to consider value 'v' once)
                continue
            d = {}
            for x in nums[i+1:]:
                s = v + x
                if -s in d:  
                    # since nums is sorted, if value -s exists in nums,
				    # it must have already been visited and inserted into d
                    res.add((v, -s, x))  
                    # since we are adding to a set, duplicates will not be inserted
					# moreover, because nums is sorted, we can only have tuples 
                    # containing elements v, -s, and x in this order (v, -s, x)
                d[x] = 1 
        return res