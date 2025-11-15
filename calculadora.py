import tkinter as tk

root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x400")

# -------------------------------
# Pantalla
# -------------------------------
pantalla = tk.Entry(root, font=("Arial", 20), justify="right")
pantalla.pack(fill="x", padx=10, pady=10)


# -------------------------------
# Función click para números
# -------------------------------
def click(valor):
    pantalla.insert(tk.END, valor)


# -------------------------------
# Botones numéricos
# -------------------------------
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
        if b == "C":
            tk.Button(
                fila_frame, text=b, width=5, height=2, font=("Arial", 16),
                command=lambda: pantalla.delete(0, tk.END)
            ).pack(side="left", padx=5, pady=5)
        else:
            tk.Button(
                fila_frame, text=b, width=5, height=2, font=("Arial", 16),
                command=lambda x=b: click(x)
            ).pack(side="left", padx=5, pady=5)


# -------------------------------
# Función para operaciones
# -------------------------------
def operar(op):
    pantalla.insert(tk.END, op)


# -------------------------------
# Botones de + - * /
# -------------------------------
ops = tk.Frame(root)
ops.pack()

for op in ["+", "-", "*", "/"]:
    tk.Button(
        ops, text=op, width=5, height=2, font=("Arial", 16),
        command=lambda x=op: operar(x)
    ).pack(side="left", padx=5, pady=5)


# -------------------------------
# Cálculo
# -------------------------------
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")


# -------------------------------
# Botón =
# -------------------------------
tk.Button(
    root, text="=", width=10, height=2, font=("Arial", 16),
    bg="lightblue", command=calcular
).pack(pady=10)


# -------------------------------
# MAINLOOP FINAL (Siempre al final)
# -------------------------------
root.mainloop()
    