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

    if operator == "\u2212":
        return x - y

    if operator == "*":
        return x * y

    if operator == "/":
        return x / y

    if operator == "^":
        return x**y


def calc_func_with_one_param(func, x):
    """A function to calculate the result of a function with one parameter.

    Args:
        func (string): A function to be calculated.
        x: The parameter of the function. Type may be int or float.

    Returns:
        Returns the result of the expression. Type may be int or float.
    """
    if func == "sqrt":
        return math.sqrt(x)
    elif func == "abs":
        return abs(x)
    elif func == "sin":
        return math.sin(x)
    elif func == "cos":
        return math.cos(x)
    elif func == "tan":
        return math.tan(x)
    elif func == "rad":
        return math.radians(x)
    elif func == "\u002D":
        return -1 * x
    elif func == "!":
        return math.factorial(x)
    elif func == "log":
        return math.log10(x)
    elif func == "ln":
        return math.log(x)
    elif func == "round":
        return round(x)


def calc_func_with_two_params(func, x, y):
    """A function to calculate the result of a function with two parameters.

    Args:
        func (string): A function to be calculated.
        x: The parameter of the function. Type may be int or float.
        y The parameter of the function. Type may be int or float.

    Returns:
        Returns the result of the expression. Type may be int or float.
    """
    if func == "min":
        return min(x, y)
    elif func == "max":
        return max(x, y)


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
