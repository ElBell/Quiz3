from typing import List, Any
from unittest.test.testmock.testpatch import function


class ArrayUtility:
    def __init__(self, input_list: List[Any]):
        self.input_list: List[Any] = input_list

    def num_occurrences(self, check: Any) -> int:
        return self.input_list.count(check)

    def odd_occurring_value(self) -> Any or None:
        for string in self.input_list:
            if self.num_occurrences(string) % 2 != 0:
                return string
        return None

    def even_occurring_value(self) -> Any or None:
        for string in self.input_list:
            if self.num_occurrences(string) % 2 == 0:
                return string
        return None

    def filter(self, passed_function: function) -> List[Any]:
        return list(filter(passed_function, self.input_list))
