# MEDIUM
#
# You are given an integer array nums. In one move, you can choose one element of nums and change it by any value.
# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
#
# Example 1:
#
# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
#
# Example 2:
#
# Input: nums = [1,5,0,10,14]
# Output: 1
# Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
# The difference between the maximum and minimum is 1-0 = 1.
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        minimums = []
        nums.sort()

        # 1 - dec 3 max elements to min
        minimums.append(nums[-4] - nums[0])
        # 2 - inc 3 min elements to max
        minimums.append(nums[-1] - nums[3])
        # 3 - dec 2 max elements, inc min element
        minimums.append(nums[-3] - nums[1])
        # 4 - inc 2 min elements, dec max element
        minimums.append(nums[-2] - nums[2])

        return min(minimums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDifference([5, 3, 2, 4]))  # 0
    print(solution.minDifference([1, 5, 0, 10, 14]))  # 1
    print(solution.minDifference([6, 6, 0, 1, 1, 4, 6]))  # 2
    print(solution.minDifference([1, 5, 6, 14, 15, 13]))  # 2
    print(solution.minDifference([82, 81, 95, 75, 20]))  # 1
