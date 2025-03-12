import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

ttk.Label(win, text= "A_label").grid(column=30, row=30)

win.mainloop()
 