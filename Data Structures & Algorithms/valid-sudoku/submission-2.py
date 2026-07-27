class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        square = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                num = int(board[i][j])
                bit = 1 << num

                if rows[i] & bit:
                    return False
                if cols[j] & bit:
                    return False
                if square[i // 3][j // 3] & bit:
                    return False

                rows[i] |= bit
                cols[j] |= bit
                square[i // 3][j // 3] |= bit

        return True