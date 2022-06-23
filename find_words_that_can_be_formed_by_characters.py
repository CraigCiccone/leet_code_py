# EASY
#
# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
#
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
# Constraints:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0

        for word in words:
            cur_chars = [char for char in chars]
            for char in word:
                if char in cur_chars:
                    cur_chars.remove(char)
                else:
                    break
            else:
                total += len(word)

        return total


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
    print(solution.countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"))
