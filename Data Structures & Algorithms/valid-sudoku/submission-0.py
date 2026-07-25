class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for column in board:
            row_check = [ 0 for i in range(9) ]
            for row in column:
                if row != ".":
                    row = int(row)
                    row_check[row-1]+=1
                    if row_check[row-1] > 1:
                        return False

        for i in range(len(board[0])):
            row_check = [ 0 for i in range(9) ]
            for j in range(len(board)):
                pos = board[j][i]
                if  pos != ".":
                    pos = int(pos)
                    row_check[pos-1]+=1
                    if row_check[pos-1] > 1:
                        return False
        for i_b in range(0, 3):
            for j_b in range(3):
                row_check = [ 0 for i in range(9) ]
                for i in range(3):
                    for j in range(3):
                        pos = board[3*i_b+i][3*j_b+j]
                        if  pos != ".":
                            pos = int(pos)
                            row_check[pos-1]+=1
                            if row_check[pos-1] > 1:
                                return False
                
        return True