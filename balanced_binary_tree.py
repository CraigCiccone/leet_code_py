# EASY
#
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# Example 1:
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# Example 2:
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# Example 3:
# Input: root = []
# Output: true
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        lhs_balanced = self.isBalanced(root.left)
        rhs_balanced = self.isBalanced(root.right)
        height_diff = abs(self.height(root.left) - self.height(root.right))

        return height_diff <= 1 and lhs_balanced and rhs_balanced

    def height(self, node: Optional[TreeNode]):
        if node is None:
            return 0

        return max(self.height(node.left), self.height(node.right)) + 1


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.isBalanced(root1))

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(solution.isBalanced(root2))

    print(solution.isBalanced(None))
