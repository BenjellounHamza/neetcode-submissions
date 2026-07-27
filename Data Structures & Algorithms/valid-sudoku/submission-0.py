class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    print(1, i)
                    return False
                if board[i][j] != '.':
                    seen.add(board[i][j])
        

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    print(2, i)
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])
        
        for a in range(3):
            for b in range(3):
                seen = set()
                for i in range(a*3, (a + 1)*3):
                    for j in range(b * 3, (b + 1) * 3):
                        if board[i][j] in seen:
                            print(3, a, b)
                            return False
                        if board[i][j] != '.':
                            seen.add(board[i][j])
        
        return True


                
        