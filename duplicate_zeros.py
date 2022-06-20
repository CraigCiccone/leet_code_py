# EASY
#
# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right. Note that elements beyond the
# length of the original array are not written. Do the above modifications to
# the input array in place and do not return anything.
#
# Example 1:
#
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
#
# Example 2:
#
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
# Constraints:
#
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 9

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        count = 0
        size = len(arr)

        for _ in range(size):
            if count >= len(arr) - 1:
                break

            if arr[count] == 0:
                arr.insert(count + 1, 0)
                arr.pop()
                count += 2
            else:
                count += 1


if __name__ == "__main__":
    solution = Solution()
    solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
    solution.duplicateZeros([1, 2, 3])
    solution.duplicateZeros([0, 4, 1, 0, 0, 8, 0, 0, 3])
