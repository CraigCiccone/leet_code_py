# EASY
#
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be
# planted in adjacent plots. Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means
# not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the
# no-adjacent-flowers rule.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0

        if n == 0:
            return True

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False

        for idx in range(len(flowerbed)):
            if idx == 0 and flowerbed[idx] == 0 and flowerbed[idx + 1] == 0:
                flowerbed[idx] = 1
                placed += 1
            elif (
                idx == len(flowerbed) - 1
                and flowerbed[idx] == 0
                and flowerbed[idx - 1] == 0
            ):
                flowerbed[idx] = 1
                placed += 1
            else:
                if (
                    flowerbed[idx - 1] == 0
                    and flowerbed[idx] == 0
                    and flowerbed[idx + 1] == 0
                ):
                    flowerbed[idx] = 1
                    placed += 1

        return placed >= n


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(solution.canPlaceFlowers([0, 0, 1, 1, 0, 0], 2))
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0, 1, 0, 0], 3))
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0, 0], 3))
    print(solution.canPlaceFlowers([0, 0, 0, 0], 2))
    print(solution.canPlaceFlowers([0, 0, 0, 0], 3))
    print(solution.canPlaceFlowers([1, 0, 0, 0, 0], 3))
    print(solution.canPlaceFlowers([0], 1))
    print(solution.canPlaceFlowers([1], 0))
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 0))
    print(solution.canPlaceFlowers([1], 1))
