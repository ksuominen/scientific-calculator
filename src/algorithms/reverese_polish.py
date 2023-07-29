from algorithms import algorithm_helpers as helper


def calculate(x, y, operator):
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
    stack = []

    for token in input:
        if not helper.is_operator(token):
            stack.append(token)

        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(calculate(left, right, token))

    return stack.pop()
