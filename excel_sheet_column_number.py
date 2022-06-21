# EASY
#
# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
# Example 1:
#
# Input: columnTitle = "A"
# Output: 1
#
# Example 2:
#
# Input: columnTitle = "AB"
# Output: 28
#
# Example 3:
#
# Input: columnTitle = "ZY"
# Output: 701
#
# Constraints:
#
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapping = {val: idx + 1 for idx, val in enumerate(ascii_uppercase)}
        title_chars = [char for char in columnTitle]
        title_chars.reverse()

        total = 0
        for idx, char in enumerate(title_chars):
            if idx == 0:
                total += mapping[char]
            else:
                total += mapping[char] * pow(26, idx)

        return total


if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber("A"))
    print(solution.titleToNumber("AB"))
    print(solution.titleToNumber("ZY"))
    print(solution.titleToNumber("FXSHRXW"))
