from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        low_idx = 0
        high_idx = len(height) - 1
        max_area = 0

        while low_idx < high_idx:
            cur_area = min(height[low_idx], height[high_idx]) * (high_idx - low_idx)
            max_area = max(max_area, cur_area)

            if height[low_idx] >= height[high_idx]:
                high_idx -= 1
            elif height[low_idx] < height[high_idx]:
                low_idx += 1

        return max_area


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea([1, 1]))
