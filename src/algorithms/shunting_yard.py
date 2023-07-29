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


def shunting_yard(input):
    output = []

    stack = []

    for token in input:
        if is_number(token):
            output.append(token)

        elif is_operator(token):
            if len(stack) == 0 or stack[-1] == "(":
                stack.append(token)
                continue
            prec = get_precedence(token)
            if prec > get_precedence(stack[-1]) or (
                prec > get_precedence(stack[-1]) and not is_left_associative(token)
            ):
                stack.append(token)
                continue

            while (stack and stack[-1] != "(") and (
                prec < get_precedence(stack[-1])
                or (prec == get_precedence(stack[-1]) and is_left_associative(token))
            ):
                output.append(stack.pop())
            stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            if not stack:
                raise ValueError("Too many opening brackets")
            stack_top = stack.pop()
            while stack_top != "(":
                if not stack:
                    raise ValueError("Too many opening brackets")
                output.append(stack_top)
                stack_top = stack.pop()

        else:
            raise ValueError("Invalid input")

    while stack:
        token = stack.pop()
        if token == "(":
            raise ValueError("Too many opening brackets")
        output.append(token)

    return output
