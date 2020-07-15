from tkinter import *
from CalculatorButtons import CalculatorButtons


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
        numbers = self.text_entry.get().split("+")
        result = 0
        for elem in numbers:
            result += int(elem)
        self.text_entry.delete(0, END)
        self.text_entry.insert(0, result)

    def run(self):
        self.root.mainloop()


calculator = Calculator()
calculator.run()
