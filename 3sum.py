# MEDIUM
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if i != 0 and num1 == nums[i - 1]:
                continue

            l_idx = i + 1
            r_idx = len(nums) - 1

            while l_idx < r_idx:
                cur_sum = num1 + nums[l_idx] + nums[r_idx]

                if cur_sum > 0:
                    r_idx -= 1
                elif cur_sum < 0:
                    l_idx += 1
                else:
                    results.append([num1, nums[l_idx], nums[r_idx]])

                    l_idx += 1
                    while nums[l_idx] == nums[l_idx - 1] and l_idx < r_idx:
                        l_idx += 1

        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([]))
    print(solution.threeSum([0]))
