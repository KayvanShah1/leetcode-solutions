# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        parent = None
        new_node = TreeNode(val)

        # Search for parent node
        while current is not None:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        # Insert new node
        if parent is None:
            root = new_node
        elif val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        return root


            