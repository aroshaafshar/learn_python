# ============================================================
# PROJECT 10 - EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

"""
Build an employee management system.

Each employee should contain at least:

- Employee ID
- Name
- Age
- Department
- Salary
- Skills

Menu: 

1. Add Employee
2. Remove Employee
3. Update Employee
4. Search Employee
5. Show All Employees
6. Department Report
7. Salary Report
8. Exit

Requirements:

- Add employees.
- Remove employees.
- Update employee information.
- Search employees.
- Search by name.
- Search by department.
- Display all employees.
- Calculate average salary.
- Display department statistics.

Example:

    Backend
    Employees: 5
    Average Salary: 42,000,000

    Frontend
    Employees: 3
    Average Salary: 35,000,000

Search should support partial names.

For example:

    Search: ali

Could find:

    Ali Ahmadi
    Alireza Mohammadi

Persistence requirement:

All employees and their latest information must be stored
and loaded when the application starts.
"""
import json

FILE_NAME = "employee.json"

try:
     with open(FILE_NAME, "r") as file:
         employees = json.load(file)
except FileNotFoundError:
     employees = []


while True:
     print(""" 
     1. Add employee
     2. Remove employee
     3. Update employee
     4. Search employee
     5. Show all employees
     6. Department report
     7. Salary report
     8. Exit
     """)
     choice = input("Chose: ")

     if choice == "1":
         name = input("Name: ")
         age = int(input("Age: "))
         department = input("Department: ")
         salary = int(input("Salary: "))
         skills = input("Skills: ").split(",")

         if len(employees) == 0:
             employee_id = 1
         else:
             employee_id = employees[-1]["id"] + 1

         employee = {
             "id": employee_id,
             "name": name,
             "age": age,
             "department": department,
             "salary": salary,
             "skills": skills
         }
         employees.append(employee)
         with open(FILE_NAME, "w") as file:
             json.dump(employees, file, indent=4)

         print("Employee added successfully.")

     elif choice == "2":
         employee_id = int(input("Employee ID: "))
         for employee in employees:
             if employee["id"] == employee_id:
                 employees.remove(employee)
                 with open(FILE_NAME, "w") as file:
                     json.dump(employees, file, indent=4)
                 print("Employee removed successfully.")
                 break
             else:
                 print("Employee not found.")

     elif choice == "3":
         employee_id = int(input("Employee ID: "))
         for employee in employees:
             if employee["id"] == employee_id:
                 print("employee")

                 employee["name"] = input("New name: ")
                 employee["age"] = int(input("New age: "))
                 employee["department"] = input("New deparrtment: ")
                 employee["salary"] = int(input("New salary: "))
                 employee["skills"] = input("New skills: ").split(",")

                 with open(FILE_NAME, "w") as file:
                     json.dump(employees, file, indent=4)

                 print("Employee update successfully.")
                 break
         else:
             print("Employee not found.")

     elif choice == "4":
         search = input("Search by name or department: ").lower()
         found = False
        
         for employee in employees:
             if search in employee["name"].lower() or search in employee["department"].lower():
                 print(employee)
                 found = True

         if not found:
             print("No employee found.")

     elif choice == "5":
         for employee in employees:
             print(employee)

     elif choice == "6":
         departments = {}
         for employee in employees:
             department = employee["department"]
             if department not in departments:
                 departments[department] = {
                     "count": 0,
                     "total_salary": 0
                 }
             departments[department]["count"] += 1
             departments[department]["total_salary"] += employee["salary"]

         for department in departments:
             count = departments[department]["count"]
             total_salary = departments[department]["total_salary"]
             average_salary = total_salary / count

             print(department)
             print("Employees:", count)
             print("Average salary:", average_salary)

     elif choice == "7":
         if len(employees) == 0:
             print("No employees.")
         else:
             total_salary = 0

             for employee in employees:
                 total_salary += employee["salary"]

             average_salary = total_salary / len(employees)
             print("Average salary:", average_salary)
     
     elif choice == "8":
         print("Goodbye.")
         break

     else:
         print("Invalid choice.")