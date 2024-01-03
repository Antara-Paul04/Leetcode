class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(row, column, num):
            for i in range(9):
                if board[row][i]==num or board[i][column]==num:
                    return False

                start_row, start_column= 3*(row//3), 3*(column//3)
                for i in range(3):
                    for j in range(3):
                        if board[start_row + i][start_column + j] == num:
                            return False
            return True
        
        def solve():
            for i in range (9):
                for j in range (9):
                    if board[i][j]==".":
                        for num in map(str, range(1, 10)):
                            if isValid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.' 
                        return False
            return True
        solve()
