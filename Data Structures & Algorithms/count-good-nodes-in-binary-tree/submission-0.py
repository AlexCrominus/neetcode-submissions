# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, m):
            nonlocal good

            if not root:
                return

            if root.val >= m:
                good += 1
                m = root.val

            dfs(root.left, m)
            dfs(root.right, m)

        dfs(root, float('-inf'))
        return good
