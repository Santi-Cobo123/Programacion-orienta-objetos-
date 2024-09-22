import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class EventScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Programador de Eventos")

        # Frame para la visualización de eventos
        self.frame_events = ttk.Frame(self.root)
        self.frame_events.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_events, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=10)

        self.label_date = ttk.Label(self.frame_input, text="Fecha:")
        self.label_date.grid(row=0, column=0)
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1)

        self.label_time = ttk.Label(self.frame_input, text="Hora:")
        self.label_time.grid(row=1, column=0)
        self.entry_time = ttk.Entry(self.frame_input)
        self.entry_time.grid(row=1, column=1)

        self.label_description = ttk.Label(self.frame_input, text="Descripción:")
        self.label_description.grid(row=2, column=0)
        self.entry_description = ttk.Entry(self.frame_input)
        self.entry_description.grid(row=2, column=1)

        # Botones
        self.button_add = ttk.Button(self.root, text="Agregar Evento", command=self.add_event)
        self.button_add.pack(pady=5)

        self.button_delete = ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.button_delete.pack(pady=5)

        self.button_exit = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.button_exit.pack(pady=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.entry_time.get()
        description = self.entry_description.get()

        if date and time and description:
            self.tree.insert("", "end", values=(date, time, description))
            self.entry_time.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            if messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?"):
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventScheduler(root)
    root.mainloop()
