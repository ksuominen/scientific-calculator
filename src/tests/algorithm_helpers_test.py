import unittest
from algorithms import algorithm_helpers as helper


class TestAlgorithmHelpers(unittest.TestCase):
    def test_get_precedence_plus(self):
        precedence = helper.get_precedence("+")
        self.assertEqual(precedence, 2)

    def test_get_precedence_power(self):
        precedence = helper.get_precedence("^")
        self.assertEqual(precedence, 4)

    def test_get_associativity_division(self):
        assoc = helper.get_associativity("/")
        self.assertEqual(assoc, "left")

    def test_get_associativity_power(self):
        assoc = helper.get_associativity("^")
        self.assertEqual(assoc, "right")

    def test_multiplication_is_left_associative(self):
        self.assertTrue(helper.is_left_associative("*"))

    def test_power_is_not_left_associative(self):
        self.assertFalse(helper.is_left_associative("^"))

    def test_is_operator_minus(self):
        self.assertTrue(helper.is_operator("-"))

    def test_char_not_operator(self):
        self.assertFalse(helper.is_operator("b"))

    def test_number_not_operator(self):
        self.assertFalse(helper.is_operator(5))

    def test_is_number_int(self):
        self.assertTrue(helper.is_number(7))

    def test_is_number_float(self):
        self.assertTrue(helper.is_number(17.34))

    def test_string_is_not_number(self):
        self.assertFalse(helper.is_number("Hello"))

    def test_operator_is_not_number(self):
        self.assertFalse(helper.is_number("^"))
