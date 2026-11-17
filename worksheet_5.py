    user_profiles[student_id] = {}

    # Save the student ID first.
    with open(filename, 'w') as file:
        json.dump(user_profiles, file)
    print('Student ID saved to file.')

    try:
        with open(filename, 'r') as file:
            loaded_profiles = json.load(file)
    except FileNotFoundError:
        print(f'Error: {filename} not found.')
        loaded_profiles = {}

    if student_id in loaded_profiles:
        dob = input('Enter Date of Birth (YYYY-MM-DD): ').strip()
        email = input('Enter Email Address: ').strip()
        loaded_profiles[student_id]['dob'] = dob
        loaded_profiles[student_id]['email'] = email

        # Save the updated profile.
        with open(filename, 'w') as file:
            json.dump(loaded_profiles, file, indent=4)
        print('Student profile updated and saved.')
    else:
        print(f'Student ID {student_id} not found in the loaded profiles.')

    print('\nCurrent Data:')
    print(json.dumps(loaded_profiles, indent=4))


# Session 10 - Exercise 1
# Kept the function and its test together for this single-file version.
def get_student_info(filename):
    result = []
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 3:
                    first_name = row[1].strip()
                    last_name = row[2].strip()
                    student_id = row[0].strip()
                    message = f'Hello {first_name} {last_name}, your student id is {student_id}.'
                    result.append(message)
    except FileNotFoundError:
        return ['File not found.']
    return result


class TestStudentInfo(unittest.TestCase):
    def test_get_student_info(self):
        # Create a small CSV file to test the function.
        with tempfile.TemporaryDirectory() as folder:
            test_filename = os.path.join(folder, 'test_students.csv')
            with open(test_filename, 'w') as f:
                f.write('1001,Alice,Smith,sd1001@uni123st.edu.au\n')
                f.write('1002,Bob,Johnson,sd1002@uni123st.edu.au\n')

            expected_output = [
                'Hello Alice Smith, your student id is 1001.',
                'Hello Bob Johnson, your student id is 1002.'
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
        emp = Employee('John', 'Doe', 50000)
        emp.give_raise()
        self.assertEqual(emp.annual_salary, 55000)

    def test_custom_raise(self):
        emp = Employee('Jane', 'Smith', 60000)
        emp.give_raise(10000)
        self.assertEqual(emp.annual_salary, 70000)


def main():
    print('\nWorksheet 5')
    print('1-6: Session 9 exercises')
    print('7: Session 10 - Student info test')
    print('8: Session 10 - Employee tests')
    print('9: Run all Session 10 tests')
    choice = input('Choose an exercise (1-9): ').strip()

    exercises = {
        '1': exercise_9_1,
        '2': exercise_9_2,
        '3': exercise_9_3,
        '4': exercise_9_4,
        '5': exercise_9_5,
        '6': exercise_9_6,
    }
    if choice in exercises:
        exercises[choice]()
    elif choice in ('7', '8', '9'):
        suite = unittest.TestSuite()
        if choice in ('7', '9'):
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStudentInfo))
        if choice in ('8', '9'):
            suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestEmployee))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():
            raise SystemExit(1)
    else:
        print('Invalid choice.')


if __name__ == '__main__':
    main()
