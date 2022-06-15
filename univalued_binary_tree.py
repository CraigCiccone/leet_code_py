# EASY
#
# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
#
# Example 1:
#
# Input: root = [1,1,1,1,1,null,1]
# Output: true
#
# Example 2:
#
# Input: root = [2,2,2,5,2]
# Output: false
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)

    def traverse(self, node: Optional[TreeNode], val=None) -> bool:
        if not node:
            return True

        # constraints state at least 1 node, so val is set at first node
        if not val:
            val = node.val

        if node.left and node.left.val != val or node.right and node.right.val != val:
            return False

        return self.traverse(node.left, val) and self.traverse(node.right, val)


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    lhs1 = TreeNode(1)
    lhs1.left = TreeNode(1)
    lhs1.right = TreeNode(1)
    rhs1 = TreeNode(1)
    rhs1.right = TreeNode(1)
    root1.left = lhs1
    root1.right = rhs1
    print(solution.isUnivalTree(root1))

    root2 = TreeNode(2)
    lhs2 = TreeNode(2)
    lhs2.left = TreeNode(5)
    lhs2.right = TreeNode(2)
    rhs2 = TreeNode(2)
    root2.left = lhs2
    root2.right = rhs2
    print(solution.isUnivalTree(root2))

    root3 = TreeNode(0)
    lhs3 = TreeNode(6)
    rhs3 = TreeNode(0)
    rhs3.right = TreeNode(0)
    root3.left = lhs3
    root3.right = rhs3
    print(solution.isUnivalTree(root3))

    root4 = TreeNode(0)
    print(solution.isUnivalTree(root4))
