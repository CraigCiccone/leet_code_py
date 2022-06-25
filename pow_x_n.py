# MEDIUM
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
# Constraints:
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= xn <= 10^4


class Solution:
    def my_pow_naive(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        magnitude = x
        for _ in range(1, abs(n)):
            magnitude *= x

        if n < 0:
            return 1 / magnitude
        else:
            return magnitude

    def myPow(self, x: float, n: int) -> float:
        magnitude = self.my_pow(x, abs(n))

        if n < 0:
            return 1 / magnitude
        else:
            return magnitude

    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if x == 0:
            return 0

        if n % 2 == 0:
            return self.my_pow(x * x, n // 2)
        else:
            return x * self.my_pow(x * x, n // 2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2, -2))
    print(solution.myPow(2, 0))
    print(solution.myPow(0, 4))
    print(solution.myPow(0.00001, 2147483647))
