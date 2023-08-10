import unittest
import calculator as c
from math import pi, e


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = c.Calculator()

    def test_update_get_expression_works(self):
        self.calc.update_expression(23)
        expression = self.calc.get_expression_as_string()
        self.assertEqual(expression, "23")

    def test_update_get_expression_works2(self):
        self.calc.update_expression(2)
        self.calc.update_expression("+")
        self.calc.update_expression(2)
        expression = self.calc.get_expression_as_string()
        self.assertEqual(expression, "2+2")

    def test_clear_expression_works(self):
        self.calc.update_expression(23)
        self.calc.clear()
        expression = self.calc.get_expression_as_string()
        self.assertEqual(expression, "0")

    def test_calculate_add(self):
        self.calc.update_expression(2)
        self.calc.update_expression("+")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.assertEqual(result, 4)

    def test_calculate_subtraction(self):
        self.calc.update_expression(20)
        self.calc.update_expression("\u2212")
        self.calc.update_expression(5)
        result = self.calc.calculate()
        self.assertEqual(result, 15)

    def test_calculate_multiply(self):
        self.calc.update_expression(10)
        self.calc.update_expression("*")
        self.calc.update_expression(9)
        result = self.calc.calculate()
        self.assertEqual(result, 90)

    def test_calculate_divide(self):
        self.calc.update_expression(10)
        self.calc.update_expression("/")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.assertEqual(result, 5)

    def test_calculate_power(self):
        self.calc.update_expression(3)
        self.calc.update_expression("^")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.assertEqual(result, 9)

    def test_calculate_returns_syntax_error_with_invalid_input(self):
        self.calc.update_expression("aa")
        self.calc.update_expression("^")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.assertEqual(result, "Syntax error")

    def test_parse_input_multidigit_works(self):
        self.calc.update_expression(1)
        self.calc.update_expression(2)
        self.calc.update_expression(3)
        result = self.calc.parse_input()
        self.assertEqual(result, [123])

    def test_parse_input_float_works(self):
        self.calc.update_expression(1)
        self.calc.update_expression(".")
        self.calc.update_expression(2)
        self.calc.update_expression(3)
        result = self.calc.parse_input()
        self.assertEqual(result, [1.23])

    def test_parse_input_multidigit_with_operator_works(self):
        self.calc.update_expression(1)
        self.calc.update_expression(2)
        self.calc.update_expression("+")
        self.calc.update_expression(3)
        result = self.calc.parse_input()
        self.assertEqual(result, [12, "+", 3])

    def test_parse_input_float_with_operator_works(self):
        self.calc.update_expression(4)
        self.calc.update_expression("*")
        self.calc.update_expression(1)
        self.calc.update_expression(".")
        self.calc.update_expression(2)
        self.calc.update_expression(3)
        result = self.calc.parse_input()
        self.assertEqual(result, [4, "*", 1.23])

    def test_parse_input_with_parentheses_works(self):
        self.calc.update_expression(4)
        self.calc.update_expression(".")
        self.calc.update_expression(1)
        self.calc.update_expression("*")
        self.calc.update_expression("(")
        self.calc.update_expression(2)
        self.calc.update_expression("+")
        self.calc.update_expression(3)
        self.calc.update_expression(")")
        result = self.calc.parse_input()
        self.assertEqual(result, [4.1, "*", "(", 2, "+", 3, ")"])

    def test_too_many_dots_raises_valueerror(self):
        self.calc.update_expression(1)
        self.calc.update_expression(".")
        self.calc.update_expression(".")
        self.calc.update_expression(2)
        with self.assertRaises(ValueError):
            self.calc.parse_input()

    def test_too_many_dots_with_operator_raises_valueerror(self):
        self.calc.update_expression(1)
        self.calc.update_expression(".")
        self.calc.update_expression(".")
        self.calc.update_expression(2)
        self.calc.update_expression("*")
        self.calc.update_expression(2)
        with self.assertRaises(ValueError):
            self.calc.parse_input()

    def test_calculate_with_sqrt(self):
        self.calc.update_expression("sqrt")
        self.calc.update_expression("(")
        self.calc.update_expression(4)
        self.calc.update_expression(")")
        result = self.calc.calculate()
        self.assertEqual(result, 2)

    def test_calculate_with_min(self):
        self.calc.update_expression("min")
        self.calc.update_expression("(")
        self.calc.update_expression(4)
        self.calc.update_expression(",")
        self.calc.update_expression(1)
        self.calc.update_expression(")")
        result = self.calc.calculate()
        self.assertEqual(result, 1)

    def test_delete_one_works(self):
        self.calc.update_expression(23)
        self.calc.update_expression("+")
        self.calc.update_expression(4)
        self.calc.update_expression(5)
        self.calc.delete_one()
        expression = self.calc.get_expression_as_string()
        self.assertEqual(expression, "23+4")

    def test_delete_one_with_empty_expression(self):
        self.calc.delete_one()
        expression = self.calc.get_expression_as_string()
        self.assertEqual(expression, "0")

    def test_parse_input_with_pi_works(self):
        self.calc.update_expression("\u03C0")
        result = self.calc.parse_input()
        self.assertEqual(result, [pi])

    def test_parse_input_with_neper_works(self):
        self.calc.update_expression("\u0065")
        result = self.calc.parse_input()
        self.assertEqual(result, [e])

    def test_parse_input_with_sqrt_works(self):
        self.calc.update_expression("\u221A")
        result = self.calc.parse_input()
        self.assertEqual(result, ["sqrt"])

    def test_parse_input_with_ans_works(self):
        self.calc.update_expression(1)
        self.calc.update_expression("+")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.calc.update_expression("Ans")
        result = self.calc.parse_input()
        self.assertEqual(result, [3])
