import tkinter as tk
from tkinter import messagebox
import math

class FormularioTrianguloRectangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Triángulo Rectángulo")

        # Etiquetas
        tk.Label(root, text="Base").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Altura").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Área").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Perímetro").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(root, text="Tipo").grid(row=4, column=0, padx=10, pady=5)

        # Entradas de texto
        self.txtBase = tk.Entry(root)
        self.txtBase.grid(row=0, column=1, padx=10, pady=5)
        self.txtAltura = tk.Entry(root)
        self.txtAltura.grid(row=1, column=1, padx=10, pady=5)
        self.txtArea = tk.Entry(root, state="readonly")
        self.txtArea.grid(row=2, column=1, padx=10, pady=5)
        self.txtPerimetro = tk.Entry(root, state="readonly")
        self.txtPerimetro.grid(row=3, column=1, padx=10, pady=5)
        self.txtTipo = tk.Entry(root, state="readonly")
        self.txtTipo.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        tk.Button(root, text="Calcular", command=self.calcular).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=5, column=1, padx=10, pady=5)
        tk.Button(root, text="Salir", command=root.quit).grid(row=5, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            base = float(self.txtBase.get())
            altura = float(self.txtAltura.get())

            # Calcular área
            area = (base * altura) / 2

            # Calcular hipotenusa
            hipotenusa = math.sqrt(base**2 + altura**2)

            # Calcular perímetro
            perimetro = base + altura + hipotenusa

            # Determinar el tipo de triángulo
            if base == altura == hipotenusa:
                tipo = "Equilátero"
            elif base != altura and base != hipotenusa and altura != hipotenusa:
                tipo = "Escaleno"
            else:
                tipo = "Isósceles"

            # Mostrar resultados
            self.txtArea.config(state="normal")
            self.txtArea.delete(0, tk.END)
            self.txtArea.insert(0, f"{area:.2f}")
            self.txtArea.config(state="readonly")

            self.txtPerimetro.config(state="normal")
            self.txtPerimetro.delete(0, tk.END)
            self.txtPerimetro.insert(0, f"{perimetro:.2f}")
            self.txtPerimetro.config(state="readonly")

            self.txtTipo.config(state="normal")
            self.txtTipo.delete(0, tk.END)
            self.txtTipo.insert(0, tipo)
            self.txtTipo.config(state="readonly")

        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

    def limpiar(self):
        self.txtBase.delete(0, tk.END)
        self.txtAltura.delete(0, tk.END)
        self.txtArea.config(state="normal")
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state="readonly")
        self.txtPerimetro.config(state="normal")
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state="readonly")
        self.txtTipo.config(state="normal")
        self.txtTipo.delete(0, tk.END)
        self.txtTipo.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioTrianguloRectangulo(root)
    root.mainloop()