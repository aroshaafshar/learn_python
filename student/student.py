students = []

# گرفتن اطلاعات دانش‌آموزها
while True:
    choice = input("1. Add student\n2. Exit\n")

    if choice == "1":
        student = {}

        student["name"] = input("Enter name: ")
        student["age"] = int(input("Enter age: "))
        student["math"] = float(input("Enter math score: "))
        student["programming"] = float(input("Enter programming score: "))
        student["english"] = float(input("Enter English score: "))

        students.append(student)

    elif choice == "2":
        break


# محاسبه میانگین و وضعیت هر دانش‌آموز
for student in students:
    student["average"] = (
        student["math"] +
        student["programming"] +
        student["english"]
    ) / 3

    if student["average"] > 18:
        student["status"] = "Excellent"

    elif (
        student["math"] > 10
        and student["programming"] > 10
        and student["english"] > 10
    ):
        student["status"] = "Pass"

    else:
        student["status"] = "Fail"


# پیدا کردن دانش‌آموز با بیشترین میانگین
top_student = students[0]

for student in students:
    if student["average"] > top_student["average"]:
        top_student = student

print("Top student:", top_student["name"])


# محاسبه میانگین کلاس
class_total = 0

for student in students:
    class_total = class_total + student["average"]

class_average = class_total / len(students)

print("Class average:", class_average)


# دانش‌آموزهای بالاتر از میانگین کلاس
print("Students above class average:")

for student in students:
    if student["average"] > class_average:
        print(student["name"])


# تغییر نمره یک دانش‌آموز
name = input("Enter student name: ")

for student in students:
    if student["name"] == name:

        score = input("Which score do you want to change? ")
        new_score = float(input("Enter new score: "))

        if score == "math":
            student["math"] = new_score

        elif score == "programming":
            student["programming"] = new_score

        elif score == "english":
            student["english"] = new_score

        # محاسبه دوباره میانگین
        student["average"] = (
            student["math"] +
            student["programming"] +
            student["english"]
        ) / 3

        # محاسبه دوباره وضعیت
        if student["average"] > 18:
            student["status"] = "Excellent"

        elif (
            student["math"] > 10
            and student["programming"] > 10
            and student["english"] > 10
        ):
            student["status"] = "Pass"

        else:
            student["status"] = "Fail"

        print("Updated average:", student["average"])
        print("Updated status:", student["status"])