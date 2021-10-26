import board
import unittest

class TestBoard(unittest.TestCase):
    
    def test_good_creation1(self):
        # * Tests the creation of a correct 3x3 board
        b1 = board.Board()
        b1.nb_rows = 3
        b1.board = [['X', None, None], [None, None, None], [None, 'O', None]]
        b2 = board.Board(3, [(0,0)], [(2,1)])
        self.assertEqual(b1,b2)
    
    def test_good_creation2(self):
        # * Tests the creation of a correct 4x4 board
        b1 = board.Board()
        b1.nb_rows = 4
        b1.board = [['X', None, None, None], [None, None, 'X', None], [None, 'O', None, None], [None, None, None, None]]
        b2 = board.Board(4, [(1,2), (0,0)], [(2,1)])
        self.assertEqual(b1,b2)

    def test_creation_error1(self):
        # * Tests the creation of an impossible board
        with self.assertRaises(Exception) as exc:
            board.Board(4, [(1,2), (0,0), (2,2)], [(2,1)])
        self.assertEqual(exc.exception.args, Exception("Invalid arguments for play_x or play_o").args)

    def test_creation_error2(self):
        # * Tests the creation of an impossible board
        with self.assertRaises(Exception) as exc:
            board.Board(4, [(1,2)], [(2,1), (0,0)])
        self.assertEqual(exc.exception.args, Exception("Invalid arguments for play_x or play_o").args)
    
    def test_creation_error3(self):
        # * Tests the creation of a board with an impossible move
        with self.assertRaises(Exception) as exc:
            board.Board(4, [(1,2), (4,2)], [(2,1), (0,0)])
        self.assertEqual(exc.exception.args, Exception("The move (4, 2) for player X is not possible.").args)

    def test_creation_error4(self):
        # * Tests the creation of a board with amove on an occupied square
        with self.assertRaises(Exception) as exc:
            board.Board(4, [(1,2), (2,1)], [(2,1), (0,0)])
        self.assertEqual(exc.exception.args, Exception("There's already something in the square").args)

    def test_winner1(self):
        # * Tests the detection of a win in a line
        b = board.Board(3,[(0,0), (0,1), (0,2)], [(1,0), (1,1)])
        res = b.getWinner()
        self.assertEqual(res, 'X')
        
    def test_winner2(self):
        # * Tests the detection of a win in a column
        b = board.Board(3, [(0,1), (0,2), (1,1)], [(0,0), (1,0), (2,0)])
        res = b.getWinner()
        self.assertEqual(res, 'O')

    def test_winner3(self):
        # * Tests the detection of a win in the left - right diagonal
        b = board.Board(3, [(0,0), (1,1), (2,2)], [(0,2), (1,2)])
        res = b.getWinner()
        self.assertEqual(res, 'X')

    def test_winner4(self):
        # * Tests the detection of a win in the right - left diagonal
        b = board.Board(3, [(0,2), (1,1), (2,0)], [(0,1), (1,2)])
        res = b.getWinner()
        self.assertEqual(res, 'X')

    def test_winner5(self):
        # * Tests the detection of a win of a completed board with no winners
        b = board.Board(3, [(1,1), (0,1), (1,0), (2,0), (2,2)], [(0,0), (0,2), (1,2), (2,1)])
        res = b.getWinner()
        self.assertEqual(res, None)

    def test_winner6(self):
        # * Tests the detection of a win of an uncompleted board with no winners
        b = board.Board(3, [(1,1), (0,1), (1,0)], [(0,0), (0,2), (1,2)])
        res = b.getWinner()
        self.assertEqual(res, None)

    def test_winner7(self):
        # * Tests the detection of a win in a 4x4 board
        b = board.Board(4, [(0,3), (1,2), (2,1), (3,0)], [(0,0), (0,2), (2,2)])
        res = b.getWinner()
        self.assertEqual(res, 'X')

    def test_getMoves(self):
        b = board.Board(4, [(0,3), (1,2), (2,1), (3,0)], [(0,0), (0,2), (2,2)])
        res = b.getMoves()
        self.assertEqual(res, ([(0,3), (1,2), (2,1), (3,0)], [(0,0), (0,2), (2,2)]))

    def test_isComplete1(self):
        b = board.Board(3, [(1,1), (0,1), (1,0), (2,0), (2,2)], [(0,0), (0,2), (1,2), (2,1)])
        res = b.isComplete()
        self.assertTrue(res)

    def test_isComplete2(self):
        b = board.Board(4, [(0,3), (1,2), (2,1), (3,0)], [(0,0), (0,2), (2,2)])
        res = b.isComplete()
        self.assertFalse(res)

    def test_representation(self):
        b = board.Board(3, [(0,0)], [(2,1)])
        res = str(b)
        expected = " X |   |   \n-----------\n   |   |   \n-----------\n   | O |   \n"
        self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()