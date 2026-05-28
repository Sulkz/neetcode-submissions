class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for the row check
        for x in range(9):
            seen_x = set()
            for y in range(9):
                if board[x][y] == '.':
                    continue
                if board[x][y] not in seen_x:
                    seen_x.add(board[x][y])
                else:
                    return False
            
        
        #for column check
   
        for x in range(9):
            seen_y = set()
            for y in range(9):
                if board[y][x] == '.':
                    continue
                if board[y][x] not in seen_y:
                    seen_y.add(board[y][x])
                else:
                    return False
            
        

        #each cube

        for x in range(0,9,3):
            for y in range(0,9,3):
                seen_square = set()
                for x_col in range(x,x+3):
                    for y_col in range(y, y+3):
                        if board[x_col][y_col] == '.':
                            continue
                        if board[x_col][y_col] not in seen_square:
                            seen_square.add(board[x_col][y_col])
                        else:
                            return False
        return True
