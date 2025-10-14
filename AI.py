from datetime import datetime

class Task:
    all_tasks = []  # список для хранения всех задач

    def __init__(self, description, deadline, status='open'):
        self.description = description  # описание задачи
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")  # срок выполнения
        self.status = status
        Task.all_tasks.append(self)  # добавляем задачу в общий список при создании

    def add_task(self, description, deadline, status='open'):
        new_task = Task(description, deadline, status)
        return new_task

    def mark_done(self):
        self.status = "done"

    def show_open_task(self):
        print("Открытые задачи:")
        for task in Task.all_tasks:
            if task.status == "open":
                print(f"- {task.description} (до {task.deadline.date()})")

    def show_all_tasks(self):
        print("Все задачи:")
        for task in Task.all_tasks:
            print(f"- {task.description} (до {task.deadline.date()}), статус: {task.status}")

Task1 = ("make dinner", "2025-01-05", "open")
Task2 = ("wash the dish", "2025-01-06", "open")

print(Task.all_tasks)
