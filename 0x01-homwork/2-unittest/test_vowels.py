import unittest
from test_vowels import count_vowels 


class CountVowelsTestCase(unittest.TestCase):
    def test_single_vowel(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("E"), 1)
        self.assertEqual(count_vowels("I"), 1)
        self.assertEqual(count_vowels("O"), 1)
        self.assertEqual(count_vowels("u"), 1)

    def test_multiple_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("OpenAI"), 3)
        self.assertEqual(count_vowels("Artificial Intelligence"), 8)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("Rhythm"), 0)
        self.assertEqual(count_vowels("Fly"), 0)
        self.assertEqual(count_vowels("XYZ"), 0)
        self.assertEqual(count_vowels("1234567890"), 0)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("hELLo"), 2)
        self.assertEqual(count_vowels("OpEnAI"), 3)
        self.assertEqual(count_vowels("ArTiFiCiAl InTeLlIgEnCe"), 8)


if __name__ == '__main__':
    unittest.main()
