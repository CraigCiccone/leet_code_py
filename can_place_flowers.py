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
