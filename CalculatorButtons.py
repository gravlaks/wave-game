from tkinter import *
from ButtonText import ButtonText
from functools import partial
class CalculatorButtons:
    def __init__(self, root, calculator):
        self.buttons = {}
        self.initialize_buttons(root, calculator)
        self.base_row=1
        self.base_col=0

    def initialize_buttons(self, root, calculator):

        self.buttons[ButtonText.one]=Button(root, text=ButtonText.one.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.one.value))
        self.buttons[ButtonText.two]=Button(root, text=ButtonText.two.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.two.value))
        self.buttons[ButtonText.three]=Button(root, text=ButtonText.three.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.three.value))
        self.buttons[ButtonText.four]=Button(root, text=ButtonText.four.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.four.value))
        self.buttons[ButtonText.five]=Button(root, text=ButtonText.five.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.five.value))
        self.buttons[ButtonText.six]=Button(root, text=ButtonText.six.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.six.value))
        self.buttons[ButtonText.seven]=Button(root, text=ButtonText.seven.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.seven.value))
        self.buttons[ButtonText.eight]=Button(root, text=ButtonText.eight.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.eight.value))
        self.buttons[ButtonText.nine]=Button(root, text=ButtonText.nine.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.nine.value))
        self.buttons[ButtonText.zero]=Button(root, text=ButtonText.zero.value, padx=40, pady=20, command=partial(calculator.insert_text, ButtonText.zero.value))
        self.buttons[ButtonText.plus] = Button(root, text=ButtonText.plus.value,  padx=40, pady=20, command=partial(calculator.add, ))
        self.buttons[ButtonText.clear] = Button(root, text=ButtonText.clear.value,  padx=91, pady=20, command=calculator.clear_text_field)
        self.buttons[ButtonText.equal] = Button(root, text=ButtonText.equal.value, padx=91, pady=20, command=calculator.calculate)
        self.buttons[ButtonText.subtract] = Button(root, text=ButtonText.subtract.value, padx=40, pady=20, command=calculator.subtract)
        self.buttons[ButtonText.multiply] = Button(root, text=ButtonText.multiply.value, padx=40, pady=20, command=calculator.multiply)
        self.buttons[ButtonText.divide] = Button(root, text=ButtonText.divide.value, padx=40, pady=20, command=calculator.divide)

    def place_on_screen(self):
        self.buttons[ButtonText.one].grid(row=self.base_row+2, column=self.base_col)
        self.buttons[ButtonText.two].grid(row=self.base_row+2, column=self.base_col+1)
        self.buttons[ButtonText.three].grid(row=self.base_row+2, column=self.base_col+2)
        self.buttons[ButtonText.four].grid(row=self.base_row+1, column=self.base_col)
        self.buttons[ButtonText.five].grid(row=self.base_row+1, column=self.base_col+1)
        self.buttons[ButtonText.six].grid(row=self.base_row+1, column=self.base_col+2)
        self.buttons[ButtonText.seven].grid(row=self.base_row, column=self.base_col)
        self.buttons[ButtonText.eight].grid(row=self.base_row, column=self.base_col+1)
        self.buttons[ButtonText.nine].grid(row=self.base_row, column=self.base_col+2)
        self.buttons[ButtonText.zero].grid(row=self.base_row+3, column=self.base_col)

        self.buttons[ButtonText.plus].grid(row=self.base_row+4,  column=self.base_col)
        self.buttons[ButtonText.clear].grid(row=self.base_row+3, column=self.base_col+1, columnspan=2)
        self.buttons[ButtonText.equal].grid(row=self.base_row+4, column=self.base_col+1,columnspan=2)
        self.buttons[ButtonText.subtract].grid(row=self.base_row+6, column=self.base_col)
        self.buttons[ButtonText.multiply].grid(row=self.base_row+6, column=self.base_col+1)
        self.buttons[ButtonText.divide].grid(row=self.base_row+6, column=self.base_col+2)

