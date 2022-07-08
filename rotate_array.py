# MEDIUM
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[len(nums) - k :] + nums[: len(nums) - k]


if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(solution.rotate([-1, -100, 3, 99], 2))
    print(solution.rotate([1], 0))
    print(solution.rotate([-1], 2))
    print(solution.rotate([1, 2], 3))
    print(solution.rotate([1, 2], 2))
