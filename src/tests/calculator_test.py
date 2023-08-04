import unittest
import calculator as c


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
        self.assertEqual(expression, "")

    def test_calculate_add(self):
        self.calc.update_expression(2)
        self.calc.update_expression("+")
        self.calc.update_expression(2)
        result = self.calc.calculate()
        self.assertEqual(result, 4)

    def test_calculate_subtraction(self):
        self.calc.update_expression(20)
        self.calc.update_expression("-")
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
