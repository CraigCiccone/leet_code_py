# MEDIUM
#
# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values
# along the path equals targetSum. The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
# Example 1:
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
# Example 2:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.results = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        self.results = 0
        self.path_sum(root, targetSum, [])
        return self.results

    def path_sum(self, node: Optional[TreeNode], target_sum: int, cur_nums: List[int]):
        if node is None:
            return

        cur_nums.append(node.val)

        if sum(cur_nums) == target_sum:
            self.results += 1

        # Only generate subpaths once, when first visiting a node
        if len(cur_nums) == 1:
            self.path_sum(node.left, target_sum, [])
            self.path_sum(node.right, target_sum, [])

        self.path_sum(node.left, target_sum, cur_nums.copy())
        self.path_sum(node.right, target_sum, cur_nums.copy())


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(2)
    root1.left.left.left = TreeNode(3)
    root1.left.left.right = TreeNode(-2)
    root1.left.right.right = TreeNode(1)
    root1.right = TreeNode(-3)
    root1.right.right = TreeNode(11)
    print(solution.pathSum(root1, 8))

    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    print(solution.pathSum(root2, 1))

    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.right = TreeNode(3)
    root3.right.right.right = TreeNode(4)
    root3.right.right.right.right = TreeNode(5)
    print(solution.pathSum(root3, 3))

    print(solution.pathSum(TreeNode(1), 1))
