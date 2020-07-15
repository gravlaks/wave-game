from tkinter import *
parent_window = Tk()


canvas = Canvas(parent_window, bd=4, bg="green")

circle = canvas.create_oval(0, 0, 3, 3, fill="red")
canvas.pack()
parent_window.mainloop()
