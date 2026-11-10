from datetime import datetime


# Session 7 - Exercise 1: Student registration

def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    student = f"{first_name} {last_name} ({student_id})"
    course = f"{course_name} ({course_id})"

    if action == "Add":
        print(f"Added: {student} to {course}")
    elif action == "Amend":
        print(f"Amended: {student}'s enrollment in {course}")
    elif action == "Delete":
        print(f"Deleted: {student}'s enrollment from {course}")
    else:
        print(f"Echo: {student} registered for {course}")


def registration_demo():
    course_enrollment("S1234", "Alice", "Brown", "CSE101", "Introduction to Computer Science")
    course_enrollment("S5678", "Bob", "Smith", "CSE102", "Data Structures", action="Add")
    course_enrollment("S2001", "Charlie", "Davis", "CS103", "Algorithms")
    course_enrollment("S2002", "Diana", "Evans", "CS104", "Databases", action="Amend")
    course_enrollment("S2003", "Ethan", "Ford", "CS105", "Operating Systems", action="Delete")


# Session 7 - Exercise 2: Student course list

def collect_courses(student_id, student_name):
    print(f"\nWelcome {student_name} (ID: {student_id})")
    courses = []

    # Get four course IDs from the student.
    for i in range(4):
        course_id = input(f"Enter course {i + 1} ID: ").strip()
        courses.append(course_id)

    semester = input("Enter semester: ").strip()
    year = input("Enter year: ").strip()

    print("\n--- Course Enrollment Summary ---")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    print("Enrolled Courses:")
    for course in courses:
        print(f"- {course}")
    print(f"Semester: {semester}")
    print(f"Year: {year}")


def store_course_info(student_id, student_name, **courses):
    print("\n--- Student Course Details ---")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")

    if courses:
        for course_id, course_name in courses.items():
            print(f"- {course_id}: {course_name}")
    else:
        print("No courses were provided.")


def course_list_demo():
    sid = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    collect_courses(sid, name)

    # Keyword arguments make a simple course dictionary.
    store_course_info(
        "S2022", "Nar",
        ICT101="Introduction to Computers",
        ICT102="Applied Communication",
        MTH104="Discrete Mathematics",
        ENG101="English Communication"
    )


# Session 7 - Exercise 3: Tkinter calculator

def open_calculator():
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("Basic Calculator")
    root.resizable(False, False)

    tk.Label(root, text="First number:").grid(row=0, column=0, padx=10, pady=6)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=6)

    tk.Label(root, text="Second number:").grid(row=1, column=0, padx=10, pady=6)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=6)
