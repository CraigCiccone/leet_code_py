# EASY
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# Example 1:
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Example 2:
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
# Example 3:
#
# Input: root = []
# Output: []
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)

        return root


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right = TreeNode(7)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    print(solution.invertTree(root1))

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.left = TreeNode(3)
    print(solution.invertTree(root2))

    root3 = None
    print(solution.invertTree(root3))
