# Dictionaries

# Student course enrollments
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
    1006: ["BIO102", "ENGL101"],
    1007: ["ECON101", "PSY101"],
    1008: ["ECON102", "SOC101"],
    1009: ["PSY102", "SOC102"],
    1010: ["CS101", "MATH101"]
}

print("\nSTUDENT COURSE ENROLLMENTS")

for student_id, courses in course_enrollments.items():
    print("\nStudent ID:", student_id)
    print("Enrolled Courses:", ", ".join(courses))


# Courses grouped by department
departments = {
    "Computer Science": [
        ("Computer Science", "CS101", "Introduction to Computer Science"),
        ("Computer Science", "CS202", "Data Structures and Algorithms")
    ],
    "Mathematics": [
        ("Mathematics", "MATH101", "Calculus I"),
        ("Mathematics", "MATH102", "Calculus II")
    ],
    "Physics": [
        ("Physics", "PHY101", "General Physics I"),
        ("Physics", "PHY102", "General Physics II")
    ],
    "Chemistry": [
        ("Chemistry", "CHEM101", "General Chemistry I"),
        ("Chemistry", "CHEM102", "General Chemistry II")
    ],
    "Biology": [
        ("Biology", "BIO101", "Biology I"),
        ("Biology", "BIO102", "Biology II")
    ],
    "History": [
        ("History", "HIST101", "American History I"),
        ("History", "HIST102", "American History II")
    ],
    "English": [
        ("English", "ENGL101", "English Composition I"),
        ("English", "ENGL102", "English Composition II")
    ],
    "Economics": [
        ("Economics", "ECON101", "Principles of Economics"),
        ("Economics", "ECON102", "Intermediate Microeconomics")
    ],
    "Psychology": [
        ("Psychology", "PSY101", "Introduction to Psychology"),
        ("Psychology", "PSY102", "Developmental Psychology")
    ],
    "Sociology": [
        ("Sociology", "SOC101", "Introduction to Sociology"),
        ("Sociology", "SOC102", "Social Problems")
    ]
}

print("\nCLASS SCHEDULE")

for department, courses in departments.items():
    print("\nDepartment:", department)

    for department_name, course_id, course_name in courses:
        print("Course ID:", course_id)
        print("Course Name:", course_name)


# Lecturer assignments
lecturer_assignments = {
    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Prof. David Lee": ["PHY101"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
    "Miss. Sophia Carter": ["CHEM102", "BIO101", "BIO102"],
    "Dr. Oliver Hernandez": ["HIST101", "HIST102", "ENGL101"],
    "Prof. Isabella Garcia": ["ENGL102", "SOC101"],
    "Prof. Evelyn Russell": ["ECON101", "ECON102"],
    "Dr. Lucas Sanchez": ["PSY101", "PSY102"],
    "Asst. Prof. Liam Lopez": ["SOC102"]
}

print("\nLECTURER ASSIGNMENTS")

for lecturer, courses in lecturer_assignments.items():
    print("\nLecturer:", lecturer)
    print("Assigned Courses:", ", ".join(courses))


# Read student details from the CSV file
print("\nCSV STUDENT DETAILS")

student_details = {}

try:
    import pandas as pd

    df = pd.read_csv("students.csv", header=None)

    for index, row in df.iterrows():
        student_id = int(row[0])
        student_firstname = str(row[1])
        student_surname = str(row[2])
        student_email = str(row[3])

        if student_id not in student_details:
            student_details[student_id] = [
                student_firstname,
                student_surname,
                student_email
            ]

    print(student_details)

except FileNotFoundError:
    print("students.csv not found.")

except ImportError:
    print("Pandas is not installed. Run: python -m pip install pandas")


# User inputs and while loops

# Build a class list with existing or new students
students = []

print("\nSTUDENT CLASS LIST")

while True:
    student_name = input("\nEnter student name (or quit to finish): ").strip()

    if student_name.lower() == "quit":
        break

    if student_name == "":
        print("Please enter a student name.")
        continue

    found = False
    full_name = student_name

    for student_id, details in student_details.items():
        student_firstname = details[0]
        student_surname = details[1]
        student_email = details[2]

        if student_name.lower() in [
            student_firstname.lower(),
            (student_firstname + " " + student_surname).lower()
        ]:
            full_name = student_firstname + " " + student_surname

            print("\nStudent ID:", student_id)
            print("Name:", full_name)
            print("Email:", student_email)

            if student_id in course_enrollments:
                print("Enrolled Courses:", ", ".join(course_enrollments[student_id]))

            found = True
            break

    if not found:
        print("New student:", student_name)

    # Avoid adding the same student twice
    if full_name.lower() not in [name.lower() for name in students]:
        students.append(full_name)
        print(full_name, "has been added to the class.")
    else:
        print(full_name, "is already in the class.")

