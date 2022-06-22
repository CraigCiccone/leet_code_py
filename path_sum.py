# EASY
#
# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
#
# Example 1:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
# Example 2:
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
# Example 3:
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, found: bool = False):
        self.found = found

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        self.find_sum(root, targetSum, [])
        return self.found

    def find_sum(self, root: Optional[TreeNode], targetSum: int, values: List[int]):
        if root is None:
            return

        values.append(root.val)

        if root.left is None and root.right is None and sum(values) == targetSum:
            self.found = True

        self.find_sum(root.left, targetSum, values.copy())
        self.find_sum(root.right, targetSum, values.copy())


if __name__ == "__main__":
    solution = Solution()

    # [5,4,8,11,null,13,4,7,2,null,null,null,1]
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.right.right = TreeNode(1)
    print(solution.hasPathSum(root1, 22))

    #  [1,2,3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(solution.hasPathSum(root2, 5))

    # []
    print(solution.hasPathSum(None, 0))
