class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the To-Do List.")

    def view_tasks(self):
        if not self.tasks:
            print("To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def delete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            deleted_task = self.tasks.pop(task_idx - 1)
            print(f"Task '{deleted_task}' deleted from the To-Do List.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_idx = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_idx)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
