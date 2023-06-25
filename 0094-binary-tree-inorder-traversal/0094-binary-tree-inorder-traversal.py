# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def iot(node):
            if node is None:
                return
                
            iot(node.left)
            output.append(node.val)
            iot(node.right)
            
        iot(root)
        return output

        
        