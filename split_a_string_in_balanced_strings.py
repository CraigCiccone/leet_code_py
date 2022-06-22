# EASY
#
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters. Given a balanced string s,
# split it in the maximum amount of balanced strings. Return the maximum amount of split balanced strings.
#
# Example 1:
#
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#
# Example 2:
#
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
#
# Example 3:
#
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
#
# Constraints:
#
# 1 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        chars = [char for char in s]
        count = 0

        for char in chars:
            if not stack:
                count += 1
                cur_char = char

            if char == cur_char:
                stack.append(char)
            else:
                stack.pop()

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.balancedStringSplit("RLRRLLRLRL"))
    print(solution.balancedStringSplit("RLLLLRRRLR"))
    print(solution.balancedStringSplit("LLLLRRRR"))
