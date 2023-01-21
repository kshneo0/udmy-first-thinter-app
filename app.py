import tkinter as tk
from tkinter import ttk


def greet():
    print("Helli, World!")


root = tk.Tk()
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="y", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left")


root.mainloop()