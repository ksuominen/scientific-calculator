from tkinter import *
import calculator as calc


class CalculatorView:
    def __init__(self, root):
        self._root = root
        self._calculator = calc.Calculator()
        self._input_field = None
        self._initialize()

    def _initialize(self):
        input_frame = Frame(self._root)
        input_frame.pack(side=TOP)
        self._input_field = Label(input_frame, text="0", justify=RIGHT)
        self._input_field.pack()
        buttons_frame = Frame(self._root)
        buttons_frame.pack()
        button1 = Button(
            buttons_frame, text="1", command=lambda: self.button_click(1)
        ).grid(row=0, column=0)
        button2 = Button(
            buttons_frame, text="2", command=lambda: self.button_click(2)
        ).grid(row=0, column=1)
        button3 = Button(
            buttons_frame, text="3", command=lambda: self.button_click(3)
        ).grid(row=0, column=2)
        plus_button = Button(
            buttons_frame, text="+", command=lambda: self.button_click("+")
        ).grid(row=1, column=0)
        equal_button = Button(
            buttons_frame, text="=", command=lambda: self.button_equal()
        ).grid(row=1, column=1)
        clear_button = Button(
            buttons_frame, text="CE", command=lambda: self.button_clear()
        ).grid(row=1, column=2)

    def button_click(self, token):
        self._calculator.update_expression(token)
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def button_clear(self):
        self._calculator.clear()
        self._input_field.config(text="0")

    def button_equal(self):
        result = self._calculator.calculate()
        self._input_field.config(text=result)
