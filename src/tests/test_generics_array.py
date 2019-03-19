from unittest import TestCase

from src.main.generics_array import ArrayUtility


class IntegerFilterTest(TestCase):
    def test1(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [6, 7, 8, 9, 10]
        utility = ArrayUtility(array)
        actual = utility.filter(lambda x: (x > 5))
        self.compare(expected, actual)

    def test2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = []
        utility = ArrayUtility(array)
        actual = utility.filter(lambda x: (x > 50))
        self.compare(expected, actual)

    def test3(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = array
        utility = ArrayUtility(array)
        actual = utility.filter(lambda x: (x < 50))
        self.compare(expected, actual)

    def test4(self):
        array = [10, 15, 20, 25, 55, 100, 150, 300, 900, 1000]
        expected = [10, 100, 1000]
        utility = ArrayUtility(array)
        actual = utility.filter(lambda x: str(x).startswith("10"))
        self.compare(expected, actual)

    def test5(self):
        array = [10, 15, 20, 25, 55, 100, 150, 300, 900, 1000]
        expected = [15, 25, 55]
        utility = ArrayUtility(array)
        actual = utility.filter(lambda x: str(x).endswith("5"))
        self.compare(expected, actual)

    def compare(self, expected, actual):
        self.assertEqual(expected, actual)


class IntegerFindEvenOccurringValue(TestCase):
    def test1(self):
        expected = 5
        array = [1, 2, 3, 4, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)

    def test2(self):
        expected = 18
        array = [1, 1, 1, 2, 2, 2, 2, 2, expected, 4, 4, 4, expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)

    def test3(self):
        expected = 30
        array = [1, expected, 4, expected, expected, 10, 10, 10, expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)


class IntegerFindOddOccurringValue(TestCase):
    def test1(self):
        expected = 5
        array = [1, 1, 2, 2, 3, 3, expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)

    def test2(self):
        expected = 18
        array = [1, 1, 6, 6, 9, 9, expected, expected, expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)

    def test3(self):
        expected = 30
        array = [11, 11, 11, 11, 20, 20, 27, 27, 27, 27, expected, expected, expected, expected, expected, expected,
                 expected]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)


class IntegerGetNumberOfOccurrences(TestCase):
    def test1(self):
        expected = 2
        value_evaluate = 5
        array = [1, 2, 3, 4, value_evaluate, value_evaluate]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(value_evaluate)
        self.assertEqual(expected, actual)

    def test2(self):
        expected = 4
        value_evaluate = 18
        array = [1, 1, 1, 2, 2, 2, 2, 2, value_evaluate, 4, 4, 4, value_evaluate, value_evaluate, value_evaluate]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(value_evaluate)
        self.assertEqual(expected, actual)

    def test3(self):
        expected = 6
        value_evaluate = 30
        array = [1, value_evaluate, 4, value_evaluate, value_evaluate, 10, 10, 10, value_evaluate, value_evaluate,
                 value_evaluate]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(value_evaluate)
        self.assertEqual(expected, actual)


class StringFilterTest(TestCase):
    def test1(self):
        expected = ["quick", "brown", "jumps", "over", "lazy"]
        string_input = "The quick brown fox jumps over the lazy dog".split(" ")
        utility = ArrayUtility(string_input)
        actual = utility.filter(lambda x: len(x) > 3)
        self.assertEqual(expected, actual)

    def test2(self):
        expected = ["The", "fox", "the", "dog"]
        string_input = "The quick brown fox jumps over the lazy dog".split(" ")
        utility = ArrayUtility(string_input)
        actual = utility.filter(lambda x: len(x) <= 3)
        self.assertEqual(expected, actual)

    def test3(self):
        expected = ["The", "over", "the"]
        string_input = "The quick brown fox jumps over the lazy dog".split(" ")
        utility = ArrayUtility(string_input)
        actual = utility.filter(lambda x: "e" in x)
        self.assertEqual(expected, actual)


class StringFindEvenOccurringValueTest(TestCase):
    def test1(self):
        expected = "Zip"
        array = [expected, expected, "Code", "Code", "Code", "Wilmington"]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)

    def test2(self):
        expected = "(-_-)"
        array = [expected, expected, "Code", "Code", "Code", expected, expected, "Wilmington"]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)

    def test3(self):
        expected = "Code"
        array = ["Zip", "Zip", "Zip", expected, expected, expected, "Wilmington", expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.even_occurring_value()
        self.assertEqual(expected, actual)


class StringFindOddOccurringValueTest(TestCase):
    def test1(self):
        expected = "Wilmington"
        array = [expected, expected, expected, "Code", "Code", "Code", "Code", "Zip", "Zip"]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)

    def test2(self):
        expected = "(-_-)"
        array = [expected, expected, expected, "Code", "Code", "Code", "Code", expected, expected, "Wilmington",
                 "Wilmington"]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)

    def test3(self):
        expected = "Code"
        array = ["Zip", "Zip", "Zip", "Zip", "Zip", "Zip", expected, expected, expected, expected, "Wilmington",
                 "Wilmington", expected, expected, expected]
        utility = ArrayUtility(array)
        actual = utility.odd_occurring_value()
        self.assertEqual(expected, actual)


class StringGetNumberOfOccurrencesTest(TestCase):
    def test1(self):
        expected = 3
        string_to_evaluate = "Wilmington"
        array = [string_to_evaluate, string_to_evaluate, string_to_evaluate, "Code", "Code", "Code", "Code", "Zip",
                 "Zip"]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(string_to_evaluate)
        self.assertEqual(expected, actual)

    def test2(self):
        expected = 5
        string_to_evaluate = "(-_-)"
        array = [string_to_evaluate, string_to_evaluate, string_to_evaluate, "Code", "Code", "Code", "Code",
                 string_to_evaluate, string_to_evaluate, "Wilmington", "Wilmington"]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(string_to_evaluate)
        self.assertEqual(expected, actual)

    def test3(self):
        expected = 7
        string_to_evaluate = "Code"
        array = ["Zip", "Zip", "Zip", "Zip", "Zip", "Zip", string_to_evaluate, string_to_evaluate, string_to_evaluate,
                 string_to_evaluate, "Wilmington", "Wilmington", string_to_evaluate, string_to_evaluate,
                 string_to_evaluate]
        utility = ArrayUtility(array)
        actual = utility.num_occurrences(string_to_evaluate)
        self.assertEqual(expected, actual)
