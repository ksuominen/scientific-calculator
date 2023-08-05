from algorithms import algorithm_helpers as helper
import math


def calculate(x, y, operator):
    """A function to calculate a simple mathematical expression with two operands and one operator.

    Args:
        x: The first operand. Type is either int or float.
        y: The second operand. Type is either int or float.
        operator (string): The mathematical operator.

    Returns:
        Returns the result of evaluating the expression. Return type is either int or float.
    """
    if operator == "+":
        return x + y

    if operator == "-":
        return x - y

    if operator == "*":
        return x * y

    if operator == "/":
        return x / y

    if operator == "^":
        return x**y


def calc_func_with_one_param(func, x):
    if func == "sqrt":
        return math.sqrt(x)


def calc_func_with_two_params(func, x, y):
    if func == "min":
        return min(x, y)


def evaluate(input):
    """A function for evaluating a mathematical expression in postfix notation.

    Args:
        input (list): A mathematical expression in postfix notation stored in a list.

    Raises:
        ValueError: Raises ValueError, if there are incompatible amount of numbers or operators.

    Returns:
        Returns the result of evaluating the expression. Return type is either int or float.
    """
    stack = []

    for token in input:
        if helper.is_number(token):
            stack.append(token)

        elif helper.is_operator(token):
            if len(stack) < 2:
                raise ValueError("Invalid input")
            right = stack.pop()
            left = stack.pop()
            stack.append(calculate(left, right, token))

        elif helper.is_function(token):
            if helper.get_parameter_amount(token) == 1:
                num = stack.pop()
                stack.append(calc_func_with_one_param(token, num))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(calc_func_with_two_params(token, left, right))

    if len(stack) != 1:
        raise ValueError("Invalid input")
    return stack.pop()
