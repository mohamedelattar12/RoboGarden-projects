import os
def load_tasks(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                tasks = file.readlines()
                return [task.strip() for task in tasks]
        else:
            return []  
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(file_name, tasks):
    try:
        with open(file_name, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    task = input("Enter a new task: ")
    if task.strip():
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Error removing task: {e}")

def view_tasks(tasks):
    if tasks:
        print("\nYour Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour task list is empty.")

def main():
    file_name = "task_list.txt"
    tasks = load_tasks(file_name)

    while True:
        print("\nTask List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(file_name, tasks)
            print("Tasks saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
