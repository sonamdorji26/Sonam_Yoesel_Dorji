# Lists

courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

print(courses)

# Sorting without changing the original list
sorted_courses = sorted(courses)
print(sorted_courses)

reverse_sorted_courses = sorted(courses, reverse=True)
print(reverse_sorted_courses)

# Reversing the list
courses.reverse()
print(courses)

courses.reverse()
print(courses)

# Sorting the original list
courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)


# Updating the available courses

courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I"
]

sorted_courses = sorted(courses)

print("\nThe following courses are available for expression of interest if students meet the prerequisites:")

for course in sorted_courses:
    print(course)

# Replacing a withdrawn course
withdrawn_course = courses[3]
courses[3] = "Discrete Mathematics"

print(f"\n{withdrawn_course} is no longer available.")
print(f"It has been replaced with {courses[3]}.")

# Adding three more courses
courses.insert(0, "Introduction to Philosophy")
courses.insert(len(courses) // 2, "Calculus II")
courses.append("Linear Algebra")

print("\nUpdated available courses:")

for course in courses:
    print(course)

# Removing four unavailable courses
unavailable_courses = []

unavailable_courses.append(courses.pop(1))
unavailable_courses.append(courses.pop(4))
unavailable_courses.append(courses.pop(7))
unavailable_courses.append(courses.pop(9))

print("\nThe following courses are unavailable due to technical and room availability issues:")

for course in unavailable_courses:
    print(course)

print("\nThe withdrawn courses have been removed.")

print("\nRemaining available courses:")

for course in courses:
    print(course)


# Tuples and loops

course_data = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

course_names = []

for course_id, course_name in course_data:
    course_names.append(course_name)

print("\nCourse names:")

for name in course_names:
    print(name)


# Conditional statements and loops

course_departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

# Search for the department using course ID
while True:
    num = input("\nEnter course ID (1-15), or 'quit' or '0' to exit: ").strip()

    if num.lower() == "quit" or num == "0":
        print("Exiting department search.")
        break

    elif num.isdigit():
        num = int(num)

        if 1 <= num <= 15:
            found = False

            for course in course_departments:
                if course[0] == num:
                    print(f"Course ID {num} is in the {course[1]} department.")
                    found = True
                    break

            if not found:
                print(f"Course ID {num} not found.")

        else:
            print("Course ID is out of range (1-15), try again.")

    else:
        print("Invalid input. Please enter a valid course ID.")


# Course information retrieval

course_details = [
    [1, "Introduction to Programming", "Computer Science", []],
    [2, "Calculus I", "Mathematics", []],
    [3, "Data Structures and Algorithms", "Computer Science", ["Introduction to Programming"]],
    [4, "Linear Algebra", "Mathematics", []],
    [5, "Physics I", "Physics", []],
    [6, "Chemistry I", "Chemistry", []],
    [7, "Biology I", "Biology", []],
    [8, "Microeconomics", "Economics", []],
    [9, "Macroeconomics", "Economics", ["Microeconomics"]],
    [10, "Psychology I", "Psychology", []],
    [11, "History I", "History", []],
    [12, "English Composition I", "English", []],
    [13, "Introduction to Philosophy", "Philosophy", []],
    [14, "Calculus II", "Mathematics", ["Calculus I"]],
    [15, "Discrete Mathematics", "Computer Science", ["Introduction to Programming"]]
]

# Find a course and display its information
while True:
    user_input = input("\nEnter course ID for details (1-15), or 'quit' or '0' to exit: ").strip()

    if user_input.lower() == "quit" or user_input == "0":
        print("Exiting the program.")
        break

    elif user_input.isdigit():
        course_id = int(user_input)

        if 1 <= course_id <= 15:
            found = False

            for course in course_details:
                if course[0] == course_id:
                    print(f"Course ID: {course[0]}")
                    print(f"Course Name: {course[1]}")
                    print(f"Department: {course[2]}")

                    if course[3]:
                        print(f"Prerequisites: {', '.join(course[3])}")
                    else:
                        print("Prerequisites: None")

                    found = True
                    break

            if not found:
                print("Course not found.")

        else:
            print("Course ID is out of range (1-15), try again.")

    else:
        print("Invalid input. Please enter a valid course ID.")
