import unittest
from algorithms import shunting_yard as sy


class TestShuntingYard(unittest.TestCase):
    def test_invalid_input_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+", 2, "hello"]
            sy.shunting_yard(operation)

    def test_invalid_input_raises_valueerror2(self):
        with self.assertRaises(ValueError):
            operation = [","]
            sy.shunting_yard(operation)

    def test_invalid_input_raises_valueerror3(self):
        with self.assertRaises(ValueError):
            operation = [",", 2]
            sy.shunting_yard(operation)

    def test_invalid_input_raises_valueerror4(self):
        with self.assertRaises(ValueError):
            operation = [")"]
            sy.shunting_yard(operation)

    def test_too_many_opening_brackets_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+", 2, "("]
            sy.shunting_yard(operation)

    def test_too_many_closing_brackets_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+", 2, ")"]
            sy.shunting_yard(operation)

    def test_shunting_yard_1(self):
        operation = [4, "+", 18, "/", "(", 9, "\u2212", 3, ")"]
        result = [4, 18, 9, 3, "\u2212", "/", "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_2(self):
        operation = [3, "+", 4, "*", 2, "/", "(", 1, "\u2212", 5, ")", "^", 2, "^", 3]
        result = [3, 4, 2, "*", 1, 5, "\u2212", 2, 3, "^", "^", "/", "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_3(self):
        operation = [1, "*", 2, "+", 3]
        result = [1, 2, "*", 3, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_4(self):
        operation = [1, "+", 2, "*", 3]
        result = [1, 2, 3, "*", "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_5(self):
        operation = [1, "*", "(", 2, "+", 3, ")"]
        result = [1, 2, 3, "+", "*"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_6(self):
        operation = [1, "\u2212", 2, "+", 3]
        result = [1, 2, "\u2212", 3, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_7(self):
        operation = [1, "*", 2, "^", 3, "+", 4]
        result = [1, 2, 3, "^", "*", 4, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_8(self):
        operation = [1, "*", "(", 2, "+", 3, "*", 4, ")", "+", 5]
        result = [1, 2, 3, 4, "*", "+", "*", 5, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_min(self):
        operation = ["min", "(", 2, ",", 3, ")"]
        result = [2, 3, "min"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_sqrt(self):
        operation = ["sqrt", "(", 1, "+", 2, ")", "*", 3]
        result = [1, 2, "+", "sqrt", 3, "*"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_sqrt_min(self):
        operation = ["sqrt", "(", "min", "(", 2, ",", 3, ")", "/", 3, "*", 2, ")"]
        result = [2, 3, "min", 3, "/", 2, "*", "sqrt"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_invalid_input_with_comma_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = ["+", ",", 3, ")"]
            sy.shunting_yard(operation)
