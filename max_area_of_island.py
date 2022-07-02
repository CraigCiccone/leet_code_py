# MEDIUM
#
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is
# the number of cells with a value 1 in the island. Return the maximum area of an island in grid. If there is no island,
# return 0.
#
# Example 1:
#
# Input: grid = [
# [0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
#
# Example 2:
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from typing import List, Set


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col, grid, visited))

        return max_area


def bfs(row: int, col: int, grid: List[List[int]], visited: Set) -> int:
    rows = len(grid)
    cols = len(grid[0])
    q = [(row, col)]
    visited.add((row, col))
    area = 1

    while q:
        row, col = q.pop()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dir_row, dir_col in dirs:
            cur_row = row + dir_row
            cur_col = col + dir_col

            if (
                0 <= cur_row < rows
                and 0 <= cur_col < cols
                and grid[cur_row][cur_col] == 1
                and (cur_row, cur_col) not in visited
            ):
                q.append((cur_row, cur_col))
                visited.add((cur_row, cur_col))
                area += 1

    return area


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
    )
    print(solution.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
