import unittest
from algorithms import reverse_polish as re


class TestReversePolish(unittest.TestCase):
    def test_reverese_polish_1(self):
        # (2 + 1) * 3 = 9
        operation = [2, 1, "+", 3, "*"]
        self.assertEqual(re.evaluate(operation), 9)

    def test_reverese_polish_2(self):
        # 4 + 13 / 5 = 6.6
        operation = [4, 13, 5, "/", "+"]
        self.assertEqual(re.evaluate(operation), 6.6)

    def test_reverese_polish_3(self):
        # 1/2=0.5
        operation = [1, 2, "/"]
        self.assertEqual(re.evaluate(operation), 0.5)

    def test_reverese_polish_4(self):
        # (2+3)^2 = 25
        operation = [2, 3, "+", 2, "^"]
        self.assertEqual(re.evaluate(operation), 25)

    def test_reverese_polish_5(self):
        # (2 - 1) * 3 = 3
        operation = [2, 1, "-", 3, "*"]
        self.assertEqual(re.evaluate(operation), 3)

    def test_too_little_operands_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+"]
            re.evaluate(operation)

    def test_too_many_operands_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, 2, "+", 3, 4]
            re.evaluate(operation)
