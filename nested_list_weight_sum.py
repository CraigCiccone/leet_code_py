# EASY
#
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Input: [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1.
#
# Example 2:
# Input: [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.


class Solution:
    def depth_sum(self, nested_list) -> int:
        total = 0

        for val in nested_list:
            total += self.ds(val, 1)

        return total

    def ds(self, val, depth) -> int:
        cur_sum = 0

        if isinstance(val, int):
            cur_sum += val * depth
        else:
            for v in val:
                cur_sum += self.ds(v, depth + 1)

        return cur_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.depth_sum([[1, 1], 2, [1, 1]]))
    print(solution.depth_sum([1, [4, [6]]]))
