from ui.calculator_view import CalculatorView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._current_view = CalculatorView(self._root)
