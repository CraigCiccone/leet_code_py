# MEDIUM
#
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target. Return the sum of the three integers. You may assume that each input would have exactly one
# solution.
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
#
# Input: nums = [0,0,0], target = 1
# Output: 0
#
# Constraints:
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()

        for idx in range(len(nums) - 2):
            low_idx = idx + 1
            high_idx = len(nums) - 1

            while low_idx < high_idx:
                cur_sum = nums[idx] + nums[low_idx] + nums[high_idx]

                if cur_sum > target:
                    high_idx -= 1
                else:
                    low_idx += 1

                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum

        return closest_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest([0, 0, 0], 1))
