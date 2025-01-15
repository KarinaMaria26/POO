import tkinter as tk
from tkinter import messagebox

class FormularioP18:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario Ejercicio 1")

        # Etiquetas
        self.lblNombre = tk.Label(root, text="Nombre")
        self.lblNombre.grid(row=0, column=0, padx=10, pady=5)

        self.lblCodigo = tk.Label(root, text="Código")
        self.lblCodigo.grid(row=1, column=0, padx=10, pady=5)

        self.lblHoras = tk.Label(root, text="Horas trabajadas")
        self.lblHoras.grid(row=2, column=0, padx=10, pady=5)

        self.lblValorHora = tk.Label(root, text="Valor por hora")
        self.lblValorHora.grid(row=3, column=0, padx=10, pady=5)

        self.lblRetefuente = tk.Label(root, text="Retefuente (%)")
        self.lblRetefuente.grid(row=4, column=0, padx=10, pady=5)

        self.lblSalarioBruto = tk.Label(root, text="Salario bruto")
        self.lblSalarioBruto.grid(row=5, column=0, padx=10, pady=5)

        self.lblSalarioNeto = tk.Label(root, text="Salario neto")
        self.lblSalarioNeto.grid(row=6, column=0, padx=10, pady=5)

        # Campos de texto
        self.txtNombre = tk.Entry(root)
        self.txtNombre.grid(row=0, column=1, padx=10, pady=5)

        self.txtCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=1, column=1, padx=10, pady=5)

        self.txtHoras = tk.Entry(root)
        self.txtHoras.grid(row=2, column=1, padx=10, pady=5)

        self.txtValorHora = tk.Entry(root)
        self.txtValorHora.grid(row=3, column=1, padx=10, pady=5)

        self.txtRetefuente = tk.Entry(root)
        self.txtRetefuente.grid(row=4, column=1, padx=10, pady=5)

        self.txtSalarioBruto = tk.Entry(root, state='readonly')
        self.txtSalarioBruto.grid(row=5, column=1, padx=10, pady=5)

        self.txtSalarioNeto = tk.Entry(root, state='readonly')
        self.txtSalarioNeto.grid(row=6, column=1, padx=10, pady=5)

        # Botones de acción
        self.btnCalcular = tk.Button(root, text="Calcular", command=self.calcularSalario)
        self.btnCalcular.grid(row=7, column=0, padx=10, pady=5)

        self.btnLimpiar = tk.Button(root, text="Limpiar", command=self.limpiarCampos)
        self.btnLimpiar.grid(row=7, column=1, padx=10, pady=5)

        self.btnSalir = tk.Button(root, text="Salir", command=root.quit)
        self.btnSalir.grid(row=7, column=2, padx=10, pady=5)

    def calcularSalario(self):
        try:
            # Recoger datos ingresados por el usuario
            horasTrabajadas = float(self.txtHoras.get())
            valorPorHora = float(self.txtValorHora.get())
            retefuentePorcentaje = float(self.txtRetefuente.get()) / 100

            # Realizar cálculos del salario bruto y neto
            salarioBruto = horasTrabajadas * valorPorHora
            descuentoRete = salarioBruto * retefuentePorcentaje
            salarioNeto = salarioBruto - descuentoRete

            # Mostrar resultados en los campos correspondientes
            self.txtSalarioBruto.config(state='normal')
            self.txtSalarioBruto.delete(0, tk.END)
            self.txtSalarioBruto.insert(0, f"{salarioBruto:.2f}")
            self.txtSalarioBruto.config(state='readonly')

            self.txtSalarioNeto.config(state='normal')
            self.txtSalarioNeto.delete(0, tk.END)
            self.txtSalarioNeto.insert(0, f"{salarioNeto:.2f}")
            self.txtSalarioNeto.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def limpiarCampos(self):
        # Restablecer todos los campos a valores vacíos
        self.txtNombre.delete(0, tk.END)
        self.txtCodigo.delete(0, tk.END)
        self.txtHoras.delete(0, tk.END)
        self.txtValorHora.delete(0, tk.END)
        self.txtRetefuente.delete(0, tk.END)
        self.txtSalarioBruto.config(state='normal')
        self.txtSalarioBruto.delete(0, tk.END)
        self.txtSalarioBruto.config(state='readonly')
        self.txtSalarioNeto.config(state='normal')
        self.txtSalarioNeto.delete(0, tk.END)
        self.txtSalarioNeto.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioP18(root)
    root.mainloop()