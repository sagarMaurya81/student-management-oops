# 🎓 Student Management System

An **Object-Oriented Programming (OOP)** based Student Management System built using **Python**.

This project is a conversion of a basic function-based Student Management application into an **OOP-based application** using classes, objects, and relationships between different entities.

---

## 📌 Project Overview

The Student Management System allows users to manage:

* Students
* Courses
* Departments
* Teachers
* Student course enrollment

The application runs in the **Command Line Interface (CLI)** and provides a menu-driven system for performing different operations.

---

## 🧱 OOP Classes Used

The project contains the following main classes:

### 1. `Student`

The `Student` class represents a student.

#### Attributes

```python
student_id
name
age
city
courses
```

#### Methods

```python
add_course()
display_details()
```

---

### 2. `Course`

The `Course` class represents a course offered by the institution.

#### Attributes

```python
course_id
course_name
students
```

#### Methods

```python
add_student()
display_course()
```

A course can contain multiple students.

---

### 3. `Department`

The `Department` class represents an academic department.

#### Attributes

```python
department_id
department_name
courses
teachers
```

#### Methods

```python
add_course()
add_teacher()
display_department()
```

A department can contain multiple courses and teachers.

---

### 4. `Teacher`

The `Teacher` class represents a teacher.

#### Attributes

```python
teacher_id
name
subject
```

#### Methods

```python
display_teacher()
```

---

### 5. `StudentManagementSystem`

This is the main management class that controls the complete application.

It stores:

```python
students
courses
departments
teachers
```

It also provides methods for performing operations such as:

```text
Add Student
View Students
Search Student
Update Student
Delete Student
Add Course
View Courses
Enroll Student
Add Department
Add Teacher
Assign Course to Department
View Departments
```

---

# 🔗 Class Relationship

The main relationship required in this practical task is:

```text
Department
    │
    ▼
  Course
    │
    ▼
 Student
```

For example:

```text
Computer Science Department
            │
            ▼
          Python
            │
            ▼
          Sagar
```

In Python, this relationship is created using:

```python
department.add_course(course)
course.add_student(student)
```

This means:

* A **Department** can have multiple Courses.
* A **Course** can have multiple Students.
* A **Student** can enroll in multiple Courses.

---

# 🏗️ Project Structure

A simple project structure can be:

```text
student-management-system/
│
├── main.py
└── README.md
```

Where:

* `main.py` → contains the complete Python application
* `README.md` → contains project documentation

---

# ⚙️ Features

## 👨‍🎓 Student Management

The application supports:

### Add Student

Add a new student by entering:

```text
Student ID
Name
Age
City
```

### View Students

Display all students stored in the system.

### Search Student

Search for a student using:

```text
Student ID
Student Name
```

### Update Student

Update the student's:

```text
Name
Age
City
```

### Delete Student

Delete a student after confirmation.

---

## 📚 Course Management

The system allows you to:

* Add a new course
* View all courses
* Enroll students into courses

Example:

```text
Course ID: C01
Course Name: Python
```

---

## 🏢 Department Management

The system allows you to:

* Add a department
* Assign courses to a department
* View department information

Example:

```text
Department ID: D01
Department Name: Computer Science
```

---

## 👨‍🏫 Teacher Management

Teachers can be added with:

```text
Teacher ID
Teacher Name
Subject
```

---

# 🖥️ Menu

When the program starts, the following menu is displayed:

```text
=======================================================
       STUDENT MANAGEMENT SYSTEM
=======================================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Add Course
7. View Courses
8. Enroll Student in Course
9. Add Department
10. Add Teacher
11. Assign Course to Department
12. View Departments
13. Exit
=======================================================
```

---

# ▶️ How to Run

## Step 1: Install Python

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Clone or Download the Project

Place the project files in a folder.

Example:

```text
student-management-system/
```

---

## Step 3: Run the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

For some Linux/macOS systems:

```bash
python3 main.py
```

---

# 💡 Example Usage

### Create a student

```text
Enter Student ID: 101
Enter Student Name: Sagar
Enter Age: 22
Enter City: Mumbai
```

Output:

```text
Student added successfully!
```

### Create a course

```text
Enter Course ID: C01
Enter Course Name: Python
```

Output:

```text
Course added successfully!
```

### Enroll student

```text
Enter Student ID: 101
Enter Course ID: C01
```

Output:

```text
Sagar enrolled in Python successfully!
```

---

# 🧠 OOP Concepts Demonstrated

This project demonstrates important Python OOP concepts.

## 1. Classes

Classes are used to create blueprints for objects.

Example:

```python
class Student:
    ...
```

---

## 2. Objects

Objects are created from classes.

Example:

```python
student = Student(
    101,
    "Sagar",
    22,
    "Mumbai"
)
```

---

## 3. Constructor

The `__init__()` method initializes object data.

Example:

```python
def __init__(self, student_id, name, age, city):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.city = city
```

---

## 4. Attributes

Attributes store object data.

Example:

```python
student.name
student.age
student.city
```

---

## 5. Methods

Methods define the behavior of an object.

Example:

```python
student.display_details()
```

---

## 6. Encapsulation

Data and related methods are grouped inside a class.

For example:

```python
class Student:

    def __init__(self, student_id, name, age, city):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.city = city

    def display_details(self):
        ...
```

---

## 7. Composition / Object Relationships

Objects are connected with other objects.

For example:

```python
class Course:

    def __init__(self, course_id, course_name):
        self.students = []
```

A `Course` object maintains a collection of `Student` objects.

Similarly:

```python
class Department:

    def __init__(self, department_id, department_name):
        self.courses = []
        self.teachers = []
```

A `Department` contains courses and teachers.

---

# 🔄 Data Relationship Diagram

```text
              ┌──────────────────┐
              │    Department    │
              │──────────────────│
              │ department_id    │
              │ department_name  │
              └────────┬─────────┘
                       │
                       │ contains
                       ▼
              ┌──────────────────┐
              │      Course      │
              │──────────────────│
              │ course_id        │
              │ course_name      │
              │ students[]       │
              └────────┬─────────┘
                       │
                       │ enrolls
                       ▼
              ┌──────────────────┐
              │     Student      │
              │──────────────────│
              │ student_id       │
              │ name             │
              │ age              │
              │ city             │
              │ courses[]        │
              └──────────────────┘

              ┌──────────────────┐
              │     Teacher      │
              │──────────────────│
              │ teacher_id       │
              │ name             │
              │ subject          │
              └──────────────────┘

                 Department
                     │
                     │ has
                     ▼
                  Teacher
```

---

# 🎯 Learning Objectives

After completing this project, you should understand:

* How to create classes in Python
* How to create objects
* How constructors work
* How to use attributes and methods
* How multiple classes interact with each other
* How to model real-world entities using OOP
* How composition and object relationships work
* How to build a menu-driven CLI application using OOP

---

# 🚀 Future Improvements

The project can be enhanced by adding:

* File/database storage
* Student login system
* Teacher-course assignment
* Department-wise student listing
* Course removal
* Student attendance
* Student marks and grades
* Validation for all user inputs
* SQLite database integration
* GUI using Tkinter
* REST API using Flask or FastAPI

---

# 👨‍💻 Technologies Used

```text
Python 3
Object-Oriented Programming
Command Line Interface (CLI)
```

---

