from unittest import TestCase

from src.main.arrays import SquareArrayAnalyzer, TicTacToe, WaveGenerator


class CompareAssortedArrays(TestCase):

    def test1(self):
        array = [1, 2, 3]
        array_squared = [1, 4, 9]
        self.util(array, array_squared)

    def test2(self):
        array = [3, 4, 5]
        array_squared = [9, 16, 25]
        self.util(array, array_squared)

    def test3(self):
        array = [121, 144, 19, 161, 19, 144, 19, 11]
        array_squared = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.util(array, array_squared)

    def util(self, array1, array2):
        self.assertTrue(SquareArrayAnalyzer.compare(array1, array2))


class CompareSortedArrays(TestCase):
    def test0(self):
        array = [1]
        array_squared = [1]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))

    def test1(self):
        array = [2]
        array_squared = [4]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))

    def test2(self):
        array = [3]
        array_squared = [9]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))

    def test3(self):
        array = [1, 2, 3]
        array_squared = [1, 4, 9]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))

    def test4(self):
        array = [3, 4, 5, ]
        array_squared = [9, 16, 25]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))

    def test5(self):
        array = [121, 144, 19, 161, 19, 144, 19, 11]
        array_squared = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertTrue(SquareArrayAnalyzer.compare(array, array_squared))


class GetColumnTest(TestCase):
    def test1(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 0
        expected = ["X", "O", "O"]
        actual = tic_tac_toe.get_column(column_index)
        self.assertEqual(expected, actual)

    def test2(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 1
        expected = ["O", "X", "X"]
        actual = tic_tac_toe.get_column(column_index)
        self.assertEqual(expected, actual)

    def test3(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "X"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 2
        expected = ["X", "X", "O"]
        actual = tic_tac_toe.get_column(column_index)
        self.assertEqual(expected, actual)


class GetRowTest(TestCase):
    def test1(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        index_fetch = 0
        expected = row1
        actual = tic_tac_toe.get_row(index_fetch)
        self.assertEqual(expected, actual)

    def test2(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        index_fetch = 1
        expected = row2
        actual = tic_tac_toe.get_row(index_fetch)
        self.assertEqual(expected, actual)

    def test3(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        index_fetch = 2
        expected = row3
        actual = tic_tac_toe.get_row(index_fetch)
        self.assertEqual(expected, actual)


class GetWinner(TestCase):
    def testDiagonal1(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "X"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "X"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)

    def testDiagonal2(self):
        row1 = ["O", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["X", "O", "X"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "X"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)

    def testRow1(self):
        row1 = ["O", "O", "O"]
        row2 = ["X", "X", "O"]
        row3 = ["O", "X", "X"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "O"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)

    def testRow2(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "O", "O"]
        row3 = ["X", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "O"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)

    def testColumn1(self):
        row1 = ["X", "O", "X"]
        row2 = ["X", "O", "O"]
        row3 = ["X", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "X"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)

    def testColumn2(self):
        row1 = ["O", "X", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["X", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        expected = "X"
        actual = tic_tac_toe.get_winner()
        self.assertEqual(expected, actual)


class IsColumnHomogeneousTest(TestCase):
    def test1(self):
        row1 = ["O", "X", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 0
        self.assertTrue(tic_tac_toe.column_win(column_index))

    def test2(self):
        row1 = ["O", "X", "X"]
        row2 = ["X", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 0
        self.assertFalse(tic_tac_toe.column_win(column_index))

    def test3(self):
        row1 = ["O", "X", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 1
        self.assertTrue(tic_tac_toe.column_win(column_index))

    def test4(self):
        row1 = ["O", "X", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        column_index = 2
        self.assertFalse(tic_tac_toe.column_win(column_index))


class IsRowHomogeneousTest(TestCase):
    def test1(self):
        row1 = ["X", "X", "X"]
        row2 = ["O", "O", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        row_index = 0
        self.assertTrue(tic_tac_toe.row_win(row_index))

    def test2(self):
        row1 = ["X", "X", "X"]
        row2 = ["O", "O", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        row_index = 1
        self.assertTrue(tic_tac_toe.row_win(row_index))

    def test3(self):
        row1 = ["X", "X", "X"]
        row2 = ["O", "O", "O"]
        row3 = ["O", "X", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        row_index = 2
        self.assertFalse(tic_tac_toe.row_win(row_index))

    def test4(self):
        row1 = ["X", "O", "X"]
        row2 = ["O", "X", "O"]
        row3 = ["O", "O", "O"]
        board = [row1, row2, row3]
        tic_tac_toe = TicTacToe(board)
        row_index = 2
        self.assertTrue(tic_tac_toe.row_win(row_index))


class WaveTest(TestCase):
    def test0(self):
        string_input = "AAAAAAA"
        expected = [
            "Aaaaaaa",
            "aAaaaaa",
            "aaAaaaa",
            "aaaAaaa",
            "aaaaAaa",
            "aaaaaAa",
            "aaaaaaA"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test1(self):
        string_input = "aaaaaaa"
        expected = [
            "Aaaaaaa",
            "aAaaaaa",
            "aaAaaaa",
            "aaaAaaa",
            "aaaaAaa",
            "aaaaaAa",
            "aaaaaaA"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test2(self):
        string_input = "A_A_A"
        expected = [
            "A_a_a",
            "a_A_a",
            "a_a_A"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test4(self):
        string_input = "Radioactivity"
        expected = [
            "Radioactivity",
            "rAdioactivity",
            "raDioactivity",
            "radIoactivity",
            "radiOactivity",
            "radioActivity",
            "radioaCtivity",
            "radioacTivity",
            "radioactIvity",
            "radioactiVity",
            "radioactivIty",
            "radioactiviTy",
            "radioactivitY"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test5(self):
        string_input = "the quick brown fox"
        expected = [
            "The quick brown fox",
            "tHe quick brown fox",
            "thE quick brown fox",
            "the Quick brown fox",
            "the qUick brown fox",
            "the quIck brown fox",
            "the quiCk brown fox",
            "the quicK brown fox",
            "the quick Brown fox",
            "the quick bRown fox",
            "the quick brOwn fox",
            "the quick broWn fox",
            "the quick browN fox",
            "the quick brown Fox",
            "the quick brown fOx",
            "the quick brown foX"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test6(self):
        string_input = "the quick brown f0x!"
        expected = [
            "The quick brown f0x!",
            "tHe quick brown f0x!",
            "thE quick brown f0x!",
            "the Quick brown f0x!",
            "the qUick brown f0x!",
            "the quIck brown f0x!",
            "the quiCk brown f0x!",
            "the quicK brown f0x!",
            "the quick Brown f0x!",
            "the quick bRown f0x!",
            "the quick brOwn f0x!",
            "the quick broWn f0x!",
            "the quick browN f0x!",
            "the quick brown F0x!",
            "the quick brown f0X!"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test7(self):
        string_input = "hello"
        expected = [
            "Hello",
            "hEllo",
            "heLlo",
            "helLo",
            "hellO"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test8(self):
        string_input = "two words"
        expected = [
            "Two words",
            "tWo words",
            "twO words",
            "two Words",
            "two wOrds",
            "two woRds",
            "two worDs",
            "two wordS"]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test9(self):
        string_input = " gap "
        expected = [
            " Gap ",
            " gAp ",
            " gaP "]
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)

    def test10(self):
        string_input = ""
        expected = []
        actual = WaveGenerator.wave(string_input)
        self.assertEqual(expected, actual)
