import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✗"
            print(f"{i}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)

        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
