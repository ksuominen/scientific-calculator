from algorithms import (
    shunting_yard as sy,
    reverse_polish as rp,
    algorithm_helpers as helper,
)


class Calculator:
    """A class to present a calculator."""

    def __init__(self):
        """The constructor of the class, creates a new calculator."""
        self._expression = []

    def update_expression(self, token):
        """A method to update the calculator's expression (list).

        Args:
            token: A token to be added to the expression.
        """
        self._expression.append(token)

    def get_expression_as_string(self):
        """A method to display calculator's expression as string.

        Returns:
            string: Returns the expression as string.
        """
        return "".join(map(str, self._expression))

    def clear(self):
        """A method to clear calculator's expression."""
        self._expression.clear()

    def calculate(self):
        """A method to calculate the value of the calculator's expression.

        Returns:
            Returns the value of the expression. May be int or float.
        """
        try:
            postfix = sy.shunting_yard(self.parse_input())
            result = rp.evaluate(postfix)
        except:
            result = "Syntax error"
        self.clear()
        return result

    def parse_input(self):
        """A method to parse the multidigit numbers and floats in the calculator's expression.

        Raises:
            ValueError: Raises ValueError if there are too many dots in a float.

        Returns:
            list: Returns a list where the multidigit numbers and floats are parsed.
        """
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
