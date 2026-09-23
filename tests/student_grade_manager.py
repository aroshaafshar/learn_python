# ============================================================
# PROJECT 1 - STUDENT GRADE MANAGER
# ============================================================

"""
Build a console application for managing students and their grades.

The application should provide a menu similar to:

1. Add Student
2. Add Grade
3. Update Grade
4. Show Student Report
5. Show All Students
6. Find Best Student
7. Delete Student
8. Exit

Each student should have at least:

- A unique ID
- Name
- Age
- A collection of subjects and grades

Example:

Student:
    ID: 1024
    Name: Ali
    Age: 22

    Python: 18
    Mathematics: 15
    English: 19

The program should be able to:

- Add a new student.
- Prevent duplicate student IDs.
- Add a new subject and grade for a student.
- Update an existing grade.
- Calculate the average grade of a student.
- Display a complete student report.
- Display all students.
- Find the student with the highest average.
- Delete a student.

Input validation:

- Student ID must be unique.
- Grades must be valid numbers.
- Grades must be within an appropriate range.
- The program must handle invalid input without crashing.

Persistence requirement:

All students and their grades must be saved to a file.

When the program starts again, previously saved students must
automatically be loaded.

Example:

Run #1:
    Add Ali
    Add Python -> 18
    Add Math -> 16

Close the program.

Run #2:
    Ali and all of his grades must still exist.

The choice of file format and data structures is up to you.
"""
