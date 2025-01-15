import tkinter as tk
from tkinter import messagebox

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class AplicacionCuadrado:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcular Área y Perímetro de un Cuadrado")

        # Etiquetas
        self.lblLado = tk.Label(root, text="Lado del cuadrado:")
        self.lblLado.grid(row=0, column=0, padx=10, pady=5)

        self.lblArea = tk.Label(root, text="Área:")
        self.lblArea.grid(row=1, column=0, padx=10, pady=5)

        self.lblPerimetro = tk.Label(root, text="Perímetro:")
        self.lblPerimetro.grid(row=2, column=0, padx=10, pady=5)

        # Campos de entrada
        self.txtLado = tk.Entry(root)
        self.txtLado.grid(row=0, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(root, state='readonly')
        self.txtArea.grid(row=1, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(root, state='readonly')
        self.txtPerimetro.grid(row=2, column=1, padx=10, pady=5)

        # Botones
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btnCalcular.grid(row=3, column=0, padx=10, pady=5)

        self.btnLimpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        self.btnLimpiar.grid(row=3, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=3, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            lado = float(self.txtLado.get())
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo.")

            cuadrado = Cuadrado(lado)

            # Calcular área y perímetro
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()

            # Mostrar resultados
            self.txtArea.config(state='normal')
            self.txtArea.delete(0, tk.END)
            self.txtArea.insert(0, f"{area:.2f}")
            self.txtArea.config(state='readonly')

            self.txtPerimetro.config(state='normal')
            self.txtPerimetro.delete(0, tk.END)
            self.txtPerimetro.insert(0, f"{perimetro:.2f}")
            self.txtPerimetro.config(state='readonly')

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def limpiar_campos(self):
        self.txtLado.delete(0, tk.END)
        self.txtArea.config(state='normal')
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state='readonly')
        self.txtPerimetro.config(state='normal')
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCuadrado(root)
    root.mainloop()