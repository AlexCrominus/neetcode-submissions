# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root: Optional[TreeNode]) -> (bool, int):

            if not root:
                return (True, 0)
            print((abs(depth(root.left)[1] - depth(root.right)[1]) <= 1 and (depth(root.left)[0] and depth(root.right)[0]), 1+max(depth(root.left)[1], depth(root.right)[1])))
            return (abs(depth(root.left)[1] - depth(root.right)[1]) <= 1 and (depth(root.left)[0] and depth(root.right)[0]), 1+max(depth(root.left)[1], depth(root.right)[1]))

        return depth(root)[0]