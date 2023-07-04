import unittest
from test_vowels import count_vowels as vowel

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
        self.assertEqual(count_vowels("SomE"), 8)


if __name__ == '__main__':
    unittest.main()
