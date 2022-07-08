# MEDIUM
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.A mapping of digits to letters (just like on the telephone buttons) is
# given below. Note that 1 does not map to any letters.
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
#
# Input: digits = ""
# Output: []
#
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List

NUM_MAP = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        combos = []
        queue = [""]
        digits = [digit for digit in digits]

        while queue:
            s = queue.pop()

            if len(s) == len(digits):
                combos.append(s)
            else:
                for letter in NUM_MAP[digits[len(s)]]:
                    queue.append(f"{s}{letter}")

        return combos


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations(""))
    print(solution.letterCombinations("2"))
    print(solution.letterCombinations("257"))
