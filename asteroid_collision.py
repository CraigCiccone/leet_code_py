# MEDIUM
#
# We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value
# represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each
# asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet,
# the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same
# direction will never meet.
#
# Example 1:
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#
# Example 2:
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
#
# Example 3:
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
# Constraints:
#
# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:

            if (
                not stack
                or stack[-1] < 0 < ast  # opposite dir - won't collide
                or (stack[-1] > 0 and ast > 0)  # both move right - won't collide
                or (stack[-1] < 0 and ast < 0)  # both move left - won't collide
            ):
                stack.append(ast)
                continue

            while stack:
                stack_val = stack.pop()

                if (stack_val > 0 and ast > 0) or (stack_val < 0 and ast < 0):
                    stack.append(stack_val)
                    stack.append(ast)
                    break

                if stack_val > abs(ast):
                    stack.append(stack_val)
                    break

                if stack_val == abs(ast):
                    break

                if not stack:
                    stack.append(ast)
                    break

        return stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.asteroidCollision([-2, -2, 1, -1]))
    print(solution.asteroidCollision([-2, -2, 1, -2]))
    print(solution.asteroidCollision([-2, -1, 1, 2]))
    print(solution.asteroidCollision([5, 10, -5]))
    print(solution.asteroidCollision([8, -8]))
    print(solution.asteroidCollision([10, 2, -5]))
    print(solution.asteroidCollision([1, 2, 3, 5, 10, -15]))
