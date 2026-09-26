import json
students = {
}
FILE_NAME = "student.json"
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
        students = {int(student_id): student for student_id, student in students.items()}
except FileNotFoundError:
    students = {}
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
while True:
    print("1. add student\n2. add grade\n3. update grade\n4. show student report\n5. show all students\n6. find best student\7. delete student\8. exit")
    choice = input("enter your choice: ")
    if choice == "1":
        while True:
            try:
              student_id = int(input("enter student ID: "))
              break
            except ValueError:
                print("please enter a number.")
        while student_id in students:
            print("student ID already exists.")
            student_id = int(input("enter another student ID: "))
        name = input("enter student name: ")
        while True:
            try:
             age = int(input("enter student age: "))
             if age > 0:
                 break
             print("age must be graeter than 0.")
            except ValueError:
                print("please enter a number")
        students[student_id] = {
            "name": name,
            "age": age,
            "grades": {}
        }
        print("student addes successfully!")
        save_students()
    elif choice == "2":
        student_id = int(input("enter student ID: "))
        if student_id not in students:
            print("student not found.")
        else:
            subject = input("enter subject name:")
            while True:
                try:
                    grade = float(input("enter grade: "))
                    if 0 <= grade <= 20:
                        break
                    print("grade must be between 0 and 20.")
                except ValueError:
                    print("please enter a number.")
            students[student_id]["grades"][subject] = grade
            print("grade added successfully!")
            save_students()
    elif choice == "3":
        student_id = int(input("enter student ID: "))
        if student_id not in students:
            print("student not found.")
        else:
            subject = input("enter subject name:")
            if subject not in students[student_id]["grades"]:
                print("subject not found.")
            else:
                while True:
                    try:
                        grade = float(input("enter new grade: "))
                        if 0 <= grade <= 20:
                            break
                        print("grade must be between 0 and 20.")
                    except ValueError:
                        print("please enter a number.")
                students[student_id]["grades"][subject] = grade
                print("grade update successfully!")
                save_students()
    elif choice == "4":
        student_id = int(input("enter student ID: "))
        if student_id not in students:
            print("student not found.")
        else:
            student = students[student_id]
            print("student ID:", student_id)
            print("name:", student["name"])
            print("age:", student["age"])
            for subject, grade in student["grades"].items():
                print(subject, ":", grade)

            if student["grades"]:
               average = sum(student["grades"].values()) / len(student["grades"])
               print("average:", average)
            else:
                print("no grades yet.")
    elif choice == "5":
        for student_id, student in students.items():
            print("ID:", student_id)
            print("name:", student["name"])
            print("age:", student["age"])
            print("grades:", student["grades"])
            print("_______________")
    elif choice == "6":
        best_student = None
        for student_id, student in students.items():
            if student["grades"]:
                average = sum(student["grades"].values()) / len(student["grades"])
                if best_student is None or average > best_student[1]:
                    best_student = (student_id, average)
        if best_student:
            print("best student ID:", best_student[0])
            print("average:", best_student[1])
        else:
            print("no student with grades.")
    elif choice == "7":
        student_id = int(input("enter student ID: "))
        if student_id not in students:
            print("student not found.")
        else:
            del students[student_id]
            print("student deleted successfully!")
            save_students()
    elif choice == "8":
        break
    else:
        print("invalid choice")