# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        node_stack = []
        sum_stack = []

        node_stack.append(root)
        sum_stack.append(targetSum - root.val)

        while node_stack:
            curr_node = node_stack.pop()
            curr_sum = sum_stack.pop()

            if (
                curr_node.left is None 
                and curr_node.right is None
                and curr_sum == 0
            ):
                return True

            if curr_node.left is not None:
                sum_stack.append(curr_sum - curr_node.left.val)
                node_stack.append(curr_node.left)

            if curr_node.right is not None:
                sum_stack.append(curr_sum - curr_node.right.val)
                node_stack.append(curr_node.right)

        return False

            