import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_todo_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_todo_task = task_todo_listbox.curselection()
    selected_done_task = task_done_listbox.curselection()

    if selected_todo_task:
        task_todo_listbox.delete(selected_todo_task)
    else:
        taks_done_listbox.delete(selected_done_task)


def mark_task():
    selected_task = task_todo_listbox.curselection()
    if selected_task:
        task_todo_listbox.itemconfig(selected_task, bg="slate blue")

root = tk.Tk()
root.title("Task tracker")
root.configure(background="Hotpink")

text1 = tk.Label(root, text="Enter your task here", bg="Hotpink")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1", fg="white")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add task", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete task", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark task as done", command=mark_task)
mark_button.pack(pady=5)

# Create a frame to hold the two sections (to-do and done tasks)
frame = tk.Frame(root, bg="Hotpink")
frame.pack(pady=10)

text2 = tk.Label(frame, text="Your Tasks", bg="Hotpink")
text2.grid(row=0, column=0, padx=10)

task_todo_listbox = tk.Listbox(frame, height=10, width=30, bg="LightPink1")
task_todo_listbox.grid(row=1, column=0, padx=10, pady=5)

text3 = tk.Label(frame, text="Done Tasks", bg="Hotpink")
text3.grid(row=0, column=1, padx=10)

task_done_listbox = tk.Listbox(frame, height=10, width=30, bg="lightPink1")
task_done_listbox.grid(row=1, column=1, padx=10, pady=5)


root.mainloop()