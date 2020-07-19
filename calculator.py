from tkinter import *
from CalculatorButtons import CalculatorButtons

from enum import Enum, unique

@unique
class Action(Enum):
    add = 0
    subtract = 1
    multiply = 2
    divide = 3

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.buttons = CalculatorButtons(self.root, self)
        self.buttons.place_on_screen()

        self.text_entry = Entry(self.root, width=35, borderwidth=5)
        self.text_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        

        

    def insert_text(self, symbol):
        self.text_entry.insert(END, symbol)

    def clear_text_field(self):
        self.text_entry.delete(0, END)

    def calculate(self):
        current_number = int(self.text_entry.get())
        self.clear_text_field()
        result = 0
        if self.action == Action.add:
            result = current_number + self.previous_value
        if self.action== Action.subtract:
            result = current_number - self.previous_value
        if self.action== Action.multiply:
            result = current_number * self.previous_value
        if self.action== Action.divide:
            result = current_number / self.previous_value


        self.text_entry.insert(0, result)

    def subtract(self):
        self.previous_value = int(self.text_entry.get())
        self.action = Action.subtract
        self.clear_text_field()

    def add(self):
        self.previous_value = int(self.text_entry.get())
        self.action = Action.add
        self.clear_text_field()

    def multiply(self):
        self.previous_value = int(self.text_entry.get())
        self.action = Action.multiply
        self.clear_text_field()

    def divide(self):
        self.previous_value = int(self.text_entry.get())
        self.action = Action.divide
        self.clear_text_field()

    def run(self):
        self.root.mainloop()


calculator = Calculator()
calculator.run()
