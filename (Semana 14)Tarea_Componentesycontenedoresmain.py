
# import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
from tkinter import messagebox

class AgendaPersonal:
    def __init__(self, root):
        root.title("Agenda Personal")
        root.geometry("500x400")

        # Crear frames para organizar la interfaz
        frame_eventos = tk.Frame(root)
        frame_eventos.pack(fill="both", expand=True)

        frame_entrada = tk.Frame(root)
        frame_entrada.pack(fill="x")

        frame_acciones = tk.Frame(root)
        frame_acciones.pack(fill="x")

        # Crear TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_eventos)
        self.tree["columns"] = ("fecha", "hora", "descripcion")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("fecha", anchor=tk.W, width=100)
        self.tree.column("hora", anchor=tk.W, width=50)
        self.tree.column("descripcion", anchor=tk.W, width=200)
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("fecha", text="Fecha", anchor=tk.W)
        self.tree.heading("hora", text="Hora", anchor=tk.W)
        self.tree.heading("descripcion", text="Descripción", anchor=tk.W)
        self.tree.pack(fill="both", expand=True)

        # Crear campos de entrada para fecha, hora y descripción
        tk.Label(frame_entrada, text="Fecha:").pack(side=tk.LEFT)
        self.fecha_entrada = ttk.Combobox(frame_entrada)
        self.fecha_entrada['values'] = ['2024-01-01', '2024-01-02', '2024-01-03']
        self.fecha_entrada.pack(side=tk.LEFT)

        tk.Label(frame_entrada, text="Hora:").pack(side=tk.LEFT)
        self.hora_entrada = tk.Entry(frame_entrada)
        self.hora_entrada.pack(side=tk.LEFT)

        tk.Label(frame_entrada, text="Descripción:").pack(side=tk.LEFT)
        self.descripcion_entrada = tk.Entry(frame_entrada)
        self.descripcion_entrada.pack(side=tk.LEFT)

        # Crear botones para agregar, eliminar y salir
        tk.Button(frame_acciones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT)
        tk.Button(frame_acciones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT)
        tk.Button(frame_acciones, text="Salir", command=root.destroy).pack(side=tk.LEFT)

    def agregar_evento(self):
        fecha = self.fecha_entrada.get()
        hora = self.hora_entrada.get()
        descripcion = self.descripcion_entrada.get()
        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.fecha_entrada.set('')
        self.hora_entrada.delete(0, tk.END)
        self.descripcion_entrada.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            respuesta = messagebox.askyesno("Eliminar Evento", "¿Está seguro de eliminar el evento seleccionado?")
            if respuesta:
                self.tree.delete(seleccionado)

root = tk.Tk()
app = AgendaPersonal(root)
root.mainloop()
