import re
from sqlite3 import Row
from turtle import update
import board
from tkinter import *
from tkinter import ttk


CELL_WIDTH = 10
CELL_HEIGHT = CELL_WIDTH
BLOCK_SPACE = 3

current_cell_coords = None

class SudokuDisplayCell:
    def __init__(self, root, cell_row, cell_column, digit):
        self.cell_row = cell_row
        self.cell_column = cell_column
        self.display = ttk.Button(root, text=digit, command=self.set_global_coords, style = "Cell.TButton")
        self.display.grid(row=cell_row+1, column=cell_column+1)
        if cell_row % 3 == 0 and cell_row != 0:
            self.display.grid(pady=(10,0))
        if cell_column % 3 == 0 and cell_column != 0:
            self.display.grid(padx=(10,0))

    def set_global_coords(self):
        global current_cell_coords
        current_cell_coords = (self.cell_row, self.cell_column)
        #print(self.cell_row, self.cell_column)
        print(current_cell_coords)


    def set_digit(self, digit):
        self.display["text"] = digit

    def set_fg(self, colour):
        self.display["foreground"] = colour
        

class SudokuDisplay:
    def __init__(self, root) -> None:
    
        self.error_label = ttk.Label(root, text="Testing")
        self.error_label.grid(row=11, column=4, columnspan=3)
        

        self.internal_sudoku = board.Board.generate_sudoku()
        self.solve_button = ttk.Button(root, command=self.solve, text="Solve")
        self.solve_button.grid( row=11, column=2)

        self.empty_button = ttk.Button(root, command=self.empty, text="Empty")
        self.empty_button.grid(row=11, column=3)
        style = ttk.Style(root)
        style.configure('Cell.TButton', height=CELL_HEIGHT, anchor=CENTER,  relief='groove', width=CELL_WIDTH)
        style.configure('MarkedCell.TButton', height=CELL_HEIGHT, anchor=CENTER,  relief='groove', width=CELL_WIDTH)
        sudoku_board = ttk.Frame(root).grid(column=1, row=1)
   
        self.rows = list()

        for i in range(board.COLUMN_AND_ROW_NB):
            sudoku_row = []
            for j in range(board.COLUMN_AND_ROW_NB):
                
                    digit = self.internal_sudoku.index(i,j)        
                    cell = SudokuDisplayCell(root, i, j, digit)
                    sudoku_row.append(cell)
            self.rows.append(sudoku_row)

    def empty(self):
        self.internal_sudoku = board.Board()
        self.update_grid()

    def solve(self):
        solution = self.internal_sudoku.solve()
        if solution == None:
            self.error_label["text"] = "No Solution Found"
        else:
            self.internal_sudoku = solution
            self.update_grid()

    def update_grid(self):
        for i in range(board.COLUMN_AND_ROW_NB):
            for j in range(board.COLUMN_AND_ROW_NB):
                digit = self.internal_sudoku.index(i,j)
                if digit == None:
                    self.rows[i][j].set_digit("")
                elif self.internal_sudoku.index_user_marked(i,j):
                    self.rows[i][j].set_digit("[%s]"%digit)
                else:
                    self.rows[i][j].set_digit(digit)

    def regenerate(self):
        self.internal_sudoku = board.Board.generate_sudoku()
        self.update_grid()

    def try_input(self, digit):
        if current_cell_coords == None :
            self.error_label["text"] = "No Cell Has been Selected"
        else:
            print("Attempting digit")
            self.error_label["text"] = self.internal_sudoku.try_input(current_cell_coords[0], current_cell_coords[1], digit)
            self.update_grid()



"""
def check_num(newval):
    return re.search('?[1-9]', newval) is not None
"""



    




"""
check_num_wrapper = (root.register(check_num), '%P')

num = StringVar()
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid(column=0, row=0, sticky='we')

"""