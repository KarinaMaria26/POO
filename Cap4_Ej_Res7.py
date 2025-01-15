import tkinter as tk
from tkinter import messagebox

class ComparadorNumeros:
    def __init__(self, numero_a, numero_b):
        self.numero_a = numero_a
        self.numero_b = numero_b
    
    def obtener_mayor(self):
        if self.numero_a > self.numero_b:
            return self.numero_a
        else:
            return self.numero_b
    
    def obtener_menor(self):
        if self.numero_a < self.numero_b:
            return self.numero_a
        else:
            return self.numero_b


class InterfazNumeros:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario Ejercicio 3")

        # Crear los widgets
        self.etiqueta_titulo = tk.Label(ventana, text="Formulario Ejercicio 3", font=("Segoe UI", 24))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.etiqueta_numero_a = tk.Label(ventana, text="Número A:")
        self.etiqueta_numero_a.grid(row=1, column=0)

        self.etiqueta_numero_b = tk.Label(ventana, text="Número B:")
        self.etiqueta_numero_b.grid(row=2, column=0)

        self.entrada_numero_a = tk.Entry(ventana)
        self.entrada_numero_a.grid(row=1, column=1)

        self.entrada_numero_b = tk.Entry(ventana)
        self.entrada_numero_b.grid(row=2, column=1)

        self.etiqueta_mayor = tk.Label(ventana, text="El número mayor es:")
        self.etiqueta_mayor.grid(row=3, column=0)

        self.entrada_mayor = tk.Entry(ventana)
        self.entrada_mayor.grid(row=3, column=1)
        self.entrada_mayor.config(state=tk.DISABLED)

        self.etiqueta_menor = tk.Label(ventana, text="El número menor es:")
        self.etiqueta_menor.grid(row=4, column=0)

        self.entrada_menor = tk.Entry(ventana)
        self.entrada_menor.grid(row=4, column=1)
        self.entrada_menor.config(state=tk.DISABLED)

        self.boton_calcular = tk.Button(ventana, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=5, column=0, columnspan=3, pady=10)

        self.boton_borrar = tk.Button(ventana, text="Borrar", command=self.borrar)
        self.boton_borrar.grid(row=6, column=0, columnspan=3)

        self.boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
        self.boton_salir.grid(row=7, column=0, columnspan=3)

    def calcular(self):
        try:
            numero_a = float(self.entrada_numero_a.get())
            numero_b = float(self.entrada_numero_b.get())

            comparador = ComparadorNumeros(numero_a, numero_b)

            mayor = comparador.obtener_mayor()
            menor = comparador.obtener_menor()

            # Mostrar resultados
            self.entrada_mayor.config(state=tk.NORMAL)
            self.entrada_mayor.delete(0, tk.END)
            self.entrada_mayor.insert(0, mayor)

            self.entrada_menor.config(state=tk.NORMAL)
            self.entrada_menor.delete(0, tk.END)
            self.entrada_menor.insert(0, menor)

            self.entrada_mayor.config(state=tk.DISABLED)
            self.entrada_menor.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")

    def borrar(self):
        self.entrada_numero_a.delete(0, tk.END)
        self.entrada_numero_b.delete(0, tk.END)
        self.entrada_mayor.config(state=tk.NORMAL)
        self.entrada_mayor.delete(0, tk.END)
        self.entrada_mayor.config(state=tk.DISABLED)
        self.entrada_menor.config(state=tk.NORMAL)
        self.entrada_menor.delete(0, tk.END)
        self.entrada_menor.config(state=tk.DISABLED)


# Crear la ventana principal
ventana_principal = tk.Tk()

# Crear la interfaz
interfaz_numeros = InterfazNumeros(ventana_principal)

# Ejecutar la aplicación
ventana_principal.mainloop()