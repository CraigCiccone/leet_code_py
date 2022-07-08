# EASY
#
# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
# are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then
# sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the
# new tree. Return the merged tree. Note: The merging process must start from the root nodes of both trees.
#
# Example 1:
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
# Example 2:
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#
# Constraints:
#
# The number of nodes in both trees is in the range [0, 2000].
# -10^4 <= Node.val <= 10^4

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        return self.merge_trees(root1, root2)

    def merge_trees(
        self, node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        node = TreeNode()

        if node1 is None and node2 is None:
            return None
        elif node1 is None:
            node.val = node2.val
            node.left = self.merge_trees(None, node2.left)
            node.right = self.merge_trees(None, node2.right)
        elif node2 is None:
            node.val = node1.val
            node.left = self.merge_trees(node1.left, None)
            node.right = self.merge_trees(node1.right, None)
        else:
            node.val = node1.val + node2.val
            node.left = self.merge_trees(node1.left, node2.left)
            node.right = self.merge_trees(node1.right, node2.right)

        return node


if __name__ == "__main__":
    solution = Solution()

    root1_e1 = TreeNode(1)
    root1_e1.left = TreeNode(3)
    root1_e1.right = TreeNode(2)
    root1_e1.left.left = TreeNode(5)

    root2_e1 = TreeNode(2)
    root2_e1.left = TreeNode(1)
    root2_e1.right = TreeNode(3)
    root2_e1.left.right = TreeNode(4)
    root2_e1.right.right = TreeNode(7)

    print(solution.mergeTrees(root1_e1, root2_e1))

    root1_e2 = TreeNode(1)

    root2_e2 = TreeNode(1)
    root2_e2.left = TreeNode(2)

    print(solution.mergeTrees(root1_e2, root2_e2))
