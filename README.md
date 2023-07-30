# SodukuSolver
To solve a Sudoku puzzle, we can use a backtracking algorithm. The idea is to try placing numbers from 1 to 9 in empty cells one by one and check if the placement is valid according to the Sudoku rules.

This is a Python program that solves a Sudoku puzzle by filling in the empty cells.

## Problem Statement
A Sudoku puzzle is a 9x9 grid that needs to be filled with digits from 1 to 9. The puzzle is divided into nine 3x3 sub-grids called sub-boxes. The objective is to fill the grid in such a way that each row, each column, and each sub-box contains all the digits from 1 to 9, without any repetition.

The input to the program is a partially filled Sudoku grid, where the empty cells are represented by the '.' character.

## Solution Approach
The program uses a backtracking algorithm to solve the Sudoku puzzle. It starts by finding an empty cell in the grid. If no empty cell is found, it means the puzzle is solved. Otherwise, it tries to fill the cell with a digit from 1 to 9 and checks if it is a valid move. If the move is valid, it proceeds to the next empty cell and repeats the process. If no valid move is found, it backtracks to the previous cell and tries a different digit.

The isValid method checks if a digit can be placed in a given cell without violating the rules of Sudoku. It checks the row, column, and sub-box to ensure that the digit is not already present.

## Example
Given the following Sudoku puzzle as input:

[    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
The program will solve the puzzle and produce the following output:

[    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
## How to Use
Clone the repository or download the sudoku_solver.py file.
Ensure you have Python installed on your system.
Update the board variable in the sudoku_solver.py file with your Sudoku puzzle. Use the '.' character for empty cells.
Run the Python script using the command python sudoku_solver.py.
The solved Sudoku grid will be displayed as output.
Feel free to use this program to solve your own Sudoku puzzles! Happy puzzling!
