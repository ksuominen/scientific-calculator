operator_precedences = {"+": 2, "-": 2, "*": 3, "/": 3, "^": 4}

operator_associativities = {
    "+": "left",
    "-": "left",
    "*": "left",
    "/": "left",
    "^": "right",
}


def get_precedence(operator):
    return operator_precedences.get(operator)


def get_associativity(operator):
    return operator_associativities.get(operator)


def is_left_associative(operator):
    return get_associativity(operator) == "left"


def is_operator(token):
    return token in operator_precedences.keys()


def is_number(token):
    return isinstance(token, (int, float))
