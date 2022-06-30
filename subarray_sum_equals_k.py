# MEDIUM
#
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
# Constraints:
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = {}
        cur_sum = 0

        for idx in range(len(nums)):
            cur_sum += nums[idx]

            if cur_sum == k:
                count += 1

            diff = cur_sum - k
            if diff in prefix_sum:
                count += prefix_sum[diff]

            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
    print(solution.subarraySum([1, 2, 3], 3))
