import json
import os
import tkinter as tk
from tkinter import messagebox

TODO_FILE = 'todo_list_gui.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task():
    task = entry.get()
    if task:
        tasks.append({'task': task, 'completed': False})
        save_tasks(tasks)
        entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def refresh_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task['completed'] else "Pending"
        listbox.insert(tk.END, f"{task['task']} - {status}")

def complete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]['completed'] = True
        save_tasks(tasks)
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks[index]
        save_tasks(tasks)
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

tasks = load_tasks()

app = tk.Tk()
app.title("To-Do List")

frame = tk.Frame(app)
frame.pack(pady=10)

entry = tk.Entry(frame, width=30)
entry.pack(side=tk.LEFT, padx=10)
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

complete_button = tk.Button(app, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=10)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT)

refresh_tasks()

app.mainloop()
