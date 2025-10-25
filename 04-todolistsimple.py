import sys

def main():
    
    tasks = {}
    task_id = 0

    while True:
        user = input("Input values: \n 1. Add Task \n 2. Edit Task \n 3. Delete Task \n 4. Exit")
        if user == "1":
            task_id += 1
            add = input("Enter new task: ")
            tasks[task_id] = add
            print("task added successfully.")
            print(tasks)
            continue
        if user =="2":
            num = int(input("What task do you want to edit?"))
            edit = input("Enter new task: ")
            tasks[num] = edit
            print(tasks)
            continue
        if user == "3":
            delete = int(input("Which task would you like to delete good sir?"))
            del tasks[delete]
            print("task {delete} deleted.")
        if user == "4":
            sys.exit()
            



main()
