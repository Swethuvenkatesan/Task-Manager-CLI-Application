import json
import os

# class for task
class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = " Completed ✅ " if self.completed else " Not Completed❌ "
        return f"Task {self.id}: {self.title} [{status}]"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available 📭 ")
        else:
            for task in self.tasks:
                print(task)

    def delete_task(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {task_id} deleted ✅ ")
        else:
            print(f"Task {task_id} not found ❌")

    def mark_task_complete(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.completed = True
            self.save_tasks()
            print(f"Task {task_id} marked as completed ✅")
        else:
            print(f"Task {task_id} not found ❌")
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            tasks_dict = [task.__dict__ for task in self.tasks]
            json.dump(tasks_dict, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                tasks_list = json.load(file)
                self.tasks = [Task(t['id'], t['title'], t['completed']) for t in tasks_list]
        else:
            self.tasks = []

# for login
def login():
    print("Please login to the Task Manager")
    email = input("Enter the Email: ")
    password = input("Enter the Password: ")

    # Dummy credentials for login
    if email == "demo@gmail.com" and password == "Taskmanager@Demo":
        print(" Login successful ✅")
        return True
    else:
        print(" Invalid. Please check and try again ❌")
        return False


def main():

    if not login(): 
         return

    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add a task ➕")
        print("2. View tasks 📋")
        print("3. Delete a task 🗑️ ")
        print("4. Mark task as complete ✅")
        print("5. Exit ➡️")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the task title: ")
            manager.add_task(title)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to mark as complete: "))
            manager.mark_task_complete(task_id)
        elif choice == '5':
            print("Exiting the application.GoodBye!👋")
            break
        else:
            print("Invalid choice. Please check and try again 🔄")

if __name__ == "__main__":
    main()
