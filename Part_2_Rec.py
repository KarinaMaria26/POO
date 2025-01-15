import tkinter as tk
from tkinter import messagebox

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class FormularioRectangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Rectángulo")

        # Etiquetas
        self.lblBase = tk.Label(root, text="Base")
        self.lblBase.grid(row=0, column=0, padx=10, pady=5)

        self.lblAltura = tk.Label(root, text="Altura")
        self.lblAltura.grid(row=1, column=0, padx=10, pady=5)

        self.lblArea = tk.Label(root, text="Área")
        self.lblArea.grid(row=2, column=0, padx=10, pady=5)

        self.lblPerimetro = tk.Label(root, text="Perímetro")
        self.lblPerimetro.grid(row=3, column=0, padx=10, pady=5)

        # Campos de texto
        self.txtBase = tk.Entry(root)
        self.txtBase.grid(row=0, column=1, padx=10, pady=5)

        self.txtAltura = tk.Entry(root)
        self.txtAltura.grid(row=1, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(root, state='readonly')
        self.txtArea.grid(row=2, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(root, state='readonly')
        self.txtPerimetro.grid(row=3, column=1, padx=10, pady=5)

        # Botones de acción
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btnCalcular.grid(row=4, column=0, padx=10, pady=5)

        self.btnLimpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        self.btnLimpiar.grid(row=4, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=4, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            # Obtener valores de los campos
            base = float(self.txtBase.get())
            altura = float(self.txtAltura.get())

            # Crear instancia de la clase Rectangulo
            rectangulo = Rectangulo(base, altura)

            # Calcular área y perímetro
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()

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
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def limpiar_campos(self):
        # Limpiar todos los campos
        self.txtBase.delete(0, tk.END)
        self.txtAltura.delete(0, tk.END)
        self.txtArea.config(state='normal')
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state='readonly')
        self.txtPerimetro.config(state='normal')
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioRectangulo(root)
    root.mainloop()