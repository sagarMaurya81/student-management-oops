# ============================================================
# OOP BASED STUDENT MANAGEMENT SYSTEM
# ============================================================


# ============================================================
# Student Class
# ============================================================

class Student:

    def __init__(self, student_id, name, age, city):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.city = city
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_details(self):
        print("\nStudent Information")
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"City       : {self.city}")

        if self.courses:
            print("Courses    : ", end="")
            print(", ".join(course.course_name for course in self.courses))
        else:
            print("Courses    : No course assigned")

        print("-" * 40)


# ============================================================
# Course Class
# ============================================================

class Course:

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

            # Also add this course to student's course list
            student.add_course(self)

    def display_course(self):
        print(f"\nCourse ID   : {self.course_id}")
        print(f"Course Name : {self.course_name}")

        if self.students:
            print("Students:")
            for student in self.students:
                print(f"  - {student.name} (ID: {student.student_id})")
        else:
            print("Students    : No students enrolled")


# ============================================================
# Teacher Class
# ============================================================

class Teacher:

    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_teacher(self):
        print("\nTeacher Information")
        print("-" * 40)
        print(f"Teacher ID : {self.teacher_id}")
        print(f"Name       : {self.name}")
        print(f"Subject    : {self.subject}")
        print("-" * 40)


# ============================================================
# Department Class
# ============================================================

class Department:

    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name
        self.courses = []
        self.teachers = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def display_department(self):
        print("\nDepartment Information")
        print("=" * 50)
        print(f"Department ID   : {self.department_id}")
        print(f"Department Name : {self.department_name}")

        print("\nCourses:")
        if self.courses:
            for course in self.courses:
                print(f"  - {course.course_name}")
        else:
            print("  No courses available")

        print("\nTeachers:")
        if self.teachers:
            for teacher in self.teachers:
                print(f"  - {teacher.name}")
        else:
            print("  No teachers available")

        print("=" * 50)


# ============================================================
# Student Management System Class
# ============================================================

