# EASY
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
#
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        total = 0

        if low <= root.val <= high:
            total += root.val

        total += self.rangeSumBST(root.left, low, high)
        total += self.rangeSumBST(root.right, low, high)

        return total


if __name__ == "__main__":
    solution = Solution()

    # [10,5,15,3,7,null,18]
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.left = None
    root1.right.right = TreeNode(18)
    print(solution.rangeSumBST(root1, 7, 15))

    # [10,5,15,3,7,13,18,1,null,6]
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(13)
    root2.right.right = TreeNode(18)
    root2.left.left.left = TreeNode(1)
    root2.left.left.right = None
    root2.left.right.left = TreeNode(6)
    print(solution.rangeSumBST(root2, 6, 10))
