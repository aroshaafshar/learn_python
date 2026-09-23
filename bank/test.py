tasks = []

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Mark task as done")
    print("5. Show completed tasks")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add task")
        title = input("Enter task: ")

        task = {
            "title": title,
            "done": False
        }

        tasks.append(task)

    elif choice == "2":
        print("Remove task")
        number = int(input("Enter task number: "))
        number = number - 1
        del tasks[number]

    elif choice == "3":
        print("Show tasks")

        for i, task in enumerate(tasks, start=1):
            print(i, task["title"])

    elif choice == "4":
        print("Mark task as done")
        number = int(input("Enter task number: "))
        number = number - 1
        tasks[number]["done"] = True

    elif choice == "5":
        print("Show completed tasks")

        for i, task in enumerate(tasks, start=1):
            if task["done"] == True:
                print(i, task["title"])

    elif choice == "6":
        print("Goodbye!")
        break