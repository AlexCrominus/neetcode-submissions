# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            return self.findMin(root.left)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        print(root.val)
        if root.val == key:
            print("FOUND", key)

            if root.right == None:
                return root.left
            elif root.left == None:
                return root.right
            else:
                minNode = self.findMin(root.right)
                root.right = self.deleteNode(root.right, minNode.val)
                root.val = minNode.val
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        return root

        