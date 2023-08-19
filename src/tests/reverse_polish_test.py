import unittest
from algorithms import reverse_polish as re
import math


class TestReversePolish(unittest.TestCase):
    def test_evaluate_1(self):
        # (2 + 1) * 3 = 9
        operation = [2, 1, "+", 3, "*"]
        self.assertEqual(re.evaluate(operation), 9)

    def test_evaluate_2(self):
        # 4 + 13 / 5 = 6.6
        operation = [4, 13, 5, "/", "+"]
        self.assertEqual(re.evaluate(operation), 6.6)

    def test_evaluate_3(self):
        # 1/2=0.5
        operation = [1, 2, "/"]
        self.assertEqual(re.evaluate(operation), 0.5)

    def test_evaluate_4(self):
        # (2+3)^2 = 25
        operation = [2, 3, "+", 2, "^"]
        self.assertEqual(re.evaluate(operation), 25)

    def test_evaluate_5(self):
        # (2 - 1) * 3 = 3
        operation = [2, 1, "\u2212", 3, "*"]
        self.assertEqual(re.evaluate(operation), 3)

    def test_too_little_operands_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, "+"]
            re.evaluate(operation)

    def test_too_many_operands_raises_valueerror(self):
        with self.assertRaises(ValueError):
            operation = [1, 2, "+", 3, 4]
            re.evaluate(operation)

    def test_calc_func_with_one_param_works(self):
        # √(4) = 2
        self.assertEqual(re.calc_func_with_one_param("sqrt", 4), 2)

    def test_calc_func_with_two_params_works(self):
        self.assertEqual(re.calc_func_with_two_params("min", 4, 1), 1)

    def test_evaluate_with_sqrt_works(self):
        # √(2+2) * 3 = 6
        operation = [2, 2, "+", "sqrt", 3, "*"]
        result = re.evaluate(operation)
        self.assertEqual(result, 6)

    def test_evaluate_with_abs_works(self):
        # abs(1-2) = 1
        operation = [1, 2, "\u2212", "abs"]
        result = re.evaluate(operation)
        self.assertEqual(result, 1)

    def test_evaluate_with_sin_works(self):
        operation = [45, "sin"]
        result = re.evaluate(operation)
        self.assertEqual(result, math.sin(45))

    def test_evaluate_with_cos_works(self):
        operation = [45, "cos"]
        result = re.evaluate(operation)
        self.assertEqual(result, math.cos(45))

    def test_evaluate_with_tan_works(self):
        operation = [45, "tan"]
        result = re.evaluate(operation)
        self.assertEqual(result, math.tan(45))

    def test_evaluate_with_negate_works(self):
        operation = [1, "\u002D"]
        result = re.evaluate(operation)
        self.assertEqual(result, -1)

    def test_evaluate_with_min_works(self):
        operation = [2, 3, "min"]
        result = re.evaluate(operation)
        self.assertEqual(result, 2)

    def test_evaluate_with_max_works(self):
        operation = [8, 3, "max"]
        result = re.evaluate(operation)
        self.assertEqual(result, 8)

    def test_evaluate_round_works(self):
        operation = [8.3, "round"]
        result = re.evaluate(operation)
        self.assertEqual(result, 8)

    def test_evaluate_factorial_works(self):
        operation = [4, "!"]
        result = re.evaluate(operation)
        self.assertEqual(result, 24)

    def test_evaluate_degree_to_radians_works(self):
        operation = [180, "rad"]
        result = re.evaluate(operation)
        self.assertEqual(result, math.pi)

    def test_evaluate_log_works(self):
        operation = [10, "log"]
        result = re.evaluate(operation)
        self.assertEqual(result, 1)

    def test_evaluate_ln_works(self):
        operation = [math.e, "ln"]
        result = re.evaluate(operation)
        self.assertEqual(result, 1)
