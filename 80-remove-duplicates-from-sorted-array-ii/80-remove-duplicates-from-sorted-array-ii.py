class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # We don't have to worry about the first two 
        # (0, 1 array index) numbers in the array.
        
		# We have to decide whether to keep the third 
        # (array index 2) element or overwrite it and so on.
        
        write_index = 2
        for i in range(2, len(nums)):
		    # If the last two numbers in the array are the same 
            # as the current one, don't increment the write_index.
			# Our search for the next number to be added to the list 
            # continues.
            
            if nums[write_index - 2] == nums[write_index - 1] == nums[i]:
                continue
                
			# We have found a non duplicate, copy the number into 
            # the position of the write_index and increment it.
            
            nums[write_index] = nums[i]
            write_index += 1

        return write_index
            
                