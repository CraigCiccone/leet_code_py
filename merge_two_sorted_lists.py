# EASY
#
# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The
# list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.
#
# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Add print support
    def __str__(self):
        node = self
        result = ""

        while node:
            result += f"{node.val}, "

            if not node.next:
                break
            else:
                node = node.next

        return result


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    solution = Solution()

    list1a = ListNode(1)
    list1a.next = ListNode(2)
    list1a.next.next = ListNode(4)
    list1b = ListNode(1)
    list1b.next = ListNode(3)
    list1b.next.next = ListNode(4)

    print(solution.mergeTwoLists(list1a, list1b))

    # print(solution.mergeTwoLists(None, None))

    # list3b = ListNode(0)
    # print(solution.mergeTwoLists(None, list3b))

    # list4a = ListNode(0)
    # print(solution.mergeTwoLists(list4a, None))
