from ui.calculator_view import CalculatorView


class UI:
    """The class responsible for the user interface."""

    def __init__(self, root):
        """The constructor that initializes the user interface.

        Args:
            root (tkinter.Tk): The root of the user interface.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """The function that starts the user interface."""
        self._current_view = CalculatorView(self._root)
