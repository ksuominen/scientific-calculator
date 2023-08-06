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
        delete_button = Button(
            buttons_frame, text="C", command=lambda: self.button_delete()
        ).grid(row=2, column=0)
        negate_button = Button(
            buttons_frame,
            text="(-)",
            command=lambda: self.function_button_click("negate"),
        ).grid(row=2, column=1)
        dot_button = Button(
            buttons_frame, text=".", command=lambda: self.button_click(".")
        ).grid(row=2, column=2)
        left_parenth_button = Button(
            buttons_frame, text="(", command=lambda: self.button_click("(")
        ).grid(row=3, column=0)
        rigth_parenth_button = Button(
            buttons_frame, text=")", command=lambda: self.button_click(")")
        ).grid(row=3, column=1)
        min_button = Button(
            buttons_frame,
            text="min",
            command=lambda: self.function_button_click("min"),
        ).grid(row=3, column=2)
        comma_button = Button(
            buttons_frame, text=",", command=lambda: self.button_click(",")
        ).grid(row=3, column=3)

    def button_click(self, token):
        self._calculator.update_expression(token)
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def function_button_click(self, token):
        self._calculator.update_expression(token)
        self._calculator.update_expression("(")
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def button_clear(self):
        self._calculator.clear()
        self._input_field.config(text="0")

    def button_equal(self):
        result = self._calculator.calculate()
        self._input_field.config(text=result)

    def button_delete(self):
        self._calculator.delete_one()
        self._input_field.config(text=self._calculator.get_expression_as_string())
