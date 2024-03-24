import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, state='disabled')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button_val in buttons:
    tk.Button(root, text=button_val, padx=20, pady=20).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()