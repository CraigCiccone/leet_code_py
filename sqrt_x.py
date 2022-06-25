# EASY
#
# Given a non-negative integer x, compute and return the square root of x. Since the return type is an integer, the
# decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#
# Example 1:
#
# Input: x = 4
# Output: 2
#
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
# Constraints:
#
# 0 <= x <= 2^31 - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 0
        high = x

        while low <= high:
            mid = low + (high - low) // 2
            mid_squared = mid * mid

            if mid_squared > x:
                high = mid - 1
            elif mid_squared < x:
                low = mid + 1
            else:
                return mid

        return low - 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
    print(solution.mySqrt(0))
    print(solution.mySqrt(1))
    print(solution.mySqrt(2))
    print(solution.mySqrt(3))
