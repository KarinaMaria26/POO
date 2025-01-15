import tkinter as tk
from tkinter import messagebox

class CalculoSalario:
    def __init__(self, salario_por_hora, horas_trabajadas):
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

class VentanaPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Formulario Ejercicio 5")

        # Crear los widgets
        self.etiqueta_titulo = tk.Label(raiz, text = "Formulario Ejercicio 5", font=("Segoe UI", 24))
        self.etiqueta_titulo.grid(row = 0, column = 0, columnspan=2, pady=10)

        self.etiqueta_nombre_empleado = tk.Label(raiz, text="Nombre del Empleado:")
        self.etiqueta_nombre_empleado.grid(row=1, column=0)

        self.etiqueta_salario_por_hora = tk.Label(raiz, text="Salario Básico por Hora:")
        self.etiqueta_salario_por_hora.grid(row=2, column=0)

        self.etiqueta_horas_trabajadas = tk.Label(raiz, text="Horas Trabajadas en el Mes:")
        self.etiqueta_horas_trabajadas.grid(row=3, column=0)

        self.etiqueta_resultado_nombre = tk.Label(raiz, text="Nombre Registrado:")
        self.etiqueta_resultado_nombre.grid(row=4, column=0)

        self.etiqueta_resultado_salario = tk.Label(raiz, text="Salario Mensual:")
        self.etiqueta_resultado_salario.grid(row=5, column=0)

        self.campo_nombre_empleado = tk.Entry(raiz)
        self.campo_nombre_empleado.grid(row=1, column=1)

        self.campo_salario_por_hora = tk.Entry(raiz)
        self.campo_salario_por_hora.grid(row=2, column=1)

        self.campo_horas_trabajadas = tk.Entry(raiz)
        self.campo_horas_trabajadas.grid(row=3, column=1)

        self.campo_resultado_nombre = tk.Entry(raiz)
        self.campo_resultado_nombre.grid(row=4, column=1)
        self.campo_resultado_nombre.config(state=tk.DISABLED)

        self.campo_resultado_salario = tk.Entry(raiz)
        self.campo_resultado_salario.grid(row=5, column=1)
        self.campo_resultado_salario.config(state=tk.DISABLED)

        self.boton_calcular = tk.Button(raiz, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=6, column=0, columnspan=2, pady=10)

        self.boton_borrar = tk.Button(raiz, text="Borrar", command=self.borrar)
        self.boton_borrar.grid(row=7, column=0, columnspan=2)

        self.boton_salir = tk.Button(raiz, text="Salir", command=raiz.quit)
        self.boton_salir.grid(row=8, column=0, columnspan=2)

    def calcular(self):
        try:
            nombre_empleado = self.campo_nombre_empleado.get()
            salario_por_hora = float(self.campo_salario_por_hora.get())
            horas_trabajadas = float(self.campo_horas_trabajadas.get())

            # Crear la instancia de la clase de cálculo
            calculo = CalculoSalario(salario_por_hora, horas_trabajadas)
            salario_mensual = calculo.calcular_salario_mensual()

            # Mostrar los resultados según las condiciones
            self.campo_resultado_nombre.config(state=tk.NORMAL)
            self.campo_resultado_nombre.delete(0, tk.END)
            self.campo_resultado_nombre.insert(0, nombre_empleado)

            if salario_mensual > 450000:
                self.campo_resultado_salario.config(state=tk.NORMAL)
                self.campo_resultado_salario.delete(0, tk.END)
                self.campo_resultado_salario.insert(0, f"${salario_mensual:,.2f}")
                self.campo_resultado_salario.config(state=tk.DISABLED)
            else:
                self.campo_resultado_salario.config(state=tk.NORMAL)
                self.campo_resultado_salario.delete(0, tk.END)
                self.campo_resultado_salario.insert(0, "No aplica")
                self.campo_resultado_salario.config(state=tk.DISABLED)

            self.campo_resultado_nombre.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")

    def borrar(self):
        self.campo_nombre_empleado.delete(0, tk.END)
        self.campo_salario_por_hora.delete(0, tk.END)
        self.campo_horas_trabajadas.delete(0, tk.END)
        self.campo_resultado_nombre.config(state=tk.NORMAL)
        self.campo_resultado_nombre.delete(0, tk.END)
        self.campo_resultado_salario.config(state=tk.NORMAL)
        self.campo_resultado_salario.delete(0, tk.END)
        self.campo_resultado_nombre.config(state=tk.DISABLED)
        self.campo_resultado_salario.config(state=tk.DISABLED)

# Crear la ventana principal
raiz = tk.Tk()

# Crear la interfaz
interfaz = VentanaPrincipal(raiz)

# Ejecutar la aplicación
raiz.mainloop()
