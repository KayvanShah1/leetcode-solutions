# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rec = []

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is not None:
            complement = k - root.val 
            if complement in self.rec:
                return True

            self.rec.append(root.val)

            return (
                self.findTarget(root.left, k) 
                or self.findTarget(root.right, k)
            )
                
        return False

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, seen):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)            
            return dfs(node.left, seen) or dfs(node.right, seen)
        
        return dfs(root, set())