print("\nFINAL CLASS LIST")

for student in students:
    print(student)

print("\nTotal Students:", len(students))


# Room details from the worksheet
rooms = [
    [101, 15, "Ground Floor", "Building A"],
    [102, 15, "Ground Floor", "Building A"],
    [103, 20, "Ground Floor", "Building A"],
    [104, 20, "Ground Floor", "Building A"],
    [105, 25, "Ground Floor", "Building A"],
    [106, 25, "Ground Floor", "Building A"],
    [107, 30, "Ground Floor", "Building A"],
    [108, 30, "Ground Floor", "Building A"],
    [109, 30, "Ground Floor", "Building A"],
    [110, 10, "Ground Floor", "Building A"],
    [201, 10, "1st Floor", "Building A"],
    [202, 10, "1st Floor", "Building A"],
    [203, 25, "1st Floor", "Building A"],
    [204, 25, "1st Floor", "Building A"],
    [205, 30, "1st Floor", "Building A"],
    [206, 40, "1st Floor", "Building A"],
    [207, 40, "1st Floor", "Building A"],
    [208, 40, "1st Floor", "Building A"]
]

print("\nCLASSROOM SEARCH")

while True:
    user_input = input("\nEnter number of students (or quit): ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    required_capacity = int(user_input)

    if required_capacity <= 0:
        print("Please enter at least one student.")
        continue

    suitable_rooms = []

    # Check for a single room first
    for room in rooms:
        if room[1] >= required_capacity:
            suitable_rooms.append(room)

    if suitable_rooms:
        best_room = min(suitable_rooms, key=lambda room: room[1])

        print("\nROOM FOUND")
        print("Number of Rooms: 1")
        print("Room Number:", best_room[0])
        print("Room Capacity:", best_room[1])
        print("Floor:", best_room[2])
        print("Location:", best_room[3])

    else:
        # Larger classes may need more than one room
        suitable_rooms = []
        sorted_rooms = sorted(rooms, key=lambda room: room[1], reverse=True)

        total_capacity = 0

        for room in sorted_rooms:
            suitable_rooms.append(room)
            total_capacity += room[1]

            if total_capacity >= required_capacity:
                break

        if total_capacity >= required_capacity:
            print("\nROOMS FOUND")
            print("Number of Rooms:", len(suitable_rooms))

            for room in suitable_rooms:
                print("\nRoom Number:", room[0])
                print("Room Capacity:", room[1])
                print("Floor:", room[2])
                print("Location:", room[3])

            print("\nTotal Capacity:", total_capacity)

        else:
            print("Not enough rooms for that many students.")


# Exit using quit, exit or 0
students = []

print("\nSTUDENT ENTRY - EXIT CONDITIONS")

while True:
    student_name = input("\nEnter student name (quit/exit/0 to stop): ").strip()

    if student_name.lower() in ["quit", "exit", "0"]:
        print("\nExit parameter used:", student_name)
        break

    if student_name == "":
        print("Please enter a valid name.")
        continue

    students.append(student_name)
    print(student_name, "has been added.")

print("\nSTUDENT LIST")

for student in students:
    print(student)

print("\nTotal Students:", len(students))


# Control the loop with an active variable
students = []
active = True

print("\nACTIVE VARIABLE LOOP")

while active:
    student_name = input("\nEnter student name (quit to stop): ").strip()

    if student_name.lower() == "quit":
        active = False

    elif student_name == "":
        print("Please enter a valid name.")

    else:
        students.append(student_name)
        print(student_name, "has been added.")

print("\nFINAL STUDENT LIST")

for student in students:
    print(student)

print("\nTotal Students:", len(students))


# Stop once the room is full
students = []
max_cap = 15

print("\nROOM CAPACITY LOOP")
print("Maximum Room Capacity:", max_cap)

while True:
    student_name = input("\nEnter student name: ").strip()

    if student_name == "":
        print("Please enter a valid name.")
        continue

    if student_name.lower() in ["quit", "exit", "0"]:
        print("Enter a student name. This loop ends at maximum capacity.")
        continue

    students.append(student_name)
    print(student_name, "has been added.")

    if len(students) >= max_cap:
        print("\nMaximum room capacity reached.")
        break

print("\nFINAL STUDENT LIST")

for student in students:
    print(student)

print("\nTotal Students:", len(students))
print("Maximum Capacity:", max_cap)


# Keep reading lines until Ctrl+C
line_count = 0

print("\nINFINITE INPUT LOOP")
print("Enter text. Press Ctrl+C to exit.")

try:
    while True:
        user_input = input("\nEnter text: ")

        line_count += 1
        print("Line", line_count, ":", user_input)

except KeyboardInterrupt:
    print("\nProgram interrupted using Ctrl+C.")
    print("Total Number of Lines:", line_count)
    print("Program exited.")
    
