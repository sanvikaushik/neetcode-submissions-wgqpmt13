# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        if not root:
            return False

        if root.val == subRoot.val:
            stack = [(root, subRoot)]
            same = True

            while stack:
                a, b = stack.pop()

                if not a and not b:
                    continue
                
                if not a or not b or a.val != b.val:
                    same = False
                    break
                
                stack.append((a.left, b.left))
                stack.append((a.right, b.right))
            
            if same:
                return True
        
        # recursively
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
