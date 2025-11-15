import tkinter as tk

root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x400")

pantalla = tk.Entry(root, font=("Arial", 20), justify="right")
pantalla.pack(fill="x", padx=10, pady=10)

root.mainloop()
