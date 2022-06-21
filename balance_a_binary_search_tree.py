# MEDIUM
#
# Given the root of a binary search tree, return a balanced binary search tree with the same node values.
# If there is more than one answer, return any of them.A binary search tree is balanced if the depth of
# the two subtrees of every node never differs by more than 1.
#
# Example 1:
#
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# Example 2:
#
# Input: root = [2,1,3]
# Output: [2,1,3]
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 10^5

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        self.traverse(root, values)
        values.sort()

        return self.balance(values, 0, len(values) - 1)

    def balance(self, values: List[int], low: int, high: int) -> Optional[TreeNode]:
        if high < low:
            return None

        mid = low + (high - low) // 2

        node = TreeNode(values[mid])
        node.left = self.balance(values, low, mid - 1)
        node.right = self.balance(values, mid + 1, high)

        return node

    def traverse(self, node: TreeNode, values: List[int]):
        if node is None:
            return

        values.append(node.val)
        self.traverse(node.left, values)
        self.traverse(node.right, values)


if __name__ == "__main__":
    solution = Solution()

    # [1, null, 2, null, 3, null, 4, null, null]
    root1 = TreeNode()
    root1.left = TreeNode(1)
    root1.left.left = TreeNode(2)
    root1.left.left.left = TreeNode(3)
    root1.left.left.left.left = TreeNode(4)
    print(solution.balanceBST(root1))

    # [2,1,3]
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print(solution.balanceBST(root2))
