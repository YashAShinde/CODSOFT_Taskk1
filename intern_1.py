import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {"tasks": []}
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks["tasks"], 1):
            print(f"{idx}. {task['title']} - {task['date']}")

def add_task(tasks):
    title = input("Enter task title: ")
    date_str = input("Enter task due date (YYYY-MM-DD): ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks["tasks"].append({"title": title, "date": date})
    print("Task added successfully.")

def update_task(tasks):
    show_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1

    if 0 <= task_index < len(tasks["tasks"]):
        new_title = input("Enter new task title (press enter to keep the same): ")
        new_date_str = input("Enter new due date (YYYY-MM-DD) (press enter to keep the same): ")

        if new_title:
            tasks["tasks"][task_index]["title"] = new_title

        if new_date_str:
            try:
                new_date = datetime.strptime(new_date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
                tasks["tasks"][task_index]["date"] = new_date
            except ValueError:
                print("Invalid date format. Task not updated.")
                return

        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
