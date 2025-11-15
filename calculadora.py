import tkinter as tk

root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x400")

pantalla = tk.Entry(root, font=("Arial", 20), justify="right")
pantalla.pack(fill="x", padx=10, pady=10)

root.mainloop()
def click(valor):
    pantalla.insert(tk.END, valor)

frame_botones = tk.Frame(root)
frame_botones.pack()

botones = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", ".", "C"]
]

for fila in botones:
    fila_frame = tk.Frame(frame_botones)
    fila_frame.pack()
    for b in fila:
        tk.Button(
            fila_frame, text=b, width=5, height=2, font=("Arial", 16),
            command=lambda x=b: click(x)
        ).pack(side="left", padx=5, pady=5)
