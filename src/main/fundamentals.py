from typing import List


class VowelUtils:
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E',  'I', 'O', 'U']

    @classmethod
    def index_vowel1(cls, input_str: str) -> int or None:
        for letter in input_str:
            if letter in cls.vowels:
                return input_str.index(letter)
        return None

    @classmethod
    def has_vowels(cls, input_str: str) -> bool:
        return any(letter in input_str for letter in cls.vowels)

    @classmethod
    def is_vowel(cls, letter: str) -> bool:
        return letter in cls.vowels

    @classmethod
    def starts_with_vowel(cls, input_str: str) -> bool:
        return input_str[0] in cls.vowels


class StringUtils:
    @staticmethod
    def capitalize_n(input_str: str, index: int) -> str:
        if index == len(input_str):
            return input_str[:-1] + input_str[-1].upper()
        else:
            return input_str[:index] + input_str[index].upper() + input_str[index + 1:]

    @staticmethod
    def get_subs(input_str: str) -> List[str]:
        return sorted(list(set([input_str[i:j + 1] for i in range(len(input_str)) for j in range(i, len(input_str))])))

    @classmethod
    def number_subs(cls, input_str: str) -> int:
        return len(cls.get_subs(input_str))

    @staticmethod
    def char_at_index(string: str, character: str, index: int) -> bool:
        return string[index] == character


class PigLatinGenerator:
    @staticmethod
    def translate_word(word: str) -> str:
        index: int = VowelUtils.index_vowel1(word)
        starts_with_vowel: bool = VowelUtils.starts_with_vowel(word)
        if index is None:
            return word + "ay"
        elif starts_with_vowel:
            return word + "way"
        else:
            return word[index:] + word[:index] + "ay"

    def translate(self, input_str: str) -> str:
        words: List[str] = input_str.split(" ")
        final_str: str = ""
        for word in words:
            final_str += self.translate_word(word) + " "
        return final_str[:-1]
