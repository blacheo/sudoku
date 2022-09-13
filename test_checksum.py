import unittest
import board

def put_three():
        test_board = board.Board()
        test_board.try_input(1,2,3)
        return test_board
     

class TestCheckSum(unittest.TestCase):

    def test_same_row(self):
        test_board = put_three()
        check_3 = test_board.cross_hatch_check(1,3,3)
        self.assertEqual(check_3, False)

    def test_same_row_s(self):
        test_board = put_three()
        check_3 = test_board.used_in_row(1,3)
        self.assertEqual(check_3, True)

    def test_same_column(self):
        test_board = put_three()
        check_3 = test_board.cross_hatch_check(2,2,3)
        self.assertEqual(check_3, False)
        
    def test_same_block(self):
        test_board = put_three()
        check_3 = test_board.cross_hatch_check(2,1,3)
        self.assertEqual(check_3, False)

    def test_diff_every(self):
        test_board = put_three()
        check_3 = test_board.cross_hatch_check(8,8,3)
        self.assertEqual(check_3, True)

    def test_same_every(self):
        test_board = put_three()
        check_3 = test_board.cross_hatch_check(1,2,3)
        self.assertEqual(check_3, False)

    def test_same_every_c(self):
        test_board = put_three()
        check_3 = test_board.used_in_column(2,3)
        self.assertEqual(check_3, True)

        


if __name__ == '__main__':
    unittest.main()
