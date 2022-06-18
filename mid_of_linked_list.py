# EASY
#
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        size = 1
        cur = head
        while cur.next:
            size += 1
            cur = cur.next

        mid_node = head
        for _ in range(size // 2):
            mid_node = mid_node.next

        return mid_node


if __name__ == "__main__":
    solution = Solution()

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    print(solution.middleNode(head1))

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = ListNode(6)
    print(solution.middleNode(head2))
