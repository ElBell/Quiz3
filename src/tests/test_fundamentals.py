from unittest import TestCase

from src.main.fundamentals import VowelUtils, StringUtils, PigLatinGenerator


class GetIndexOfFirstVowel(TestCase):
    def test1(self):
        test_input = "Psychological Warfare"
        expected = 5
        actual = VowelUtils.index_vowel1(test_input)
        self.assertEqual(expected, actual)

    def test2(self):
        test_input = "Psych!"
        expected = None
        actual = VowelUtils.index_vowel1(test_input)
        self.assertEqual(expected, actual)

    def test3(self):
        test_input = "Pterodactyl"
        expected = 2
        actual = VowelUtils.index_vowel1(test_input)
        self.assertEqual(expected, actual)


class HasVowels(TestCase):
    def test(self):
        self.test1()
        self.test2()
        self.test3()

    def test1(self):
        test_input = "qwrtypsdfghjklzxcvbnm"
        self.assertFalse(VowelUtils.has_vowels(test_input))

    def test2(self):
        test_input = "qwrtypsdfghjklzxcvbnma"
        self.assertTrue(VowelUtils.has_vowels(test_input))

    def test3(self):
        test_input = "qwrtypsdfghjklzxcvbnm_"
        self.assertFalse(VowelUtils.has_vowels(test_input))


class IsVowel(TestCase):
    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()

    def test1(self):
        self.assertTrue(VowelUtils.is_vowel('a'))

    def test2(self):
        self.assertTrue(VowelUtils.is_vowel('A'))

    def test3(self):
        self.assertTrue(VowelUtils.is_vowel('E'))

    def test4(self):
        self.assertTrue(VowelUtils.is_vowel('e'))

    def test5(self):
        self.assertTrue(VowelUtils.is_vowel('I'))

    def test6(self):
        self.assertTrue(VowelUtils.is_vowel('i'))


class StartsWithVowel(TestCase):
    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()

    def test1(self):
        test_input = "Jumping Jacks"
        self.assertFalse(VowelUtils.starts_with_vowel(test_input))

    def test2(self):
        test_input = "Hey there world"
        self.assertFalse(VowelUtils.starts_with_vowel(test_input))

    def test3(self):
        test_input = "Eggnog"
        self.assertTrue(VowelUtils.starts_with_vowel(test_input))

    def test4(self):
        test_input = "Optical"
        self.assertTrue(VowelUtils.starts_with_vowel(test_input))


class CapitalizeNthCharacter(TestCase):
    def test1(self):
        test_input = "hello"
        expected = "Hello"
        index = 0
        actual = StringUtils.capitalize_n(test_input, index)
        self.assertEqual(expected, actual)

    def test2(self):
        test_input = "hello"
        expected = "hEllo"
        index = 1
        actual = StringUtils.capitalize_n(test_input, index)
        self.assertEqual(expected, actual)

    def test3(self):
        test_input = "hello"
        expected = "heLlo"
        index = 2
        actual = StringUtils.capitalize_n(test_input, index)
        self.assertEqual(expected, actual)


class GetAllSubStrings(TestCase):
    def test1(self):
        test_input = "Hello"
        expected = [
            "H",
            "He",
            "Hel",
            "Hell",
            "Hello",
            "e",
            "el",
            "ell",
            "ello",
            "l",
            "ll",
            "llo",
            "lo",
            "o" ]
        actual = StringUtils.get_subs(test_input)
        self.assertEqual(expected, actual)

    def test5(self):
        test_input = "Janitor"
        expected = [
            "J",
            "Ja",
            "Jan",
            "Jani",
            "Janit",
            "Janito",
            "Janitor",
            "a",
            "an",
            "ani",
            "anit",
            "anito",
            "anitor",
            "i",
            "it",
            "ito",
            "itor",
            "n",
            "ni",
            "nit",
            "nito",
            "nitor",
            "o",
            "or",
            "r",
            "t",
            "to",
            "tor" ]
        actual = StringUtils.get_subs(test_input)
        actual = sorted(actual)
        self.assertEqual(expected, actual)


class GetNumberOfSubStrings(TestCase):
    def test1(self):
        test_input = "Hello"
        expected = 14
        actual = StringUtils.number_subs(test_input)
        self.assertEqual(expected, actual)

    def test2(self):
        test_input = "The Quick Brown"
        expected = 119
        actual = StringUtils.number_subs(test_input)
        self.assertEqual(expected, actual)


class IsCharacterAtIndex(TestCase):
    def test1(self):
        string = "Quickly"
        character = 'q'
        index = 0
        self.assertFalse(StringUtils.char_at_index(string, character, index))

    def test2(self):
        string = "Quickly"
        character = 'Q'
        index = 0
        self.assertTrue(StringUtils.char_at_index(string, character, index))

    def test3(self):
        string = "Quickly"
        character = 'y'
        index = 6
        self.assertTrue(StringUtils.char_at_index(string, character, index))

    def test4(self):
        string = "Quickly"
        character = 'Y'
        index = 6
        self.assertFalse(StringUtils.char_at_index(string, character, index))


class TranslateSentence(TestCase):
    def setUp(self):
        self.p = PigLatinGenerator()

    def testTheQuickBrownFoxJumpsOverTheLazyDog(self):
        test_input = "The Quick Brown Fox Jumps Over The Lazy Dog"
        expected = "eThay uickQay ownBray oxFay umpsJay Overway eThay azyLay ogDay"
        actual = self.p.translate(test_input)
        self.assertEqual(expected, actual)

    def test_thequickbrownfoxjumpsoverthelazydog(self):
        test_input = "The Quick Brown Fox Jumps Over The Lazy Dog".lower()
        expected = "eThay uickQay ownBray oxFay umpsJay Overway eThay azyLay ogDay".lower()
        actual = self.p.translate(test_input)
        self.assertEqual(expected, actual)

    def testTHEQUICKBROWNFOXJUMPSOVERTHELAZYDOG(self):
        test_input = "The Quick Brown Fox Jumps Over The Lazy Dog".upper()
        expected = "ETHay UICKQay OWNBRay OXFay UMPSJay OVERway ETHay AZYLay OGDay"
        actual = self.p.translate(test_input)
        self.assertEqual(expected, actual)


class TranslateSingleWordStartingWithConsonant(TestCase):
    def setUp(self):
        self.p = PigLatinGenerator()

    def testMap(self):
        self.assertEqual("apMay", self.p.translate("Map"))

    def testSpaghetti(self):
        self.assertEqual("aghettiSpay", self.p.translate("Spaghetti"))

    def testJava(self):
        self.assertEqual("avaJay", self.p.translate("Java"))

    def testPython(self):
        self.assertEqual("onPythay", self.p.translate("Python"))

    def testPsychosis(self):
        self.assertEqual("osisPsychay", self.p.translate("Psychosis"))

    def testPneumonia(self):
        self.assertEqual("eumoniaPnay", self.p.translate("Pneumonia"))

    def testRuby(self):
        self.assertEqual("ubyRay", self.p.translate("Ruby"))

    def testCCC(self):
        self.assertEqual("CCCCay", self.p.translate("CCCC"))


class TranslateSingleWordStartingWithVowel(TestCase):
    def setUp(self):
        self.p = PigLatinGenerator()

    def testegg(self):
        self.assertEqual("eggway", self.p.translate("egg"))

    def testapple(self):
        self.assertEqual("appleway", self.p.translate("apple"))

