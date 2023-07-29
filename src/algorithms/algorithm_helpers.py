operator_precedences = {"+": 2, "-": 2, "*": 3, "/": 3, "^": 4}

operator_associativities = {
    "+": "left",
    "-": "left",
    "*": "left",
    "/": "left",
    "^": "right",
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
