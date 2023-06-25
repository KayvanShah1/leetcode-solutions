# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if root is None:
            return output

        stack = [root]
        while stack:
            level = []
            next_stack = []

            for node in stack:
                if node is not None:
                    level.append(node.val)
                if node.left is not None:
                    next_stack.append(node.left)
                if node.right is not None:
                    next_stack.append(node.right)

            output.append(level)
            stack = next_stack

        return output