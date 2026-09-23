tasks = []
while True:
    print("1. add task\n2. remove task\n3. show task\n4. mark task as done\n5. show completed tasks\n6. exit")
    choice = input("choose an option:")
    if choice == "1":
         print("add task")
         title = input("enter task: ")
         task = {
               "title": title,
               "done": False
             }
         tasks.append(task)
    elif choice == "2":
           print("remove task")
           number = int(input("enter task number"))
           number = number - 1
           del tasks[number]
    elif choice =="3":
           print("show task")
           for i, task in enumerate(tasks, start=1):
               print(i, task["title"])
    elif choice =="4":
           print("mark task as done")
           number = int(input("enter task number:"))
           number = number - 1
           tasks[number]["done"] = True
    elif choice =="5":
           print("show completed tasks")
           for i, task in enumerate(tasks, start=1):
               if task["done"] == True:
                   print(i, task["title"])
    elif choice =="6":
           print("goodbye1")
           break
    else:
           print("invalid choice, please try again.")
     