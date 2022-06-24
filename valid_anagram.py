# EASY
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or
# phrase formed by rearranging the letters of a different word or phrase, typically using all the original
# letters exactly once.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted([char for char in s]) == sorted([char for char in t])


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
