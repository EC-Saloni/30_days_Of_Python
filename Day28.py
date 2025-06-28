import json
import os

# < To-Do CLI App > - Add, delete, mark tasks- Store in a JSON or text file

file_name = "task.json"

def load_tasks():
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("JSON file is corrupted! Starting fresh.")
                return {}
    else:
        return {}

def save_tasks(tasks):
    with open("task.json","w") as file:
        json.dump(tasks,file,indent=4)

def add_task():
    tasks = load_tasks()
    key = input("Enter task name: ")
    value = input("Enter task description: ")
    tasks[key] = value
    save_tasks(tasks)
    print("Task added successfully!")


def delete_task():
    tasks = load_tasks()

    n = input("Enter key that you want to delete: ")
    if n in tasks:
        del tasks[n]
        save_tasks(tasks)
        print(f"Task '{n}' deleted. ")
    else:
        print("Task not found!")

          
def mark_tasks():
    tasks = load_tasks()
    
    key_to_update = input("Enter the key you want to mark/update : ")

    if key_to_update in tasks:
        new_value = input(f"Enter the value for {key_to_update} : ")
        tasks[key_to_update] = new_value
        save_tasks(tasks)
        print(f"Task '{key_to_update}' updated. ")
    else:
        print("Task not found!")


def display():
    tasks = load_tasks()
    if tasks:
        print("\n Your Tasks : ")
        for i, (key, value) in enumerate(tasks.items(), 1):
            print(f"{i}. {key}: {value}")
    else:
        print("No tasks found!")


# Main CLI Menu
while True:
    print("\n--- To-Do CLI App ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark/Update Task")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        mark_tasks()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
   



