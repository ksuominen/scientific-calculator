from tkinter import *
import calculator as calc


class CalculatorView:
    def __init__(self, root):
        self._root = root
        self._calculator = calc.Calculator()
        self._input_field = None
        self._ans_field = None
        self._memorized_result_field = None
        self._initialize()

    def _initialize(self):
        input_frame = Frame(self._root)
        input_frame.pack(side=TOP)
        self._input_field = Label(
            input_frame, text="0", width=50, height=2, font=("Arial", 16), justify=RIGHT
        )
        self._input_field.grid(row=0, column=1, rowspan=2)

        self._ans_field = Label(
            input_frame, text="Ans=0", width=8, height=1, font=("Arial", 10)
        )
        self._ans_field.grid(row=0, column=0, padx=1)
        self._memorized_result_field = Label(
            input_frame, text="M=0", width=8, height=1, font=("Arial", 10)
        )
        self._memorized_result_field.grid(row=1, column=0, padx=1)

        button_width = 8
        button_height = 2
        button_border = 1
        button_font = ("Arial", 12)
        buttons_frame = Frame(self._root)
        buttons_frame.pack()
        ln_button = Button(
            buttons_frame,
            text="ln",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("ln"),
        ).grid(row=0, column=0)
        log_button = Button(
            buttons_frame,
            text="log",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("log"),
        ).grid(row=0, column=1)
        pi_button = Button(
            buttons_frame,
            text="\u03C0",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("\u03C0"),
        ).grid(row=0, column=2)
        neper_button = Button(
            buttons_frame,
            text="\u0065",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("\u0065"),
        ).grid(row=0, column=3)
        round_button = Button(
            buttons_frame,
            text="round",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("round"),
        ).grid(row=0, column=4)

        min_button = Button(
            buttons_frame,
            text="min",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("min"),
        ).grid(row=1, column=0)
        max_button = Button(
            buttons_frame,
            text="max",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("max"),
        ).grid(row=1, column=1)
        comma_button = Button(
            buttons_frame,
            text=",",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(","),
        ).grid(row=1, column=2)
        abs_button = Button(
            buttons_frame,
            text="abs",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("abs"),
        ).grid(row=1, column=3)
        factorial_button = Button(
            buttons_frame,
            text="!(x)",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("!"),
        ).grid(row=1, column=4)

        sin_button = Button(
            buttons_frame,
            text="sin",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("sin"),
        ).grid(row=2, column=0)
        cos_button = Button(
            buttons_frame,
            text="cos",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("cos"),
        ).grid(row=2, column=1)
        tan_button = Button(
            buttons_frame,
            text="tan",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("tan"),
        ).grid(row=2, column=2)
        rad_button = Button(
            buttons_frame,
            text="rad",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("rad"),
        ).grid(row=2, column=3)
        negate_button = Button(
            buttons_frame,
            text="(-)",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("\u002D"),
        ).grid(row=2, column=4)

        left_parenth_button = Button(
            buttons_frame,
            text="(",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("("),
        ).grid(row=3, column=0)
        right_parenth_button = Button(
            buttons_frame,
            text=")",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(")"),
        ).grid(row=3, column=1)
        sqrt_button = Button(
            buttons_frame,
            text="\u221A",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.function_button_click("\u221A"),
        ).grid(row=3, column=2)
        exp_button = Button(
            buttons_frame,
            text="^",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("^"),
        ).grid(row=3, column=3)
        clear_all_button = Button(
            buttons_frame,
            text="CE",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_clear(),
        ).grid(row=3, column=4)

        button7 = Button(
            buttons_frame,
            text="7",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(7),
        ).grid(row=4, column=0)
        button8 = Button(
            buttons_frame,
            text="8",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(8),
        ).grid(row=4, column=1)
        button9 = Button(
            buttons_frame,
            text="9",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(9),
        ).grid(row=4, column=2)
        div_button = Button(
            buttons_frame,
            text="÷",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("/"),
        ).grid(row=4, column=3)
        delete_button = Button(
            buttons_frame,
            text="C",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_delete(),
        ).grid(row=4, column=4)

        button4 = Button(
            buttons_frame,
            text="4",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(4),
        ).grid(row=5, column=0)
        button5 = Button(
            buttons_frame,
            text="5",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(5),
        ).grid(row=5, column=1)
        button6 = Button(
            buttons_frame,
            text="6",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(6),
        ).grid(row=5, column=2)
        mult_button = Button(
            buttons_frame,
            text="\u00D7",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("*"),
        ).grid(row=5, column=3)
        memory_button = Button(
            buttons_frame,
            text="M",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("M"),
        ).grid(row=5, column=4)

        button1 = Button(
            buttons_frame,
            text="1",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(1),
        ).grid(row=6, column=0)
        button2 = Button(
            buttons_frame,
            text="2",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(2),
        ).grid(row=6, column=1)
        button3 = Button(
            buttons_frame,
            text="3",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(3),
        ).grid(row=6, column=2)
        minus_button = Button(
            buttons_frame,
            text="\u2212",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("\u2212"),
        ).grid(row=6, column=3)
        save_button = Button(
            buttons_frame,
            text="Save",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_save(),
        ).grid(row=6, column=4)

        ans_button = Button(
            buttons_frame,
            text="Ans",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("Ans"),
        ).grid(row=7, column=0)
        button0 = Button(
            buttons_frame,
            text="0",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click(0),
        ).grid(row=7, column=1)
        dot_button = Button(
            buttons_frame,
            text=".",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("."),
        ).grid(row=7, column=2)
        plus_button = Button(
            buttons_frame,
            text="+",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_click("+"),
        ).grid(row=7, column=3)
        equal_button = Button(
            buttons_frame,
            text="=",
            width=button_width,
            height=button_height,
            bd=button_border,
            font=button_font,
            command=lambda: self.button_equal(),
        ).grid(row=7, column=4)

    def button_click(self, token):
        if token == "M":
            self._calculator.update_expression(self._calculator.get_saved_result())
        else:
            self._calculator.update_expression(token)
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def function_button_click(self, token):
        self._calculator.update_expression(token)
        self._calculator.update_expression("(")
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def button_clear(self):
        self._calculator.clear()
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def button_equal(self):
        result = self._calculator.calculate()
        self._input_field.config(text=result)
        self._ans_field.config(text=f"Ans={result}")

    def button_delete(self):
        self._calculator.delete_one()
        self._input_field.config(text=self._calculator.get_expression_as_string())

    def button_save(self):
        self._calculator.save_result()
        result = self._calculator.get_saved_result()
        self._memorized_result_field.config(text=f"M={result}")
