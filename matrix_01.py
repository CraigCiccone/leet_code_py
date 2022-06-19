# MEDIUM
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
#
# Example 1:
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
#
# Example 2:
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        result = [[None for _ in range(cols)] for _ in range(rows)]
        q = []

        for row_idx in range(rows):
            for col_idx in range(cols):
                if mat[row_idx][col_idx] == 0:
                    q.append((row_idx, col_idx, 0))

        while q:
            row, col, dist = q.pop(0)
            if 0 <= row < rows and 0 <= col < cols and result[row][col] is None:
                result[row][col] = dist
                q.append((row - 1, col, dist + 1))
                q.append((row + 1, col, dist + 1))
                q.append((row, col - 1, dist + 1))
                q.append((row, col + 1, dist + 1))

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    print(
        solution.updateMatrix([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]])
    )
