# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
# Input: root = [2,1,3]
# Output: true
#
# Example 2:
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -2^31 <= Node.val <= 2^31 - 1

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)

    def validate(self, node: Optional[TreeNode], least: Optional[int], most: Optional[int]) -> bool:
        if not node:
            return True
        elif least is not None and node.val <= least:
            return False
        elif most is not None and node.val >= most:
            return False
        
        return self.validate(node.left, least, node.val) and self.validate(node.right, node.val, most)


if __name__ == "__main__":
    solution = Solution()
    
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(solution.isValidBST(root1))

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    rhs = TreeNode(4)
    rhs.left = 3
    rhs.right = 4
    root2.right = rhs
    print(solution.isValidBST(root2))
