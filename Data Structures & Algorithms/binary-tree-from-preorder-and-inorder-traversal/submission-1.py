# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder, inorder):
            if len(preorder) == 0:
                return None
            root = preorder[0]
            index_root = inorder.index(root)
            left = inorder[:index_root]
            right = inorder[index_root + 1:]
            
            return TreeNode(root, helper([i for i in preorder if i in left], left), helper([i for i in preorder if i in right], right))

        return helper(preorder, inorder)
            
        