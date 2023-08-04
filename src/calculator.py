from algorithms import (
    shunting_yard as sy,
    reverse_polish as rp,
    algorithm_helpers as helper,
)


class Calculator:
    def __init__(self):
        self._expression = []

    def update_expression(self, token):
        self._expression.append(token)

    def get_expression_as_string(self):
        return "".join(map(str, self._expression))

    def clear(self):
        self._expression.clear()

    def calculate(self):
        try:
            postfix = sy.shunting_yard(self.parse_input())
            result = rp.evaluate(postfix)
        except:
            result = "Syntax error"
        self.clear()
        return result

    def parse_input(self):
        input = self._expression
        infix = []
        current = ""

        for token in input:
            if helper.is_number(token) or token == ".":
                current += str(token)
            else:
                if current:
                    if current.count(".") > 1:
                        raise ValueError("Invalid input")
                    if "." in current:
                        infix.append(float(current))
                        current = ""
                    else:
                        infix.append(int(current))
                        current = ""
                infix.append(token)

        if current:
            if current.count(".") > 1:
                raise ValueError("Invalid input")
            if "." in current:
                infix.append(float(current))
            else:
                infix.append(int(current))
        return infix
