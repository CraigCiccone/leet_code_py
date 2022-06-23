# EASY
#
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
# has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among
# its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds. Given such
# a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
#
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
# Example 2:
#
# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 2^31 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the tree.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = []
        self.traverse(root, values)
        values = list(set(values))
        values.sort()

        if len(values) > 1:
            return values[1]
        else:
            return -1

    def traverse(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return None

        values.append(node.val)

        self.traverse(node.left, values)
        self.traverse(node.right, values)


if __name__ == "__main__":
    solution = Solution()

    # [2,2,5,null,null,5,7]
    root1 = TreeNode(2)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    print(solution.findSecondMinimumValue(root1))

    # [2,2,2]
    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    print(solution.findSecondMinimumValue(root2))

    # [5, 8, 5]
    root3 = TreeNode(5)
    root3.left = TreeNode(8)
    root3.right = TreeNode(5)
    print(solution.findSecondMinimumValue(root3))
