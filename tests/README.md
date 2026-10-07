# Python Intermediate+ Practice

Welcome to the Python practice repository.

The goal of these exercises is not only to make the code work.

You should learn how to:

* Think about a problem before coding.
* Choose appropriate data structures.
* Break a problem into functions.
* Work with files and persistent data.
* Handle invalid input and edge cases.
* Debug your own code.
* Read and understand error messages.
* Work with Git branches and Pull Requests.

---

# Important Git Rules

## DO NOT PUSH YOUR ANSWERS TO `test`

The `test` branch contains the original questions and is the base branch for your work.

**You must NEVER push your solution code directly to `test`.**

Your workflow must always be:

```text
test
  |
  └── create a new branch
          |
          └── test-answer
                  |
                  └── write your solutions
                          |
                          └── push test-answer
                                  |
                                  └── create Pull Request
                                          |
                                          └── test
```

Your answer branch must be called:

```text
test-answer
```

### Required workflow

Start from the latest `test` branch:

```bash
git checkout test
git pull
```

Create your answer branch:

```bash
git checkout -b test-answer
```

Do your work on:

```text
test-answer
```

Commit your changes:

```bash
git add .
git commit -m "Add Python practice solutions"
```

Push ONLY the answer branch:

```bash
git push -u origin test-answer
```

Then create a Pull Request:

```text
test-answer -> test
```

Do not merge the Pull Request yourself unless instructed.

---

# Exercise Order

You must complete the exercises in the following order.

## 1. Student Grade Manager

File/data persistence, collections, functions, validation and calculations.

Focus on understanding:

* Lists
* Dictionaries
* Nested data
* Functions
* Searching
* Calculations
* Reading from files
* Writing to files

---

## 2. Personal Wallet

Build a personal wallet application.

Focus on:

* Income and expenses
* transaction
* Calculating balances
* Filtering
* Searching
* Persistent state
* Working with dates

---

## 3. Inventory Management System

Build an inventory management application.

Focus on:

* Products
* Stock management
* Searching
* Updating data
* Validation
* Calculations
* Persistent state

---

## 4. Personal Library

Build a personal library application.

Focus on:

* Managing collections
* Searching
* Filtering
* Updating object state
* Borrow/return logic
* Persistent data

---

## 5. Simple Banking System

Build a simple banking system.

Focus on:

* Multiple accounts
* transaction
* Money transfers
* Validation
* State changes
* transaction history
* Persistent state

Pay special attention to what happens when an operation fails halfway through.

---

## 6. Game Save System

Build a small text-based game with a persistent player state.

Focus on:

* Managing application state
* Updating state
* Inventory
* Experience and levels
* Saving and loading
* Designing your own game logic

---

## 7. Todo Manager

Build a Todo application.

Focus on:

* CRUD operations
* Searching
* Filtering
* Status changes
* Priorities
* Persistent state

---

## 8. Shopping Cart & Order History

Build a small shopping system.

Focus on:

* Products
* Stock
* Shopping cart
* Orders
* Calculations
* State changes
* Persistent order history

---

## 9. Expense Tracker With Reports

Build an advanced expense tracker.

Focus on:

* Dates
* Date ranges
* Monthly reports
* Category reports
* Searching
* Filtering
* Aggregating data
* Persistent state

This exercise should require more planning before coding.

---

## 10. Employee Management System

Build an employee management system.

Focus on:

* CRUD operations
* Searching
* Updating
* Departments
* Salary calculations
* Reports
* Persistent state

---

# Final Project

## Personal Finance Manager

After completing the previous exercises, build the final project.

This project combines the concepts from the previous exercises.

You should be able to manage:

* Income
* Expenses
* Transfers
* transaction
* Categories
* Reports
* Monthly statistics
* Date-range statistics
* Persistent application state

Do not start the final project before completing the previous exercises.

The purpose of the previous exercises is to prepare you for this one.

---

# Bonus Challenges

After completing the Final Project, you can work on:

1. Undo System
2. Multiple Data Files
3. Backup & Restore System

These are optional but highly recommended.

---

# AI Usage Rules

You are allowed to use AI as a learning and research tool.

However, there is one very important rule:

## DO NOT GIVE THE FULL QUESTION TO AI AND ASK FOR THE SOLUTION.

You should solve the problem yourself first.

You may use search engines, documentation and AI to understand a concept.

