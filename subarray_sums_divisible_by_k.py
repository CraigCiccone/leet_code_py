# MEDIUM
#
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# Example 2:
#
# Input: nums = [5], k = 9
# Output: 0
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        prefixes = {}

        for idx in range(len(nums)):
            cur_sum += nums[idx]

            if cur_sum % k == 0:
                count += 1

            if cur_sum % k in prefixes:
                count += prefixes[cur_sum % k]

            prefixes[cur_sum % k] = prefixes.get(cur_sum % k, 0) + 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
    print(solution.subarraysDivByK([5], 9))
