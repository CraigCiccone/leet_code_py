# MEDIUM
#
# Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be
# constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once.
#
# Example 1:
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
# Example 3:
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_sz = len(board)
        col_sz = len(board[0])
        word_chars = [char for char in word]

        chars = []
        for row in board:
            for col in row:
                chars.append(col)

        for char in word_chars:
            if char not in chars:
                return False

        for row_idx in range(row_sz):
            for col_idx in range(col_sz):
                q = [(row_idx, col_idx, [], {})]

                while q:
                    cur = q.pop()
                    row = cur[0]
                    col = cur[1]
                    cur_chars = cur[2].copy()
                    used = cur[3].copy()

                    if row == 0 and col == 0:
                        moves = [(row + 1, col), (row, col + 1)]
                    elif row == 0 and col == col_sz - 1:
                        moves = [(row + 1, col), (row, col - 1)]
                    elif row == row_sz - 1 and col == 0:
                        moves = [(row - 1, col), (row, col + 1)]
                    elif row == row_sz - 1 and col == col_sz - 1:
                        moves = [(row - 1, col), (row, col - 1)]
                    elif row == 0:
                        moves = [(row + 1, col), (row, col - 1), (row, col + 1)]
                    elif row == row_sz - 1:
                        moves = [(row - 1, col), (row, col - 1), (row, col + 1)]
                    elif col == 0:
                        moves = [(row + 1, col), (row - 1, col), (row, col + 1)]
                    elif col == col_sz - 1:
                        moves = [(row + 1, col), (row - 1, col), (row, col - 1)]
                    else:
                        moves = [
                            (row + 1, col),
                            (row - 1, col),
                            (row, col - 1),
                            (row, col + 1),
                        ]

                    desired = word_chars[len(cur_chars)]
                    if row < row_sz and col < col_sz and board[row][col] == desired:
                        cur_chars.append(desired)
                        used[(row, col)] = True
                        for move in moves:
                            if move not in used:
                                q.append((move[0], move[1], cur_chars, used))

                    if cur_chars == word_chars:
                        return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )  # true
    print(
        solution.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
    )  # true
    print(
        solution.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
    )  # false
    print(solution.exist([["a"]], "ab"))  # false
    print(solution.exist([["a", "b"], ["c", "d"]], "abcd"))  # false
    print(
        solution.exist(
            [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
            "ABCESEEEFS",
        )
    )  # true
    print(
        solution.exist(
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
            ],
            "AAAAAAAAAAAABAA",
        )
    )  # false
