# ============================================================
# PROJECT 7 - TODO MANAGER
# ============================================================

"""
Build a Todo management application.

Each task should contain at least:

- Task ID
- Title
- Description
- Priority
- Status

Example:

    ID: 12
    Title: Learn Python
    Priority: High
    Status: Pending

Menu:

1. Add Task
2. Complete Task
3. Delete Task
4. Show All Tasks
5. Show Completed Tasks
6. Show Pending Tasks
7. Search Tasks
8. Filter By Priority
9. Exit

Requirements:

- Add tasks.
- Complete tasks.
- Delete tasks.
- Search tasks.
- Filter by priority.
- Show completed tasks.
- Show pending tasks.
- Search using partial text.

The application should support at least:

    High
    Medium
    Low

The program should not allow an invalid priority or status.

Persistence requirement:

All tasks must be stored in a file.

Closing and reopening the application must preserve all tasks
and their current statuses.
"""
import json

FILENAME = "todo.json"

try:
     with open(FILENAME, "r") as file:
         tasks = json.load(file)
except FileNotFoundError:
     tasks = []

def save_tasks():
     with open(FILENAME, "w") as file:
         json.dump(tasks, file, indent=4)

class task:
     def __init__(self, id, title, description, priority, status):
         self.id = id
         self.title = title
         self.description = description
         self.priority = priority
         self.status = status
         
def add_task():
    title = input("Title: ")
    description = input("Description: ")

    while True:
        priority = input("Priority: ")

        if priority == "High" or priority == "Medium" or priority == "Low":
         break

        else:
            print("Invalid priority!")
            

    status = "Pending"

    if tasks:
         task_id = max(task["id"] for task in tasks) + 1
    else:
         task_id = 1

    new_task = task(
        task_id,
        title,
        description,
        priority,
        status
     )
    tasks.append(new_task.__dict__)
    save_tasks()
    print("task added.")

def complte_task():
     task_id = int(input("Task ID: "))
     for task in tasks:
         if task["id"] == task_id:
             task["status"] = "Completed"
             save_tasks()
             print("Task completed!")
             return
     print("Task not found!")

def delete_task():
     task_id = int(input("Task ID: "))
     for task in tasks:
         if task["id"] == task_id:
             tasks.remove(task)
             save_tasks()
             print("Task deleted!")
             return
     print("Task not found!")

def show_all_tasks():
     if not tasks:
         print("No tasks!")
         return
     for task in tasks:
         print("----------------")
         print("ID:",  task["id"])
         print("Title:",  task["title"])
         print("Description:", task["description"])
         print("Priority:", task["priority"])
         print("Status:", task["status"])

def show_completed_tasks():
     for task in tasks:
         if task["status"] == "completded":
             print("----------------")
             print("ID:",  task["id"])
             print("Title:",  task["title"])
             print("Description:", task["description"])
             print("Priority:", task["priority"])
             print("Status:", task["status"])

def show_pending_tasks():
     for task in tasks:
         if task["status"] == "pending":
             print("----------------")
             print("ID:",  task["id"])
             print("Title:",  task["title"])
             print("Description:", task["description"])
             print("Priority:", task["priority"])
             print("Status:", task["status"])

def search_tasks():
     search = input("Search: ").lower()
     for task in tasks:
         if search in task["title"].lower() or search in task["description"].lower():
             print("----------------")
             print("ID:",  task["id"])
             print("Title:",  task["title"])
             print("Description:", task["description"])
             print("Priority:", task["priority"])
             print("Status:", task["status"])

def filter_by_priority():
     priority = input("Priority (High/Medium/Low): ")
     if priority != "High" and priority != "Medium" and priority != "Low":
         print("Invalid priority!")
         return
     for task in tasks:
         if task["priority"] == priority:
             print("----------------")
             print("ID:",  task["id"])
             print("Title:",  task["title"])
             print("Description:", task["description"])
             print("Priority:", task["priority"])
             print("Status:", task["status"])

while True:
     print("1. add task\n2. complete task\n3. delete task\n4. show all tasks\n5. show completed tasks\n6. show pending tasks\n7. search tasks\n8. filter by priority\n9. exit")

     choice = input("choose: ")
     if choice == "1":
         add_task()

     if choice == "2":
         complte_task()

     if choice == "3":
         delete_task()

     if choice == "4":
         show_all_tasks()

     if choice == "5":
         show_completed_tasks()

     if choice == "6":
         show_pending_tasks()

     if choice == "7":
         search_tasks()

     if choice == "8":
         filter_by_priority()

     if choice == "9":
         print("Goodbye!")
         break

     