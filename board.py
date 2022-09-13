import copy
import random

MAX_NUM = 9
MIN_CELLS = 20
MAX_CELLS = 50
BLOCK_SIZE = 3
COLUMN_AND_ROW_NB = 9

class Board:
    def __init__(self, grid=None):
        if grid == None:
            self.the_board = list()
            row = list()
            for i in range(COLUMN_AND_ROW_NB):
                row.append(Cell(None))

            for i in range(COLUMN_AND_ROW_NB):
                self.the_board.append(row.copy())
        else:
            self.the_board = list()
            for row in grid:
                new_row = list()
                for number in row:
                    if number == 0:
                        new_row.append(Cell(None))
                    else:
                        new_row.append(Cell(number))
                self.the_board.append(new_row)

    def remove(self, row, column):
        self.the_board[row][column] = Cell(None)

    def index(self, row, column):
        return self.the_board[row][column].number

    def index_user_marked(self, row, column):
        return self.the_board[row][column].user_marked

    # Produces true if successful
    def try_input(self, row, column, number):

        if number == None:
            pass
        elif  self.the_board[row][column].number != None and not self.the_board[row][column].user_marked:
            return "Cell already filled with non-user placed digit"
        elif self.used_in_column(column, number):
            return "Digit already used in column"
        elif self.used_in_row(row, number):
            return "Digit already used in row"
        elif self.used_in_block(row, column, number):
            return "Digit already used in block"
        
        
        self.the_board[row][column] = Cell(number, True)
        return "Digit placed succesfully"
        

    def print(self):
        for row in self.the_board:
            for i in range(len(row)):
                if i % 3 == 0 and i != 0:
                    print( ' ' , end='')
                row[i].print()
            print()

    @staticmethod
    def generate_sudoku():
        new_sudoku = Board()
        new_sudoku = new_sudoku.solve()
        coordinates = []
        for i in range(0, MAX_NUM):
            for j in range(0, MAX_NUM):
                coordinates.append((i,j))
        #Remove random value
        for i in range(random.randint(MIN_CELLS, MAX_CELLS)):
            row, column = random.choice(coordinates)
            coordinates.remove((row,column))
            new_sudoku.remove(row, column)
            #Do not remove value

        new_sudoku.shuffle_numbers()
        return new_sudoku

    def shuffle_numbers(self):
        
        shuffled_nums = list(range(1, MAX_NUM + 1))
        random.shuffle(shuffled_nums)

        for row in self.the_board:
            for cell in row:
                if cell.number != None:
                    cell.number = shuffled_nums[cell.number-1] 


    def solvable(self):
        pass
        
   

    def solve(self):
        if self.full():
            return self
        
        row, column = self.find_empty_loc()
        for i in range(1, MAX_NUM + 1):
            if self.cross_hatch_check(row, column, i):
                board_attempt = copy.deepcopy(self)
                board_attempt.the_board[row][column] = Cell(i)
                board_solution = board_attempt.solve()
                if board_solution != None:
                    return board_solution
            
    
    # Produces True if candidate is not used in row, column or block
    def cross_hatch_check(self, row, column, candidate):
        return not ( self.used_in_column(column, candidate) 
                or self.used_in_block(row, column, candidate) 
                or self.used_in_row(row, candidate) )

    def used_in_column(self, column, candidate):
        for i in range(COLUMN_AND_ROW_NB):
            if candidate == self.the_board[i][column].number:
                return True
        return False
    
    def used_in_row(self, row, candidate):
        for i in range(COLUMN_AND_ROW_NB):
           if candidate == self.the_board[row][i].number:
               return True
        return False

    def used_in_block(self, row, column, candidate):
        for i in range(MAX_NUM):
            if i // BLOCK_SIZE == row // BLOCK_SIZE:
                for j in range(MAX_NUM):
                    if j // BLOCK_SIZE == column // BLOCK_SIZE and self.the_board[i][j].number == candidate:
                        return True
        return False

    def find_empty_loc(self):
        for i in range(len(self.the_board)):
            for j in range(len(self.the_board)):
                if self.the_board[i][j].number == None:
                    return i, j


    def full(self):
        for row in self.the_board:
            for cell in row:
                if cell.number == None:
                    return False
        return True

    def completed(self):
        return False




            
class Cell:
    def __init__(self, number, user_marked=False):
        if number != 0:
            self.number = number
        else:
            self.number = None
        self.user_marked = user_marked

    def print(self):
        if self.number == None:
            print(0, end='')
        else:
            print(self.number, end='')
        

