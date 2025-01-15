import tkinter as tk
from tkinter import messagebox

class CalculoMatricula:
    def __init__(self, valor_patrimonio, nivel_estrato):
        self.valor_patrimonio = valor_patrimonio
        self.nivel_estrato = nivel_estrato
        self.valor_matricula = 50000

    def calcular_matricula(self):
        if self.valor_patrimonio > 2000000 and self.nivel_estrato > 3:
            self.valor_matricula += 0.03 * self.valor_patrimonio
        return self.valor_matricula


class VentanaPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Cálculo de Matrícula")

        # Crear los widgets
        self.etiqueta_titulo = tk.Label(raiz, text="Cálculo de Matrícula", font=("Segoe UI", 24))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.etiqueta_nombres = tk.Label(raiz, text="Nombre Completo:")
        self.etiqueta_nombres.grid(row=1, column=0)

        self.etiqueta_num_inscripcion = tk.Label(raiz, text="Número de Inscripción:")
        self.etiqueta_num_inscripcion.grid(row=2, column=0)

        self.etiqueta_estrato = tk.Label(raiz, text="Estrato Social:")
        self.etiqueta_estrato.grid(row=3, column=0)

        self.etiqueta_patrimonio = tk.Label(raiz, text="Valor del Patrimonio:")
        self.etiqueta_patrimonio.grid(row=4, column=0)

        self.etiqueta_resultado_nombres = tk.Label(raiz, text="Nombre Registrado:")
        self.etiqueta_resultado_nombres.grid(row=5, column=0)

        self.etiqueta_resultado_inscripcion = tk.Label(raiz, text="Inscripción Registrada:")
        self.etiqueta_resultado_inscripcion.grid(row=6, column=0)

        self.etiqueta_resultado_pago = tk.Label(raiz, text="Pago Total Matrícula:")
        self.etiqueta_resultado_pago.grid(row=7, column=0)

        self.campo_inscripcion = tk.Entry(raiz)
        self.campo_inscripcion.grid(row=2, column=1)

        self.campo_nombres = tk.Entry(raiz)
        self.campo_nombres.grid(row=1, column=1)

        self.campo_patrimonio = tk.Entry(raiz)
        self.campo_patrimonio.grid(row=4, column=1)

        self.campo_estrato = tk.Entry(raiz)
        self.campo_estrato.grid(row=3, column=1)

        self.campo_resultado_inscripcion = tk.Entry(raiz)
        self.campo_resultado_inscripcion.grid(row=6, column=1)
        self.campo_resultado_inscripcion.config(state=tk.DISABLED)

        self.campo_resultado_nombres = tk.Entry(raiz)
        self.campo_resultado_nombres.grid(row=5, column=1)
        self.campo_resultado_nombres.config(state=tk.DISABLED)

        self.campo_resultado_pago = tk.Entry(raiz)
        self.campo_resultado_pago.grid(row=7, column=1)
        self.campo_resultado_pago.config(state=tk.DISABLED)

        self.boton_calcular = tk.Button(raiz, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=8, column=0, columnspan=2, pady=10)

        self.boton_borrar = tk.Button(raiz, text="Borrar", command=self.borrar)
        self.boton_borrar.grid(row=9, column=0, columnspan=2)

        self.boton_salir = tk.Button(raiz, text="Salir", command=raiz.quit)
        self.boton_salir.grid(row=10, column=0, columnspan=2)

    def calcular(self):
        try:
            numero_inscripcion = self.campo_inscripcion.get()
            nombre_completo = self.campo_nombres.get()
            valor_patrimonio = float(self.campo_patrimonio.get())
            nivel_estrato = float(self.campo_estrato.get())

            # Crear la instancia de la clase de cálculo
            calculo = CalculoMatricula(valor_patrimonio, nivel_estrato)
            valor_pago = calculo.calcular_matricula()

            # Mostrar los resultados
            self.campo_resultado_inscripcion.config(state=tk.NORMAL)
            self.campo_resultado_inscripcion.delete(0, tk.END)
            self.campo_resultado_inscripcion.insert(0, numero_inscripcion)

            self.campo_resultado_nombres.config(state=tk.NORMAL)
            self.campo_resultado_nombres.delete(0, tk.END)
            self.campo_resultado_nombres.insert(0, nombre_completo)

            self.campo_resultado_pago.config(state=tk.NORMAL)
            self.campo_resultado_pago.delete(0, tk.END)
            self.campo_resultado_pago.insert(0, f"${valor_pago:,.2f}")

            # Deshabilitar los campos de resultado
            self.campo_resultado_inscripcion.config(state=tk.DISABLED)
            self.campo_resultado_nombres.config(state=tk.DISABLED)
            self.campo_resultado_pago.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")

    def borrar(self):
        self.campo_inscripcion.delete(0, tk.END)
        self.campo_nombres.delete(0, tk.END)
        self.campo_patrimonio.delete(0, tk.END)
        self.campo_estrato.delete(0, tk.END)
        self.campo_resultado_inscripcion.config(state=tk.NORMAL)
        self.campo_resultado_inscripcion.delete(0, tk.END)
        self.campo_resultado_nombres.config(state=tk.NORMAL)
        self.campo_resultado_nombres.delete(0, tk.END)
        self.campo_resultado_pago.config(state=tk.NORMAL)
        self.campo_resultado_pago.delete(0, tk.END)
        self.campo_resultado_inscripcion.config(state=tk.DISABLED)
        self.campo_resultado_nombres.config(state=tk.DISABLED)
        self.campo_resultado_pago.config(state=tk.DISABLED)


# Crear la ventana principal
raiz = tk.Tk()

# Crear la interfaz
interfaz = VentanaPrincipal(raiz)

# Ejecutar la aplicación
raiz.mainloop()