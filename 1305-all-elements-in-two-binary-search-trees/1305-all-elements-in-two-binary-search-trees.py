# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(
            self.traverse(root1) + self.traverse(root2)
        )
    
    def traverse(self, root):
        if not root:
            return []
        else:
            return (
                self.traverse(root.left) +
                [root.val] +
                self.traverse(root.right)
            )