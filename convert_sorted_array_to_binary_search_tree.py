# EASY
#
# Given an integer array nums where the elements are sorted in ascending order, convert it to
# a height-balanced binary search tree. A height-balanced binary tree is a binary tree in which
# the depth of the two subtrees of every node never differs by more than one.
#
# Example 1:
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
# Constraints:
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        return self.convert(nums, 0, len(nums) - 1)

    def convert(self, nums: List[int], l_idx: int, r_idx: int) -> Optional[TreeNode]:
        if l_idx > r_idx:
            return None

        mid_idx = l_idx + (r_idx - l_idx) // 2
        node = TreeNode(nums[mid_idx])
        node.left = self.convert(nums, l_idx, mid_idx - 1)
        node.right = self.convert(nums, mid_idx + 1, r_idx)

        return node


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedArrayToBST([-10, -3, 0, 5, 9]))
    print(solution.sortedArrayToBST([1, 3]))
    print(solution.sortedArrayToBST([]))
