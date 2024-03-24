import tkinter as tk

root = tk.Tk()
root.title("Sign Up Page")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="Email").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)
tk.Label(root, text="Password").grid(row=2, column=0)
tk.Entry(root).grid(row=2, column=1)
tk.Button(root, text="Sign Up Now").grid(row=3, columnspan=2)

root.mainloop()