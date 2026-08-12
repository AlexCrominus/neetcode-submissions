class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        if root.left:
            if root.left.val < root.val:
                left = self.isValidBST(root.left, min_val, root.val)
            else:
                return False
        else:
            left = True

        if root.right:
            if root.right.val > root.val:
                right = self.isValidBST(root.right, root.val, max_val)
            else:
                return False
        else:
            right = True

        return left and right