class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        square = [[0] * 3 for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    int_value = int(board[i][j])
                    value_row = rows[i]
                    if value_row & (1<<int_value):
                        # value exists:
                        return False
                    value_col = cols[j]
                    if value_col & (1<<int_value):
                        # value exists:
                        return False
                    value_square = square[(i // 3)][(j // 3)]
                    if value_square & (1<<int_value):
                        # value exists:
                        return False
                    # update values
                    rows[i] = rows[i] | (1<<int_value)
                    cols[j] = cols[j] | (1<<int_value)
                    square[i // 3][j // 3] = square[i // 3][j // 3] | (1<<int_value)
        return True