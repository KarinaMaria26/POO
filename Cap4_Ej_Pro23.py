import tkinter as tk
from tkinter import messagebox
import math

class FormularioEcuacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Ejercicio 6")

        # Etiquetas
        self.lblA = tk.Label(root, text="Valor de A:")
        self.lblA.grid(row=0, column=0, padx=10, pady=5)

        self.lblB = tk.Label(root, text="Valor de B:")
        self.lblB.grid(row=1, column=0, padx=10, pady=5)

        self.lblC = tk.Label(root, text="Valor de C:")
        self.lblC.grid(row=2, column=0, padx=10, pady=5)

        self.lblSolucion1 = tk.Label(root, text="Solución 1:")
        self.lblSolucion1.grid(row=3, column=0, padx=10, pady=5)

        self.lblSolucion2 = tk.Label(root, text="Solución 2:")
        self.lblSolucion2.grid(row=4, column=0, padx=10, pady=5)

        # Campos de texto
        self.txtA = tk.Entry(root)
        self.txtA.grid(row=0, column=1, padx=10, pady=5)

        self.txtB = tk.Entry(root)
        self.txtB.grid(row=1, column=1, padx=10, pady=5)

        self.txtC = tk.Entry(root)
        self.txtC.grid(row=2, column=1, padx=10, pady=5)

        self.txtSolucion1 = tk.Entry(root, state='readonly')
        self.txtSolucion1.grid(row=3, column=1, padx=10, pady=5)

        self.txtSolucion2 = tk.Entry(root, state='readonly')
        self.txtSolucion2.grid(row=4, column=1, padx=10, pady=5)

        # Botones de acción
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcularSoluciones)
        self.btnCalcular.grid(row=5, column=0, padx=10, pady=5)

        self.btnLimpiar = tk.Button(root, text="Limpiar", command=self.limpiarCampos)
        self.btnLimpiar.grid(row=5, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=5, column=2, padx=10, pady=5)

    def calcularSoluciones(self):
        try:
            # Recoger los valores de A, B y C
            A = float(self.txtA.get())
            B = float(self.txtB.get())
            C = float(self.txtC.get())

            if A == 0:
                messagebox.showerror("Error", "El valor de A no puede ser cero en una ecuación de segundo grado.")
                return

            # Calcular el discriminante
            discriminante = B**2 - 4*A*C

            if discriminante > 0:
                # Dos soluciones reales distintas
                solucion1 = (-B + math.sqrt(discriminante)) / (2 * A)
                solucion2 = (-B - math.sqrt(discriminante)) / (2 * A)
            elif discriminante == 0:
                # Una solución real única
                solucion1 = solucion2 = -B / (2 * A)
            else:
                # Soluciones complejas
                parteReal = -B / (2 * A)
                parteImaginaria = math.sqrt(-discriminante) / (2 * A)
                solucion1 = f"{parteReal} + {parteImaginaria}i"
                solucion2 = f"{parteReal} - {parteImaginaria}i"

            # Mostrar las soluciones en los campos de texto
            self.txtSolucion1.config(state='normal')
            self.txtSolucion1.delete(0, tk.END)
            self.txtSolucion1.insert(0, str(solucion1))
            self.txtSolucion1.config(state='readonly')

            self.txtSolucion2.config(state='normal')
            self.txtSolucion2.delete(0, tk.END)
            self.txtSolucion2.insert(0, str(solucion2))
            self.txtSolucion2.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def limpiarCampos(self):
        # Limpiar todos los campos
        self.txtA.delete(0, tk.END)
        self.txtB.delete(0, tk.END)
        self.txtC.delete(0, tk.END)
        self.txtSolucion1.config(state='normal')
        self.txtSolucion1.delete(0, tk.END)
        self.txtSolucion1.config(state='readonly')
        self.txtSolucion2.config(state='normal')
        self.txtSolucion2.delete(0, tk.END)
        self.txtSolucion2.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioEcuacion(root)
    root.mainloop()