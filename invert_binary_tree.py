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
        if not root:
            return None
        else:
            self.swap(root)

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root

    def swap(self, node: Optional[TreeNode]):
        tmp = node.left
        node.left = node.right
        node.right = tmp


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(4)
    lhs1 = TreeNode(2)
    lhs1.left = TreeNode(1)
    lhs1.right = TreeNode(3)
    rhs1 = TreeNode(7)
    rhs1.left = TreeNode(6)
    rhs1.right = TreeNode(9)
    print(solution.invertTree(root1))

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.left = TreeNode(3)
    print(solution.invertTree(root2))

    root3 = None
    print(solution.invertTree(root3))
