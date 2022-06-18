# EASY
#
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
# Constraints:
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_chars = [char for char in pattern]
        pattern_seen = {}
        pattern_order = []
        s_words = s.split(" ")
        s_seen = {}
        s_order = []

        pattern_count = 0
        for char in pattern_chars:
            if char not in pattern_seen:
                pattern_seen[char] = pattern_count
                pattern_count += 1
            pattern_order.append(pattern_seen[char])

        s_count = 0
        for word in s_words:
            if word not in s_seen:
                s_seen[word] = s_count
                s_count += 1
            s_order.append(s_seen[word])

        return pattern_order == s_order


if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))
    print(solution.wordPattern("abba", "dog cat cat fish"))
    print(solution.wordPattern("aaaa", "dog cat cat dog"))
