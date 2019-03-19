from typing import List


class SquareArrayAnalyzer:
    @staticmethod
    def compare(array1: List[int], array2: List[int]) -> bool:
        for number in array1:
            if not SquareArrayAnalyzer.is_square(number, array2):
                return False
        return True

    @staticmethod
    def is_square(num1: int, array2: List[int]) -> bool:
        for number in array2:
            if number == num1 or number == num1*num1:
                return True
        return False


class TicTacToe:
    def __init__(self, board: List[List[str]]):
        self.board: List[List[str]] = board

    def get_column(self, index: int) -> List[str]:
        return [self.board[0][index]] + [self.board[1][index]] + [self.board[2][index]]

    def get_row(self, index: int) -> List[str]:
        return self.board[index]

    def column_win(self, index: int) -> bool:
        return self.col_row_won(self.get_column(index))

    def row_win(self, index: int) -> bool:
        return self.col_row_won(self.get_row(index))

    def col_row_won(self, col_row: List[str]) -> bool:
        return col_row[0] == col_row[1] == col_row[2]

    def get_winner(self) -> str:
        for i in range(2):
            if self.column_win(i):
                return self.board[0][i]
            elif self.row_win(i):
                return self.board[i][0]
            else:
                return self.board[1][1]


class WaveGenerator:
    @staticmethod
    def wave(input_string: str) -> List[str]:
        string: str = input_string.lower()
        strings: List[str] = []
        for i in range(len(string)):
            if string[i].isalpha():
                strings.append(string[:i] + string[i].upper() + string[i+1:])
        return strings

