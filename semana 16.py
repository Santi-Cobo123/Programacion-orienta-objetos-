import tkinter as tk
from tkinter import messagebox, Listbox, END


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_list = Listbox(root, width=50, height=10)
        self.task_list.pack(pady=10)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            self.tasks[selected_index] += " (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def update_task_list(self):
        self.task_list.delete(0, END)
        for task in self.tasks:
            self.task_list.insert(END, task)


if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()
