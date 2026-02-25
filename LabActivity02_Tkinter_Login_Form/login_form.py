import tkinter as tk
from tkinter import messagebox

def validate_login(username_entry, password_entry, status_label):
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "admin" and password == "password123":
        status_label.config(text="Login Successful!", fg="green")
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        status_label.config(text="Invalid credentials!", fg="red")
        messagebox.showerror("Error", "Username or password incorrect")

def main():
    root = tk.Tk()
    root.title("Login Form")
    root.geometry("320x180")

    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root, width=25)

    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root, show="*", width=25)

    status_label = tk.Label(root, text="", fg="green")

    login_button = tk.Button(
        root,
        text="Login",
        width=10,
        bg="lightblue",
        command=lambda: validate_login(username_entry, password_entry, status_label),
    )

    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button.grid(row=2, column=0, columnspan=2, pady=10)
    status_label.grid(row=3, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
