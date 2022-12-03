import unittest
from main import count_digits


class TestCountDigits(unittest.TestCase):
    def wrong_type(self):
        with self.assertRaises(AssertionError):
            count_digits(42)

    def str_subclasses(self):
        class TestStr(str):
            pass
        line = TestStr("The answer is 42")
        self.assertEqual(count_digits(line), 2)

    def no_digits(self):
        self.assertEqual(count_digits("The answer is..."), 0)

    def all_digits(self):
        self.assertEqual(count_digits("1234567890"), 10)

    def some_digits(self):
        self.assertEqual(count_digits("The answer is 42"), 2)


if __name__ == '__main__':
    unittest.main()
