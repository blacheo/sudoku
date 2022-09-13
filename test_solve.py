import unittest
import board
MAX_NUM = board.MAX_NUM

example_board =  [ 
                [9, 6, 8, 1, 3, 5, 2, 4, 7],
                [1, 3, 7, 8, 4, 2, 9, 5, 6],
                [4, 2, 5, 9, 6, 7, 3, 8, 1],
                [7, 8, 2, 6, 1, 3, 4, 9, 5],
                [3, 1, 4, 5, 9, 8, 7, 6, 2],
                [5, 9, 6, 2, 7, 4, 8, 1, 3],
                [8, 7, 9, 3, 5, 1, 6, 2, 4],
                [6, 4, 1, 7, 2, 9, 5, 3, 8],
                [2, 5, 3, 4, 8, 6, 1, 7, 9] 
                 ]

example_unsolved_board = [
        [ 0, 6, 9, 8, 0, 0, 0, 0, 0 ],
        [ 3, 0, 4, 7, 0, 6, 5, 0, 0 ],
        [ 2, 0, 0, 5, 9, 0, 6, 0, 0 ],
        [ 0, 2, 0, 0, 0, 0, 0, 1, 0 ],
        [ 9, 0, 0, 1, 0, 7, 0, 0, 8 ],
        [ 0, 3, 0, 0, 0, 0, 0, 4, 0 ],
        [ 0, 0, 2, 0, 5, 4, 0, 0, 7 ],
        [ 0, 0, 3, 2, 0, 1, 4, 0, 5 ],
        [ 0, 0, 0, 0, 0, 9, 2, 6, 0 ]
        ]

class TestSolve(unittest.TestCase):

    def test_grid_size(self):
        test_board = board.Board(example_board)
        self.assertEqual(MAX_NUM, len(test_board.the_board))

    def test_new_constr(self):
        test_board = board.Board(example_board)
        for i in range(MAX_NUM):
            for j in range(MAX_NUM):
                for k in range(1, MAX_NUM + 1):
                    if test_board.cross_hatch_check(i, j, k):
                        self.assertEqual(True, False)
        self.assertEqual(True,True)

    def test_find_empty(self):
        test_board = board.Board(example_board)
        test_board.remove(0,0)
        self.assertEqual((0, 0), test_board.find_empty_loc())


    def test_simple(self):
        test_board = board.Board(example_board)
        test_board.remove(0,0)
        test_board = test_board.solve()
        self.assertEqual(test_board.index(0,0), 9)

    def test_backtrack(self):
        test_board = board.Board(example_unsolved_board)
        test_board = test_board.solve()
        self.assertEqual(test_board.index(0,0), 5)

    def test_simple_3_empty(self):
        test_board = board.Board(example_board)
        test_board.remove(0,0)
        test_board.remove(0,1)
        test_board.remove(0,3)
        test_board = test_board.solve()
        self.assertEqual(test_board.index(0,0), 9)
        self.assertEqual(test_board.index(0,1), 6)
        self.assertEqual(test_board.index(0,3), 1)
       
