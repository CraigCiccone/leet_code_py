# MEDIUM
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it. Return the number of possible non-empty
# sequences of letters you can make using the letters printed on those tiles.
#
# Example 1:
#
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
#
# Example 2:
#
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
#
# Input: tiles = "V"
# Output: 1
#
# Constraints:
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_list = [char for char in tiles]
        sequences = []

        for i in range(1, len(tile_list) + 1):
            cur_sequences = permutations(tile_list, i)
            sequences += list(cur_sequences)

        return len(set(sequences))


if __name__ == "__main__":
    solution = Solution()
    print(solution.numTilePossibilities("AAB"))
    print(solution.numTilePossibilities("AAABBC"))
    print(solution.numTilePossibilities("V"))
