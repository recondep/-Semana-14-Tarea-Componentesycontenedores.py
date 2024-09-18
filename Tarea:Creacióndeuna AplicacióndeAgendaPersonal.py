# import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x600")

        # Crear contenedores
        self.container_principal = tk.Frame(self.root)
        self.container_principal.pack(fill="both", expand=True)

        self.container_eventos = tk.Frame(self.container_principal)
        self.container_eventos.pack(fill="both", expand=True)

        self.container_entrada = tk.Frame(self.container_principal)
        self.container_entrada.pack(fill="x")

        self.container_acciones = tk.Frame(self.container_principal)
        self.container_acciones.pack(fill="x")

        # Crear lista de eventos
        self.lista_eventos = ttk.Treeview(self.container_eventos)
        self.lista_eventos["columns"] = ("Fecha", "Hora", "Descripción")
        self.lista_eventos.column("#0", width=0, stretch=tk.NO)
        self.lista_eventos.column("Fecha", anchor=tk.W, width=100)
        self.lista_eventos.column("Hora", anchor=tk.W, width=50)
        self.lista_eventos.column("Descripción", anchor=tk.W, width=200)
        self.lista_eventos.heading("#0", text="", anchor=tk.W)
        self.lista_eventos.heading("Fecha", text="Fecha", anchor=tk.W)
        self.lista_eventos.heading("Hora", text="Hora", anchor=tk.W)
        self.lista_eventos.heading("Descripción", text="Descripción", anchor=tk.W)
        self.lista_eventos.pack(fill="both", expand=True)

        # Crear campos de entrada
        self.etiqueta_fecha = tk.Label(self.container_entrada, text="Fecha:")
        self.etiqueta_fecha.pack(side=tk.LEFT)
        self.entrada_fecha = tk.Entry(self.container_entrada, width=10)
        self.entrada_fecha.pack(side=tk.LEFT)

        self.etiqueta_hora = tk.Label(self.container_entrada, text="Hora:")
        self.etiqueta_hora.pack(side=tk.LEFT)
        self.entrada_hora = tk.Entry(self.container_entrada, width=5)
        self.entrada_hora.pack(side=tk.LEFT)

        self.etiqueta_descripcion = tk.Label(self.container_entrada, text="Descripción:")
        self.etiqueta_descripcion.pack(side=tk.LEFT)
        self.entrada_descripcion = tk.Entry(self.container_entrada, width=20)
        self.entrada_descripcion.pack(side=tk.LEFT)

        # Crear botones
        self.boton_agregar = tk.Button(self.container_acciones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(side=tk.LEFT)

        self.boton_eliminar = tk.Button(self.container_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(side=tk.LEFT)

        self.boton_salir = tk.Button(self.container_acciones, text="Salir", command=self.root.destroy)
        self.boton_salir.pack(side=tk.LEFT)

    def agregar_evento(self):
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()
        self.lista_eventos.insert("", "end", values=(fecha, hora, descripcion))
        self.entrada_fecha.delete(0, tk.END)
        self.entrada_hora.delete(0, tk.END)
        self.entrada_descripcion.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.lista_eventos.selection()
        if seleccionado:
            self.lista_eventos.delete(seleccionado)
        else:
            messagebox.showinfo("Error", "No hay evento seleccionado")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
