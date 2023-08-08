operator_precedences = {"+": 2, "\u2212": 2, "*": 3, "/": 3, "^": 4}

operator_associativities = {
    "+": "left",
    "\u2212": "left",  # minus
    "*": "left",
    "/": "left",
    "^": "right",
}

function_parameters = {
    "sqrt": 1,
    "abs": 1,
    "sin": 1,
    "cos": 1,
    "tan": 1,
    "rad": 1,
    "!": 1,
    "\u002D": 1,  # negate
    "log": 1,
    "ln": 1,
    "min": 2,
    "max": 2,
}


def get_precedence(operator):
    """A function to get precedence of an operator.

    Args:
        operator (string): A mathematical operator.

    Returns:
        int: Returns the precedence of the operator.
    """
    return operator_precedences.get(operator)


def get_associativity(operator):
    """A function to get associativity of an operator.

    Args:
        operator (string): A mathematical operator.

    Returns:
        string: Returns right or left.
    """
    return operator_associativities.get(operator)


def is_left_associative(operator):
    """Tests if the operator is lefr associative.

    Args:
        operator (string): A mathematical operator.

    Returns:
        boolean: Returns True if the operator is left associative, else False.
    """
    return get_associativity(operator) == "left"


def get_parameter_amount(token):
    """A function to get amount of function's parameters.

    Args:
        token (string): The function abbreviation.

    Returns:
        int: Returns 1 or 2 depending on the function.
    """
    return function_parameters.get(token)


def is_operator(token):
    """Tests if the input token is an operator.

    Args:
        token: The input token to be tested.

    Returns:
        boolean: Returns True if the token is included in the keyset of dictionary operator_precedences, else False.
    """
    return token in operator_precedences.keys()


def is_number(token):
    """Tests if the input token is a number.

    Args:
        token: The input token to be tested.

    Returns:
        boolean: Returns True if the token is of type int or float, else False.
    """
    return isinstance(token, (int, float))


def is_function(token):
    """Tests if the input token is a function.

    Args:
        token: The input token to be tested.

    Returns:
        boolean: Returns True if the token is an abbreviation of a function, else False.
    """
    return token in function_parameters.keys()
