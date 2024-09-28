import tkinter as tk
from tkinter import messagebox, Listbox, END

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.task_list = []

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_listbox = Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.task_listbox.bind("<Double-1>", self.complete_task)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_list.append(task)
            self.update_task_listbox()
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_list[selected_task_index]
            self.task_list[selected_task_index] = f"{task} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.task_list[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.task_list:
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
