# EASY
#
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
#
# 1 <= n <= 45

from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        start_1 = climb(1, n)
        start_2 = climb(2, n)
        return start_1 + start_2


@lru_cache()
def climb(cur_steps: int, n: int) -> int:
    if cur_steps > n:
        return 0
    elif cur_steps == n:
        return 1
    else:
        return climb(cur_steps + 1, n) + climb(cur_steps + 2, n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
