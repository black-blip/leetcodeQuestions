def isValidSudoku(board) -> bool:

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sub = [set() for _ in range(9)]

    for r in range(9):

        for c in range(9):

            if board[r][c]==".":
                continue
            
            if board[r][c] in rows[r]:
                return False
            
            rows[r].add(board[r][c])
            if board[r][c] in cols[c]:
                return False

            cols[c].add(board[r][c])
            
            idx = (r//3)*3+(c//3)

            if board[r][c] in sub[idx]:
                return False
            
            sub[idx].add(board[r][c])
            
    
    return True





board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))