# EASY
#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# You may assume that word1 does not equal word2, and word1 and word2 are both in the list.
#
# Example 1:
#
# Input：["practice", "makes", "perfect", "coding", "makes"],"coding","practice"
# Output：3
# Explanation：index("coding") - index("practice") = 3
#
# Example 2:
#
# Input：["practice", "makes", "perfect", "coding", "makes"],"makes","coding"
# Output：1
# Explanation：index("makes") - index("coding") = 1

from typing import List


class Solution:
    def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
        idx_w1 = -1
        idx_w2 = -1
        dist = float("inf")

        for idx in range(len(words)):
            if words[idx] == word1:
                idx_w1 = idx

            if words[idx] == word2:
                idx_w2 = idx

            if idx_w1 > -1 and idx_w2 > -1:
                dist = min(dist, abs(idx_w1 - idx_w2))

        return dist


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.shortest_distance(
            ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
        )
    )
    print(
        solution.shortest_distance(
            ["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"
        )
    )
