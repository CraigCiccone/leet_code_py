# MEDIUM
#
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col, grid, visited)
                    islands += 1

        return islands


def bfs(row: int, col: int, grid: List[List[str]], visited: Set):
    rows = len(grid)
    cols = len(grid[0])
    q = [(row, col)]
    visited.add((row, col))

    while q:
        row, col = q.pop()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dir_row, dir_col in dirs:
            cur_row = row + dir_row
            cur_col = col + dir_col

            if (
                0 <= cur_row < rows
                and 0 <= cur_col < cols
                and grid[cur_row][cur_col] == "1"
                and (cur_row, cur_col) not in visited
            ):
                q.append((cur_row, cur_col))
                visited.add((cur_row, cur_col))


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )
    print(
        solution.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    print(
        solution.numIslands(
            [
                ["1", "1", "1", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    print(solution.numIslands([["1"]]))
