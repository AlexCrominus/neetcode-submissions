class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.check(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def check(self, r, s):
        if not r and not s:
            return True

        if not r or not s:
            return False

        if r.val != s.val:
            return False

        return (
            self.check(r.left, s.left) and
            self.check(r.right, s.right)
        )