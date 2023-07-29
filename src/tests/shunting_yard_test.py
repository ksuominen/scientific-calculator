import unittest
from algorithms import shunting_yard as sy


class TestShuntingYard(unittest.TestCase):
    def test_get_precedence_plus(self):
        precedence = sy.get_precedence("+")
        self.assertEqual(precedence, 2)

    def test_get_precedence_power(self):
        precedence = sy.get_precedence("^")
        self.assertEqual(precedence, 4)

    def test_get_associativity_division(self):
        assoc = sy.get_associativity("/")
        self.assertEqual(assoc, "left")

    def test_get_associativity_power(self):
        assoc = sy.get_associativity("^")
        self.assertEqual(assoc, "right")

    def test_multiplication_is_left_associative(self):
        self.assertTrue(sy.is_left_associative("*"))

    def test_power_is_not_left_associative(self):
        self.assertFalse(sy.is_left_associative("^"))

    def test_is_operator_minus(self):
        self.assertTrue(sy.is_operator("-"))

    def test_char_not_operator(self):
        self.assertFalse(sy.is_operator("b"))

    def test_number_not_operator(self):
        self.assertFalse(sy.is_operator(5))

    def test_is_number_int(self):
        self.assertTrue(sy.is_number(7))

    def test_is_number_float(self):
        self.assertTrue(sy.is_number(17.34))

    def test_string_is_not_number(self):
        self.assertFalse(sy.is_number("Hello"))

    def test_operator_is_not_number(self):
        self.assertFalse(sy.is_number("^"))

    def test_invalid_input_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+", 2, "hello"]
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
        operation = [4, "+", 18, "/", "(", 9, "-", 3, ")"]
        result = [4, 18, 9, 3, "-", "/", "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_2(self):
        operation = [3, "+", 4, "*", 2, "/", "(", 1, "-", 5, ")", "^", 2, "^", 3]
        result = [3, 4, 2, "*", 1, 5, "-", 2, 3, "^", "^", "/", "+"]
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
        operation = [1, "-", 2, "+", 3]
        result = [1, 2, "-", 3, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_7(self):
        operation = [1, "*", 2, "^", 3, "+", 4]
        result = [1, 2, 3, "^", "*", 4, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)

    def test_shunting_yard_8(self):
        operation = [1, "*", "(", 2, "+", 3, "*", 4, ")", "+", 5]
        result = [1, 2, 3, 4, "*", "+", "*", 5, "+"]
        self.assertEqual(sy.shunting_yard(operation), result)
