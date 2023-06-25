# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def iot(node):
            if node is None:
                return
                
            iot(node.left)
            iot(node.right)
            output.append(node.val)
            
        iot(root)
        return output