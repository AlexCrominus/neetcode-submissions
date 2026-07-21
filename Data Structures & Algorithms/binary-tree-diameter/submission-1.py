class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter

            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Longest path passing through this node
            diameter = max(diameter, left_depth + right_depth)

            # Depth of this subtree
            return 1 + max(left_depth, right_depth)

        depth(root)
        return diameter