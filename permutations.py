# MEDIUM
#
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from itertools import permutations
from typing import List


class Solution:
    def py_native_permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        perms = self.permute(nums[1:])

        results = []
        for perm in perms:
            for i in range(len(perm) + 1):
                results.append(perm[:i] + [nums[0]] + perm[i:])

        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([0, 1]))
    print(solution.permute([1]))
    print(solution.permute([1, 2, 3, 4]))