class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.courses = []
        self.departments = []
        self.teachers = []

    # --------------------------------------------------------
    # Add Student
    # --------------------------------------------------------

    def add_student(self):

        print("\n========== ADD STUDENT ==========")

        try:
            student_id = int(input("Enter Student ID: "))

            # Check duplicate ID
            for student in self.students:
                if student.student_id == student_id:
                    print("Student ID already exists.")
                    return

            name = input("Enter Student Name: ").strip()
            age = int(input("Enter Age: "))
            city = input("Enter City: ").strip()

            student = Student(
                student_id,
                name,
                age,
                city
            )

            self.students.append(student)

            print("Student added successfully!")

        except ValueError:
            print("Invalid input.")


    # --------------------------------------------------------
    # View Students
    # --------------------------------------------------------

    def view_students(self):

        print("\n========== ALL STUDENTS ==========")

        if not self.students:
            print("No students found.")
            return

        print("-" * 70)

        for student in self.students:
            print(
                f"ID: {student.student_id} | "
                f"Name: {student.name} | "
                f"Age: {student.age} | "
                f"City: {student.city}"
            )

        print("-" * 70)


    # --------------------------------------------------------
    # Find Student
    # --------------------------------------------------------

    def find_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student

        return None


    # --------------------------------------------------------
    # Search Student
    # --------------------------------------------------------

    def search_student(self):

        print("\n========== SEARCH STUDENT ==========")

        keyword = input("Enter Student ID or Name: ").strip()

        found = False

        for student in self.students:

            if (
                str(student.student_id) == keyword
                or keyword.lower() in student.name.lower()
            ):

                student.display_details()
                found = True

        if not found:
            print("No student found.")


    # --------------------------------------------------------
    # Update Student
    # --------------------------------------------------------

    def update_student(self):

        print("\n========== UPDATE STUDENT ==========")

        try:

            student_id = int(input("Enter Student ID: "))

            student = self.find_student(student_id)

            if student is None:
                print("Student not found.")
                return

            print("\nCurrent Details:")

            student.display_details()

            student.name = input("Enter New Name: ").strip()
            student.age = int(input("Enter New Age: "))
            student.city = input("Enter New City: ").strip()

            print("Student updated successfully!")

        except ValueError:

            print("Invalid input.")


    # --------------------------------------------------------
    # Delete Student
    # --------------------------------------------------------

    def delete_student(self):

        print("\n========== DELETE STUDENT ==========")

        try:

            student_id = int(input("Enter Student ID: "))

            student = self.find_student(student_id)

            if student is None:
                print("Student not found.")
                return

            confirmation = input(
                f"Delete {student.name}? (y/n): "
            ).lower()

            if confirmation in ("y", "yes"):

                self.students.remove(student)

                print("Student deleted successfully!")

            else:

                print("Delete operation cancelled.")

        except ValueError:

            print("Invalid input.")


    # --------------------------------------------------------
    # Add Course
    # --------------------------------------------------------

    def add_course(self):

        print("\n========== ADD COURSE ==========")

        course_id = input("Enter Course ID: ")
        course_name = input("Enter Course Name: ")

        course = Course(course_id, course_name)

        self.courses.append(course)

        print("Course added successfully!")


    # --------------------------------------------------------
    # Enroll Student
    # --------------------------------------------------------

    def enroll_student(self):

        print("\n========== ENROLL STUDENT ==========")

        try:

            student_id = int(input("Enter Student ID: "))

            student = self.find_student(student_id)

            if student is None:
                print("Student not found.")
                return

            course_id = input("Enter Course ID: ")

            course = None

            for c in self.courses:

                if c.course_id == course_id:
                    course = c
                    break

            if course is None:
                print("Course not found.")
                return

            course.add_student(student)

            print(
                f"{student.name} enrolled in "
                f"{course.course_name} successfully!"
            )

        except ValueError:

            print("Invalid input.")


    # --------------------------------------------------------
    # View Courses
    # --------------------------------------------------------

    def view_courses(self):

        print("\n========== ALL COURSES ==========")

        if not self.courses:

            print("No courses found.")
            return

        for course in self.courses:

            course.display_course()


    # --------------------------------------------------------
    # Add Department
    # --------------------------------------------------------

    def add_department(self):

        print("\n========== ADD DEPARTMENT ==========")

        department_id = input("Enter Department ID: ")
        department_name = input("Enter Department Name: ")

        department = Department(
            department_id,
            department_name
        )

        self.departments.append(department)

        print("Department added successfully!")


    # --------------------------------------------------------
    # Add Teacher
    # --------------------------------------------------------

    def add_teacher(self):

        print("\n========== ADD TEACHER ==========")

        teacher_id = input("Enter Teacher ID: ")
        name = input("Enter Teacher Name: ")
        subject = input("Enter Subject: ")

        teacher = Teacher(
            teacher_id,
            name,
            subject
        )

        self.teachers.append(teacher)

        print("Teacher added successfully!")


    # --------------------------------------------------------
    # Assign Course to Department
    # --------------------------------------------------------

    def assign_course_to_department(self):

        print("\n========== ASSIGN COURSE ==========")

        department_id = input("Enter Department ID: ")
        course_id = input("Enter Course ID: ")

        department = None
        course = None

        for d in self.departments:

            if d.department_id == department_id:
                department = d

        for c in self.courses:

            if c.course_id == course_id:
                course = c

        if department is None:
            print("Department not found.")
            return

        if course is None:
            print("Course not found.")
            return

        department.add_course(course)

        print("Course assigned to department successfully!")


    # --------------------------------------------------------
    # Display Departments
    # --------------------------------------------------------

    def view_departments(self):

        print("\n========== DEPARTMENTS ==========")

        if not self.departments:

            print("No departments found.")
            return

        for department in self.departments:

            department.display_department()


    # --------------------------------------------------------
    # Main Menu
    # --------------------------------------------------------

    def menu(self):

        while True:

            print("\n")
            print("=" * 55)
            print("       STUDENT MANAGEMENT SYSTEM")
            print("=" * 55)

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Add Course")
            print("7. View Courses")
            print("8. Enroll Student in Course")
            print("9. Add Department")
            print("10. Add Teacher")
            print("11. Assign Course to Department")
            print("12. View Departments")
            print("13. Exit")

            print("=" * 55)

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.add_course()

            elif choice == "7":
                self.view_courses()

            elif choice == "8":
                self.enroll_student()

            elif choice == "9":
                self.add_department()

            elif choice == "10":
                self.add_teacher()

            elif choice == "11":
                self.assign_course_to_department()

            elif choice == "12":
                self.view_departments()

            elif choice == "13":

                print(
                    "\nThank you for using "
                    "Student Management System!"
                )

                break

            else:

                print("Invalid choice. Please try again.")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":

    system = StudentManagementSystem()

    system.menu()