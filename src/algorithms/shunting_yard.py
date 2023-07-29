from algorithms import algorithm_helpers as helper


def shunting_yard(input):
    output = []

    stack = []

    for token in input:
        if helper.is_number(token):
            output.append(token)

        elif helper.is_operator(token):
            if len(stack) == 0 or stack[-1] == "(":
                stack.append(token)
                continue
            prec = helper.get_precedence(token)
            if prec > helper.get_precedence(stack[-1]) or (
                prec > helper.get_precedence(stack[-1])
                and not helper.is_left_associative(token)
            ):
                stack.append(token)
                continue

            while (stack and stack[-1] != "(") and (
                prec < helper.get_precedence(stack[-1])
                or (
                    prec == helper.get_precedence(stack[-1])
                    and helper.is_left_associative(token)
                )
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
