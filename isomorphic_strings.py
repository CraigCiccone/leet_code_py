# EASY
#
# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in
# s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving
# the order of characters. No two characters may map to the same character, but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
# Constraints:
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_normalized = normalize_str(s)
        t_normalized = normalize_str(t)

        return s_normalized == t_normalized


def normalize_str(word: str) -> str:
    normalized_val = 0
    char_map = {}
    normalized = ""

    for char in word:
        if char not in char_map:
            char_map[char] = normalized_val
            normalized_val += 1

        normalized = f"{normalized} {char_map[char]}"

    return normalized


if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))
    print(
        solution.isIsomorphic(
            "abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"
        )
    )
