# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is not None:

            if not self.isValidBST(root.left):
                return False

            if (
                self.prev is not None and 
                self.prev.val >= root.val  
            ):
                return False

            self.prev = root
            return self.isValidBST(root.right)

        return True