For example, it is completely fine to ask:

```text
How does JSON serialization work in Python?
```

or:

```text
How does the `datetime` module work?
```

or:

```text
Why am I getting this Python error?
```

or:

```text
What is the difference between a list and a dictionary?
```

or:

```text
How can I safely read data from a file in Python?
```

These are learning questions.

However, do NOT do this:

```text
Here is my entire exercise.
Write the solution for me.
```

or:

```text
Solve this project completely.
```

or:

```text
Here is the assignment.
Give me the complete code.
```

The purpose of these exercises is for you to develop your own problem-solving ability.

If you let AI solve the entire problem, you will lose the most important part of the exercise.

---

# You Are Allowed To Ask AI For Help

If you are stuck on a specific concept, you can ask for an explanation.

For example:

```text
I don't understand how I should save a Python dictionary into a file.
Can you explain the concept without solving my exercise?
```

This is allowed.

You can also show a specific error:

```text
I wrote this code and I'm getting this error:

[error]

Can you explain what this error means?
```

You should still try to fix the problem yourself after understanding the explanation.

---

# Debugging Is Part Of The Exercise

Your code does NOT need to be perfect on the first attempt.

In fact, it is expected that you will encounter:

* Bugs
* Errors
* Wrong calculations
* Unexpected input
* File problems
* Logic problems
* Incorrect data structures
* Functions that don't behave as expected

Do not immediately ask AI to rewrite your code.

First:

1. Read the error.
2. Find the line that caused it.
3. Understand what the program was trying to do.
4. Try to identify the problem yourself.
5. Try a fix.
6. Run the program again.
7. If you are still stuck, ask a specific question.

---

# Discuss Your Bugs

If you cannot solve a bug after trying yourself, bring the problem to our discussion.

You can send:

* The relevant part of your code.
* The error message.
* What you expected to happen.
* What actually happened.
* What you already tried.

We will discuss the problem and fix it together.

The goal is not simply to receive the corrected code.

The goal is to understand:

```text
Why was it broken?
Why did the fix work?
How could you recognize this problem next time?
```

---

# Persistence Requirement

Most of these projects require persistent data.

This means:

```text
Run #1
    Create data
    Modify data
    Close program

Run #2
    Previous data must still exist
```

For example:

```text
Run #1:

Student: Ali
Python: 18
Math: 16
```

After closing the program and running it again:

```text
Run #2:

Student: Ali
Python: 18
Math: 16
```

The application must load its previous state automatically.

---

# File Handling

You are responsible for deciding:

* What should be stored?
* How should it be represented?
* Which file format is appropriate?
* When should data be loaded?
* When should data be saved?
* What should happen if the file does not exist?
* What should happen if stored data is invalid?

Do not blindly copy a solution.

Understand why your chosen approach works.

---

# Data Structures

Do not use a data structure simply because someone told you to use it.

For every project, think about:

```text
What information do I have?

How is that information related?

Do I need to search it?

Do I need to update it?

Do I need to delete it?

Do I need to calculate something from it?

Do I need to save it to a file?
```

Then choose the appropriate Python data types.

---

# Functions

Do not write the entire application as one huge function.

As the projects become larger, think about separating responsibilities.

For example, you may eventually need separate parts of your program for:

* Input
* Validation
* Data processing
* Calculations
* File operations
* Displaying results

You are responsible for deciding how to structure your functions.

Do not blindly follow predefined function names.

---

# Code Quality

Your code should be:

* Readable
* Understandable
* Consistent
* Properly indented
* Reasonably organized
* Easy to modify

Avoid unnecessary complexity.

At the same time, do not put everything into one huge block just to make the code shorter.

---

# Most Important Rule

**TRY FIRST.**

It is completely fine if your first implementation has bugs.

It is completely fine if your program does not work on the first attempt.

It is completely fine to struggle with a problem.

The important thing is that you think about the problem and attempt your own solution before asking for help.

A working solution that you fully understand is much more valuable than a perfect solution that you copied from AI.

---

# Final Git Reminder

Before pushing anything, check your branch:

```bash
git branch
```

You should see:

```text
* test-answer
```

NOT:

```text
* test
```

Your answers must ONLY be pushed to:

```text
test-answer
```

Then open a Pull Request:

```text
test-answer -> test
```

**NEVER PUSH YOUR ANSWERS DIRECTLY TO `test`.**
