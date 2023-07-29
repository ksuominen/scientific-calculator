from algorithms import algorithm_helpers as helper


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


def evaluate(input):
    """A function for evaluating a mathematical expression in postfix notation.

    Args:
        input (list): A mathematical expression in postfix notation stored in a list.

    Returns:
        Returns the result of evaluating the expression. Return type is either int or float.
    """
    stack = []

    for token in input:
        if not helper.is_operator(token):
            stack.append(token)

        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(calculate(left, right, token))

    return stack.pop()
