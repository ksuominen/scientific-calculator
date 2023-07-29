from algorithms import shunting_yard as sy, reverse_polish as rp


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
        # todo: replace self._expression with self.parse_input()
        try:
            postfix = sy.shunting_yard(self._expression)
            result = rp.evaluate(postfix)
        except:
            result = "Syntax error"
        self.clear()
        return result

    def parse_input(self):
        input = self._expression
        infix = []
        # todo: parse floats and multidigit numbers etc
        return infix
