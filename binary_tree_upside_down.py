# MEDIUM
#
# Given the root of a binary tree, turn the tree upside down and return the new root. You can turn a binary tree upside
# down with the following steps:
# 1. The original left child becomes the new root
# 2. The original root becomes the new right child
# 3. The original right child becomes the new left child
#
# The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2
# children.
#
# Example 1:
#
# Input: {1,2,3,4,5}
# Output: {4,5,2,#,#,3,1}
# Explanation:
# The input is
#     1
#    / \
#   2   3
#  / \
# 4   5
# and the output is
#    4
#   / \
#  5   2
#     / \
#    3   1
#
# Example 2:
#
# Input: {1,2,3,4}
# Output: {4,#,2,3,1}
# Explanation:
# The input is
#     1
#    / \
#   2   3
#  /
# 4
# and the output is
#    4
#     \
#      2
#     / \
#    3   1
#
# Constraints
# The number of nodes in the tree will be in the range [0, 10].
# 1 <= Node.val <= 10
# Every node has either 0 or 2 children

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upside_down_binary_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left and root.right:
            new_root = self.upside_down_binary_tree(root.left)
            root.left.left = root.right
            root.left.right = root

            root.left = None
            root.right = None

            return new_root
        else:
            return root


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(solution.upside_down_binary_tree(root1))

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    print(solution.upside_down_binary_tree(root2))

    print(solution.upside_down_binary_tree(None))

    print(solution.upside_down_binary_tree(TreeNode(1)))
