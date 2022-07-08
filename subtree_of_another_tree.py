# EASY
#
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise. A subtree of a binary tree is a tree that consists of
# a node in tree and all of this node's descendants. The tree could also be considered as a subtree of itself.
#
# Example 1:
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
# Example 2:
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        return (
            is_sub_tree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


def is_sub_tree(node: Optional[TreeNode], sub_node: Optional[TreeNode]) -> bool:
    if node is None and sub_node is None:
        return True
    elif node is None or sub_node is None:
        return False
    elif node.val == sub_node.val:
        return is_sub_tree(node.left, sub_node.left) and is_sub_tree(
            node.right, sub_node.right
        )

    return False


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    sub_root1 = TreeNode(4)
    sub_root1.left = TreeNode(1)
    sub_root1.right = TreeNode(2)

    print(solution.isSubtree(root1, sub_root1))

    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)

    sub_root2 = TreeNode(4)
    sub_root2.left = TreeNode(1)
    sub_root2.right = TreeNode(2)

    print(solution.isSubtree(root2, sub_root2))
