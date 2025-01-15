import tkinter as tk
from tkinter import messagebox
import math

class FormularioCirculo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Área y Perímetro de un Círculo")

        # Etiquetas
        self.lblRadio = tk.Label(root, text="Radio del círculo:")
        self.lblRadio.grid(row=0, column=0, padx=10, pady=5)

        self.lblArea = tk.Label(root, text="Área del círculo:")
        self.lblArea.grid(row=1, column=0, padx=10, pady=5)

        self.lblPerimetro = tk.Label(root, text="Perímetro del círculo:")
        self.lblPerimetro.grid(row=2, column=0, padx=10, pady=5)

        # Campos de entrada
        self.txtRadio = tk.Entry(root)
        self.txtRadio.grid(row=0, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(root, state='readonly')
        self.txtArea.grid(row=1, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(root, state='readonly')
        self.txtPerimetro.grid(row=2, column=1, padx=10, pady=5)

        # Botones
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btnCalcular.grid(row=3, column=0, padx=10, pady=5)

        self.btnLimpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.btnLimpiar.grid(row=3, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=3, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            # Obtener el radio del círculo
            radio = float(self.txtRadio.get())

            if radio < 0:
                messagebox.showerror("Error", "El radio no puede ser negativo.")
                return

            # Calcular área y perímetro
            area = math.pi * math.pow(radio, 2)
            perimetro = 2 * math.pi * radio

            # Mostrar resultados
            self.txtArea.config(state='normal')
            self.txtArea.delete(0, tk.END)
            self.txtArea.insert(0, f"{area:.2f}")
            self.txtArea.config(state='readonly')

            self.txtPerimetro.config(state='normal')
            self.txtPerimetro.delete(0, tk.END)
            self.txtPerimetro.insert(0, f"{perimetro:.2f}")
            self.txtPerimetro.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def limpiar(self):
        # Limpiar todos los campos
        self.txtRadio.delete(0, tk.END)
        self.txtArea.config(state='normal')
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state='readonly')
        self.txtPerimetro.config(state='normal')
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioCirculo(root)
    root.mainloop()