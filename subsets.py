# MEDIUM
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
#
# Input: nums = [0]
# Output: [[],[0]]
#
# Constraints:
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        answer = []
        self.collect(nums, subset, answer)
        return answer

    def collect(
        self, nums: List[int], subset: List[int], answer: List[List[int]]
    ):
        if len(nums) == 0:
            answer.append(subset)
        else:
            self.collect(nums[1:], subset.copy(), answer)
            subset.append(nums[0])
            self.collect(nums[1:], subset.copy(), answer)


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
    print(solution.subsets([0]))
    print(solution.subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0]))
