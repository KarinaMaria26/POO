import tkinter as tk
from tkinter import messagebox
import math

class TrianguloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Ejercicio 2")
        
        # Etiquetas
        self.labelTitulo = tk.Label(root, text="Formulario Ejercicio 2", font=("Segoe UI", 36), anchor="center")
        self.labelTitulo.grid(row=0, column=0, columnspan=3, pady=20)

        self.labelLado = tk.Label(root, text="Lado")
        self.labelLado.grid(row=1, column=0, padx=10, pady=5)

        self.labelArea = tk.Label(root, text="Área")
        self.labelArea.grid(row=2, column=0, padx=10, pady=5)

        self.labelPerimetro = tk.Label(root, text="Perímetro")
        self.labelPerimetro.grid(row=3, column=0, padx=10, pady=5)

        self.labelAltura = tk.Label(root, text="Altura")
        self.labelAltura.grid(row=4, column=0, padx=10, pady=5)

        # Campos de entrada
        self.txtLado = tk.Entry(root)
        self.txtLado.grid(row=1, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(root, state="readonly")
        self.txtArea.grid(row=2, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(root, state="readonly")
        self.txtPerimetro.grid(row=3, column=1, padx=10, pady=5)

        self.txtAltura = tk.Entry(root, state="readonly")
        self.txtAltura.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btnCalcular.grid(row=5, column=0, padx=10, pady=20)

        self.btnBorrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.btnBorrar.grid(row=5, column=1, padx=10, pady=20)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=5, column=2, padx=10, pady=20)

    def calcular(self):
        try:
            lado = float(self.txtLado.get())
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo")

            # Crear instancia de la clase Triangulo y realizar cálculos
            triangulo = Triangulo(lado)

            # Obtener área, perímetro y altura
            area = triangulo.area()
            perimetro = triangulo.perimetro()
            altura = triangulo.altura()

            # Mostrar resultados
            self.txtArea.config(state="normal")
            self.txtArea.delete(0, tk.END)
            self.txtArea.insert(0, f"{area:.2f}")
            self.txtArea.config(state="readonly")

            self.txtPerimetro.config(state="normal")
            self.txtPerimetro.delete(0, tk.END)
            self.txtPerimetro.insert(0, f"{perimetro:.2f}")
            self.txtPerimetro.config(state="readonly")

            self.txtAltura.config(state="normal")
            self.txtAltura.delete(0, tk.END)
            self.txtAltura.insert(0, f"{altura:.2f}")
            self.txtAltura.config(state="readonly")

        except ValueError as e:
            messagebox.showerror("Error", f"Error de entrada: {e}")

    def borrar(self):
        self.txtLado.delete(0, tk.END)
        self.txtArea.config(state="normal")
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state="readonly")
        self.txtPerimetro.config(state="normal")
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state="readonly")
        self.txtAltura.config(state="normal")
        self.txtAltura.delete(0, tk.END)
        self.txtAltura.config(state="readonly")

class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Fórmula para el área de un triángulo equilátero: (lado^2 * √3) / 4
        return (self.lado ** 2 * math.sqrt(3)) / 4

    def perimetro(self):
        # Fórmula para el perímetro de un triángulo equilátero: 3 * lado
        return 3 * self.lado

    def altura(self):
        # Fórmula para la altura de un triángulo equilátero: (√3 / 2) * lado
        return (math.sqrt(3) / 2) * self.lado

if __name__ == "__main__":
    root = tk.Tk()
    app = TrianguloApp(root)
    root.mainloop()