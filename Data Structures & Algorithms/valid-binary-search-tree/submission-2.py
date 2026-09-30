# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high):
            # 1. Base case
            if not node:
                return True

            # 2. Check if current node is valid
            if not (low < node.val < high):
                return False

            # 3. Recursively check left and right subtrees
            return (
                valid(node.left, low, node.val) and
                valid(node.right, node.val, high)
            )

        # doesnt check relative to fulls subtree just the node -> how to check this??
        return valid(root, float("-inf"), float("inf"))