import csv
import json
import os
import tempfile
import unittest


# Session 9 - Exercise 1
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_summary(self):
        if not self.filename.endswith(".txt"):
            print("Please use a .txt file.")
            return

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write("Python is easy to learn and powerful.\n")
                file.write("It supports object-oriented programming.\n")
                file.write("Python can handle files and exceptions.\n")
                file.write("Python is used in many different fields.\n")
            print("Summary saved successfully.")
        except OSError as error:
            print(f"Error: {error}")


def exercise_9_1():
    filename = input("Enter text filename: ").strip()
    if not filename:
        filename = "python_summary.txt"

    manager = FileManager(filename)
    manager.write_summary()


# Session 9 - Exercise 2
def exercise_9_2():
    filename = "python_summary.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\nFile contents:")
            print(file.read())
    except FileNotFoundError:
        print("File not found. Run Exercise 1 first.")
    except OSError as error:
        print(f"Error: {error}")


# Session 9 - Exercise 3
def exercise_9_3():
    filename = "notes.txt"
    note = input("Enter a note: ")

    try:
        # Append without deleting previous notes.
        with open(filename, "a", encoding="utf-8") as file:
            file.write(note + "\n")
        print("Note saved successfully.")
    except OSError as error:
        print(f"Error: {error}")


# Session 9 - Exercise 4
def exercise_9_4():
    filename = "notes.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        print(f"\nTotal lines: {len(lines)}")
        for number, line in enumerate(lines, start=1):
            print(f"{number}: {line.strip()}")
    except FileNotFoundError:
        print("No notes found. Run Exercise 3 first.")
    except OSError as error:
        print(f"Error: {error}")


# Session 9 - Exercise 5
def exercise_9_5():
    filename = "students.csv"

    student_id = input("Enter Student ID: ").strip()
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    email = input("Enter Email: ").strip()

    if not student_id or not first_name or not last_name:
        print("Student ID and names cannot be empty.")
        return

    try:
        # Save student details in CSV format.
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, first_name, last_name, email])
        print("Student saved successfully.")
    except OSError as error:
        print(f"Error: {error}")


# Session 9 - Exercise 6
def exercise_9_6():
    filename = "student_profiles.json"
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    user_profiles = {}

    # Load existing profiles if available.
    try:
        with open(filename, "r", encoding="utf-8") as file:
            user_profiles = json.load(file)
            if not isinstance(user_profiles, dict):
                user_profiles = {}
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with empty profiles.")
    except OSError as error:
        print(f"Error: {error}")
        return

    user_profiles[student_id] = {}

    try:
        # Save the student ID first.
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(user_profiles, file, indent=4)
        print("Student ID saved to file.")

        with open(filename, "r", encoding="utf-8") as file:
            loaded_profiles = json.load(file)

        if student_id in loaded_profiles:
            dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
            email = input("Enter Email Address: ").strip()

            loaded_profiles[student_id]["dob"] = dob
            loaded_profiles[student_id]["email"] = email

            # Save the updated profile.
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(loaded_profiles, file, indent=4)

            print("Student profile updated and saved.")
        else:
            print(f"Student ID {student_id} not found.")

        print("\nCurrent Data:")
        print(json.dumps(loaded_profiles, indent=4))

    except (OSError, json.JSONDecodeError) as error:
        print(f"Error: {error}")


# Session 10 - Exercise 1
def get_student_info(filename):
    result = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if len(row) >= 3:
                    student_id = row[0].strip()
                    first_name = row[1].strip()
                    last_name = row[2].strip()

                    message = (
                        f"Hello {first_name} {last_name}, "
                        f"your student id is {student_id}."
                    )
                    result.append(message)

    except FileNotFoundError:
        return ["File not found."]

    return result


class TestStudentInfo(unittest.TestCase):
    def test_get_student_info(self):
        # Create temporary student data for testing.
        with tempfile.TemporaryDirectory() as folder:
            test_filename = os.path.join(folder, "test_students.csv")

            with open(test_filename, "w", encoding="utf-8") as file:
                file.write("1001,Alice,Smith,sd1001@uni123st.edu.au\n")
                file.write("1002,Bob,Johnson,sd1002@uni123st.edu.au\n")

            expected_output = [
                "Hello Alice Smith, your student id is 1001.",
                "Hello Bob Johnson, your student id is 1002."
            ]

            result = get_student_info(test_filename)
            self.assertEqual(result, expected_output)


# Session 10 - Exercise 2
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount


class TestEmployee(unittest.TestCase):
    def test_default_raise(self):
        emp = Employee("John", "Doe", 50000)
        emp.give_raise()
        self.assertEqual(emp.annual_salary, 55000)

    def test_custom_raise(self):
        emp = Employee("Jane", "Smith", 60000)
        emp.give_raise(10000)
        self.assertEqual(emp.annual_salary, 70000)


# Main menu
def main():
    while True:
        print("\n===== ICT105 Worksheet 5 =====")
        print("1. Session 9 - Write Python summary")
        print("2. Session 9 - Read Python summary")
        print("3. Session 9 - Add a note")
        print("4. Session 9 - Read notes")
        print("5. Session 9 - Save student CSV")
        print("6. Session 9 - Student JSON profile")
        print("7. Session 10 - Student info test")
        print("8. Session 10 - Employee tests")
        print("9. Run all Session 10 tests")
        print("0. Exit")

        choice = input("Choose an exercise (0-9): ").strip()

        exercises = {
            "1": exercise_9_1,
            "2": exercise_9_2,
            "3": exercise_9_3,
            "4": exercise_9_4,
            "5": exercise_9_5,
            "6": exercise_9_6
        }

        if choice == "0":
            print("Program closed.")
            break

        elif choice in exercises:
            exercises[choice]()

        elif choice in ("7", "8", "9"):
            suite = unittest.TestSuite()

            if choice in ("7", "9"):
                suite.addTests(
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        TestStudentInfo
                    )
                )

            if choice in ("8", "9"):
                suite.addTests(
                    unittest.defaultTestLoader.loadTestsFromTestCase(
                        TestEmployee
                    )
                )

            result = unittest.TextTestRunner(verbosity=2).run(suite)

            if result.wasSuccessful():
                print("All selected tests passed.")
            else:
                print("Some tests failed.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
