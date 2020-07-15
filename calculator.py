from tkinter import *
from functools import partial

root = Tk()

root.title("Calculator")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = []
def button_click(symbol):
    print(symbol)
    e.insert(END, symbol)

def clear_text_field():
    e.delete(0, END)

def calculate():
    numbers = e.get().split("+")
    result = 0
    for elem in numbers:
        result += int(elem)
    e.delete(0, END)
    e.insert(0, result)


base_col = 0
max_col = 2
bottom_row = 4

for i in range(10):
    if i==0:
        row = bottom_row
        col = base_col
    else:
        row = bottom_row-(i+2)//3
        col = (i+2)%3
    local_copy = i
    print(int(local_copy))
    buttons.append(Button(root, text=str(i), padx=40, pady=20, command=partial(button_click, i)))
    buttons[i].grid(row=row, column=col)
    print(i, row, col)

button_add = Button(root, text="+", padx=39, pady=20, command=partial(button_click, "+"))
button_clear = Button(root, text="clear",  padx=79, pady=20, command=clear_text_field)
button_equal = Button(root, text="=", padx=91, pady=20, command=calculate)
button_add.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
    
root.mainloop()

