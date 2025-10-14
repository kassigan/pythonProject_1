# Менеджер задач
from datetime import datetime

class Task():

    def __init__(self, description, deadline, status='open'):
        self.description = description # описание задачи
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")  # срок выполнения
        self.status = status

# методы класса

    def add_task(self, description, deadline, status):
        task = Task(description, deadline, status)
        Task.all_tasks.append(task)

    def mark_done(self):
        self.status = "done"

    def show_open_task(self):



Task1 = Task("call police", "2025-05-01", "open")
Task2 = Task("buy milk", "2025-04-17", "done")


print(Task1.description, Task1.deadline, Task1.status)
print(Task2.description, Task2.deadline, Task2.status)

Task1.mark_done()
print(Task1.status)