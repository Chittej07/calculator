import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))

        self.button_add = tk.Button(master, text="+", padx=39, pady=20, command=lambda: self.button_operation("+"))
        self.button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=lambda: self.button_operation("-"))
        self.button_multiply = tk.Button(master, text="*", padx=40, pady=20, command=lambda: self.button_operation("*"))
        self.button_divide = tk.Button(master, text="/", padx=41, pady=20, command=lambda: self.button_operation("/"))
        self.button_power = tk.Button(master, text="x^y", padx=37, pady=20, command=lambda: self.button_operation("**"))
        self.button_root = tk.Button(master, text="√x", padx=37, pady=20, command=lambda: self.button_operation("sqrt"))
        self.button_mod = tk.Button(master, text="%", padx=39, pady=20, command=lambda: self.button_operation("%"))

        self.button_decimal = tk.Button(master, text=".", padx=41, pady=20, command=lambda: self.button_operation("."))
        self.button_clear = tk.Button(master, text="C", padx=91, pady=20, command=self.clear)
        self.button_equals = tk.Button(master, text="=", padx=91, pady=20, command=self.calculate)

        # Place buttons on the grid
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)