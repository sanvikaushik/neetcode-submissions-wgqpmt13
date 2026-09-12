# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # build a parents dict
        queue = [root]
        parents = {root: None}

        while queue:

            node = queue.pop(0)

            if node.left:
                parents[node.left] = node
                queue.append(node.left)

            if node.right:  
                parents[node.right] = node
                queue.append(node.right)
        
        # now i have all parents 
        # [5: None, 3: 5, 8: 5....]


        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parents[p]

        while q not in p_ancestors:
            q = parents[q]
        
        return q


        # now LCA
        # build a parents queue of the node that is a child

