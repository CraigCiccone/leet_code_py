# MEDIUM
#
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is
# either an integer, or a list -- whose elements may also be integers or other lists. Different from the previous
# question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e.,
# the leaf level integers have weight 1, and the root level integers have the largest weight.
#
# Example 1:
#
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 8
# Explanation:
# four 1's at depth 1, one 2 at depth 2
#
# Example 2:
#
# Input: nestedList = [1,[4,[6]]]
# Output: 17
# Explanation:
# one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17


class Solution:
    def depthSumInverse(self, nestedList):
        cur_tot = tot = 0
        nested_list = nestedList

        while nested_list:
            nxt = []

            for entry in nested_list:
                if isinstance(entry, int):
                    cur_tot += entry
                else:
                    for e in entry:
                        nxt.append(e)

            tot += cur_tot
            nested_list = nxt

        return tot


if __name__ == "__main__":
    solution = Solution()
    print(solution.depthSumInverse([[1, 1], 2, [1, 1]]))
    print(solution.depthSumInverse([1, [4, [6]]]))
