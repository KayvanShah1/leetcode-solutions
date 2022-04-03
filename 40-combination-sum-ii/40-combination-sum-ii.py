class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sorting the list
        candidates.sort()
        return self.backtrack(candidates, target)
    
    def backtrack(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # If target is found inside the simply append that into results list
        if target in candidates:
            result.append([target])
            
        for i, num in enumerate(candidates):
            if num > target//2:
                break
                
            elif i==0 or candidates[i] != candidates[i-1]:
                result_next = self.backtrack(candidates[i+1:], target-num)
                for res in result_next:
                    result.append([num] + res)
            
        return result
            
        
        
        