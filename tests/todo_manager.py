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

    new_task = Task(
        task_id,
        title,
        description,
        priority,
        status
    )

    tasks.append(new_task.__dict__)
    save_tasks()

