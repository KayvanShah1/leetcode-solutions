class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # for adding all the answers
        self.ans = []                                   
        self.traverse(candidates,[], 0, target)
        return self.ans
    
    def traverse(self, candid, arr, sm, target): 
        """
        arr : an array that contains the accused combination 
        sm : is the sum of all elements of arr
        target: required sum
        """
        
        # If sum is equal to target then append to the ans list
        if sm == target: 
            self.ans.append(arr)
            
        # If sum is greater than target then no need to move further.
        if sm >= target: 
            return                     
        
        # we will traverse each element from the array.
        # splice the array including the current index
        # splicing in order to handle the duplicates.
        for i in range(len(candid)):                
            self.traverse(
                candid[i:], 
                arr + [candid[i]], 
                sm + candid[i], 
                target
            )   