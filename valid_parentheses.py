# EASY
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.


from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = [char for char in s]

        for char in chars:
            match char:
                case "(":
                    stack.append(char)
                case "[":
                    stack.append(char)
                case "{":
                    stack.append(char)
                case ")":
                    if self.valid("(", stack):
                        continue
                    else:
                        return False
                case "]":
                    if self.valid("[", stack):
                        continue
                    else:
                        return False
                case "}":
                    if self.valid("{", stack):
                        continue
                    else:
                        return False

        return len(stack) == 0

    def valid(self, expected: str, stack: List[str]) -> bool:
        if len(stack) == 0:
            return False
        elif expected == stack.pop():
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("(((("))
    print(solution.isValid("(()"))
    print(solution.isValid("({([])})"))
    print(solution.isValid("]"))
