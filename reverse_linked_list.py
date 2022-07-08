# EASY
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
#
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
#
# Input: head = []
# Output: []
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        out = ""

        while node:
            out = f"{out} {node.val}"
            node = node.next

        return out


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        while head:
            tmp_next = head.next
            head.next = new_head
            new_head = head
            head = tmp_next

        return new_head

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        return self.reverse_recursive(head, None)

    def reverse_recursive(
        self, cur: ListNode, next=Optional[ListNode]
    ) -> Optional[ListNode]:
        remaining = cur.next
        cur.next = next

        if remaining is None:
            return cur
        else:
            return self.reverse_recursive(remaining, cur)


if __name__ == "__main__":
    solution = Solution()

    root1 = ListNode(1)
    root1.next = ListNode(2)
    root1.next.next = ListNode(3)
    root1.next.next.next = ListNode(4)
    root1.next.next.next.next = ListNode(5)
    print(solution.reverseList(root1))

    root1 = ListNode(1)
    root1.next = ListNode(2)
    print(solution.reverseList(root1))

    print(solution.reverseList(None))
