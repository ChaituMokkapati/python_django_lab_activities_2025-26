import tkinter as tk

def main():
    root = tk.Tk()
    root.title("My First Tkinter Window")
    root.geometry("400x300")

    label = tk.Label(root, text="Hello, Welcome to Tkinter!", font=("Arial", 14))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
