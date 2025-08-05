todo_list = []
filename = "tasks.txt"

def load_tasks():
    try:
        with open(filename, "r") as file:
            for line in file:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(task + "\n")

def show_menu():
    print("\n====== To-Do List Menu ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

load_tasks() 

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        save_tasks() 
        print("Task added.")

    elif choice == "2":
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
            try:
                remove_idx = int(input("Enter task number to remove: ")) - 1
                if 0 <= remove_idx < len(todo_list):
                    removed = todo_list.pop(remove_idx)
                    save_tasks()  
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye! 👋")
        break

    else:
        print("Invalid choice, Please enter a number from 1 to 4.")
