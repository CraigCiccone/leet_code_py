# EASY
#
# Given a string array words, return an array of all characters that show up in all strings within the
# words (including duplicates). You may return the answer in any order.
#
# Example 1:
#
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
#
# Example 2:
#
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = {}
        for char in words[0]:
            chars[char] = chars.get(char, 0) + 1

        for word in words[1:]:
            cur_chars = {}
            for char in word:
                cur_chars[char] = cur_chars.get(char, 0) + 1

            remove = []
            for char in chars:
                if char not in cur_chars:
                    remove.append(char)
                elif chars[char] > cur_chars[char]:
                    chars[char] = min(chars[char], cur_chars[char])

            for key in remove:
                chars.pop(key)

        result = []
        for char, val in chars.items():
            for _ in range(val):
                result.append(char)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.commonChars(["bella", "label", "roller"]))
    print(solution.commonChars(["cool", "lock", "cook"]))
    print(
        solution.commonChars(
            [
                "bcaddcdd",
                "cbcdccdd",
                "ddccbdda",
                "dacbbdad",
                "dababdcb",
                "bccbdaad",
                "dbccbabd",
                "accdddda",
            ]
        )
    )
