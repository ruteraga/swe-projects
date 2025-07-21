import tkinter as tk
from tkinter import messagebox, simpledialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        self.load_tasks()
        
        # Create UI elements
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)
        
        self.refresh_listbox()
        
        # Buttons frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Complete Task", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=2, padx=5)
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")
    
    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_listbox()
    
    def complete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.tasks[selected]
            if not task.startswith("[X]"):
                self.tasks[selected] = f"[X] {task}"
                self.save_tasks()
                self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task first!")
    
    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.tasks.pop(selected)
            self.save_tasks()
            self.refresh_listbox()
            messagebox.showinfo("Deleted", f"Task '{task}' deleted!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task first!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

