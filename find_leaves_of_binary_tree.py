# MEDIUM
#
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until
# the tree is empty.
#
# Example1
# Input: {1,2,3,4,5}
# Output: [[4, 5, 3], [2], [1]].
# Explanation:
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# Example2
# Input: {1,2,3,4}
# Output: [[4, 3], [2], [1]].
# Explanation:
#
#     1
#    / \
#   2   3
#  /
# 4

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = defaultdict(list)
        self.find_leaves(root, result, 0)
        return list(result.values())

    def find_leaves(self, node: Optional[TreeNode], result, height) -> int:
        if node is None:
            return height

        lhs = self.find_leaves(node.left, result, height)
        rhs = self.find_leaves(node.right, result, height)

        height = max(lhs, rhs)
        result[height].append(node.val)

        return height + 1


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(solution.findLeaves(root1))

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    print(solution.findLeaves(root2))

    print(solution.findLeaves(None))
