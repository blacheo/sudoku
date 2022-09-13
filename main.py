
import sudoku_cell_display
from tkinter import ttk
from tkinter import *


def num_press(event):
    print('num press called')
    key = event.char
    if ('0' <= key and key <= '9'):
        sudoku_board.try_input(int(key))

root = Tk()
root.title("Sudoku")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



sudoku_board = sudoku_cell_display.SudokuDisplay(mainframe)

regenerate_button = ttk.Button(mainframe, text="Regenerate", command=sudoku_board.regenerate).grid(row=11, column=1)

"""
selected_cell = ttk.Label(mainframe)
selected_cell.grid(row=11, column=3)
"""

root.bind('<Key>', num_press)



root.mainloop()
