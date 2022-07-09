# EASY
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked
# list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is
# not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Constraints:
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        if head is None:
            return False

        while head:
            if head in seen:
                return True
            seen[head] = head.val
            head = head.next

        return False


if __name__ == "__main__":
    solution = Solution()

    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(-4)
    head1.next.next.next.next = head1.next
    print(solution.hasCycle(head1))

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next = head2
    print(solution.hasCycle(head2))

    head3 = ListNode(1)
    print(solution.hasCycle(head3))
