import tkinter as tk

def calculate():
    try:
        equation = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, eval(equation))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_press(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_1 = tk.Button(button_frame, text="1", padx=40, pady=20, command=lambda: button_press(1))
button_2 = tk.Button(button_frame, text="2", padx=40, pady=20, command=lambda: button_press(2))
button_3 = tk.Button(button_frame, text="3", padx=40, pady=20, command=lambda: button_press(3))
button_4 = tk.Button(button_frame, text="4", padx=40, pady=20, command=lambda: button_press(4))
button_5 = tk.Button(button_frame, text="5", padx=40, pady=20, command=lambda: button_press(5))
button_6 = tk.Button(button_frame, text="6", padx=40, pady=20, command=lambda: button_press(6))
button_7 = tk.Button(button_frame, text="7", padx=40, pady=20, command=lambda: button_press(7))
button_8 = tk.Button(button_frame, text="8", padx=40, pady=20, command=lambda: button_press(8))
button_9 = tk.Button(button_frame, text="9", padx=40, pady=20, command=lambda: button_press(9))
button_0 = tk.Button(button_frame, text="0", padx=40, pady=20, command=lambda: button_press(0))
button_add = tk.Button(button_frame, text="+", padx=39, pady=20, command=lambda: button_press("+"))
button_subtract = tk.Button(button_frame, text="-", padx=41, pady=20, command=lambda: button_press("-"))
button_multiply = tk.Button(button_frame, text="*", padx=40, pady=20, command=lambda: button_press("*"))
button_divide = tk.Button(button_frame, text="/", padx=41, pady=20, command=lambda: button_press("/"))
button_equal = tk.Button(button_frame, text="=", padx=91, pady=20, command=calculate)
button_clear = tk.Button(button_frame, text="Clear", padx=79, pady=20, command=clear)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
