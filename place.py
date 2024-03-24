import tkinter as tk

root = tk.Tk()
root.title("Login Page")

username_label = tk.Label(root, text="Username")
username_label.place(x=10, y=10)

username_entry = tk.Entry(root)
username_entry.place(x=100, y=10)

password_label = tk.Label(root, text="Password")
password_label.place(x=10, y=40)

password_entry = tk.Entry(root)
password_entry.place(x=100, y=40)

login_button = tk.Button(root, text="Login")
login_button.place(x=50, y=80)

root.mainloop()