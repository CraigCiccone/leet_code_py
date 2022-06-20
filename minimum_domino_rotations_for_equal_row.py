# MEDIUM
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino
# is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the ith domino, so that
# tops[i] and bottoms[i] swap values. Return the minimum number of rotations so that all the values in tops are
# the same, or all the values in bottoms are the same. If it cannot be done, return -1.
#
# Example 1:
#
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
# as indicated by the second figure.
#
# Example 2:
#
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
#
# Constraints:
#
# 2 <= tops.length <= 2 * 10^4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_rotations = float("inf")
        processed_top = {}
        processed_bot = {}

        if all(val == tops[0] for val in tops) or all(
            val == bottoms[0] for val in bottoms
        ):
            return 0

        got_all = True
        for val in tops:
            if val in processed_top:
                continue
            else:
                processed_top[val] = True

            cur_rotations = 0

            for idx in range(len(tops)):
                if not got_all:
                    break

                if tops[idx] == val:
                    continue
                elif bottoms[idx] == val:
                    cur_rotations += 1
                else:
                    got_all = False

            if got_all:
                min_rotations = min(cur_rotations, min_rotations)
            else:
                got_all = True

        got_all = True
        for val in bottoms:
            if val in processed_bot:
                continue
            else:
                processed_bot[val] = True

            cur_rotations = 0

            for idx in range(len(bottoms)):
                if not got_all:
                    break

                if bottoms[idx] == val:
                    continue
                elif tops[idx] == val:
                    cur_rotations += 1
                else:
                    got_all = False

            if got_all:
                min_rotations = min(cur_rotations, min_rotations)
            else:
                got_all = True

        if min_rotations == float("inf"):
            return -1
        else:
            return min_rotations


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
    print(solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
