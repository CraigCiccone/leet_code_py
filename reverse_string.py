# EASY
#
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


if __name__ == "__main__":
    solution = Solution()
    solution.reverseString(["h", "e", "l", "l", "o"])
    solution.reverseString(["H", "a", "n", "n", "a", "h"])
