# MEDIUM
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You
# may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        node = self
        out = "List: "

        while node:
            out += f"{node.val}, "
            node = node.next

        return out


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        l1_vals = []
        l2_vals = []

        while l1 is not None:
            l1_vals.append(str(l1.val))
            l1 = l1.next

        while l2 is not None:
            l2_vals.append(str(l2.val))
            l2 = l2.next

        l1_vals.reverse()
        l2_vals.reverse()

        l1_vals_str = "".join(l1_vals)
        l2_vals_str = "".join(l2_vals)

        if len(l1_vals_str) == 0:
            total = int(l2_vals_str)
        elif len(l2_vals_str) == 0:
            total = int(l1_vals_str)
        else:
            total = int(l1_vals_str) + int(l2_vals_str)

        total_vals = [int(char) for char in str(total)]
        total_vals.reverse()

        cur = ListNode(total_vals.pop())
        while total_vals:
            new = ListNode(total_vals.pop())
            new.next = cur
            cur = new

        return cur


if __name__ == "__main__":
    solution = Solution()

    e0_l1 = ListNode(6)
    e0_l1.next = ListNode(7)
    e0_l1.next.next = ListNode(4)
    e0_l2 = ListNode(5)
    e0_l2.next = ListNode(7)
    print(solution.addTwoNumbers(e0_l1, e0_l2))

    e1_l1 = ListNode(2)
    e1_l1.next = ListNode(4)
    e1_l1.next.next = ListNode(3)
    e1_l2 = ListNode(5)
    e1_l2.next = ListNode(6)
    e1_l2.next.next = ListNode(4)
    print(solution.addTwoNumbers(e1_l1, e1_l2))

    e2_l1 = ListNode(0)
    e2_l2 = ListNode(0)
    print(solution.addTwoNumbers(e2_l1, e2_l2))

    e3_l1 = ListNode(9)
    e3_l1.next = ListNode(9)
    e3_l1.next.next = ListNode(9)
    e3_l1.next.next.next = ListNode(9)
    e3_l1.next.next.next.next = ListNode(9)
    e3_l1.next.next.next.next.next = ListNode(9)
    e3_l1.next.next.next.next.next.next = ListNode(9)
    e3_l2 = ListNode(9)
    e3_l2.next = ListNode(9)
    e3_l2.next.next = ListNode(9)
    e3_l2.next.next.next = ListNode(9)
    print(solution.addTwoNumbers(e3_l1, e3_l2))

    print(solution.addTwoNumbers(None, None))
    print(solution.addTwoNumbers(None, ListNode(1)))
    print(solution.addTwoNumbers(ListNode(1), None))
