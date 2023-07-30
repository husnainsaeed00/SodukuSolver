class Solution:
    def isValid(self, board, row, col, num):
        # Check if the number is not present in the current row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check if the number is not present in the current column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check if the number is not present in the current 3x3 sub-box
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True

    def findEmptyCell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def solveSudoku(self, board):
        emptyCell = self.findEmptyCell(board)
        if not emptyCell:
            return True

        row, col = emptyCell
        for num in range(1, 10):
            if self.isValid(board, row, col, str(num)):
                board[row][col] = str(num)
                if self.solveSudoku(board):
                    return True
                board[row][col] = '.'  # Backtrack and try a different number

        return False

# Example puzzle
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = Solution()
solution.solveSudoku(board)

for row in board:
    print(row)
