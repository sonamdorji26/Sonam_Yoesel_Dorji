    first_entry = tk.Entry(root, width=16)
    first_entry.grid(row=0, column=1)

    tk.Label(root, text="Second number:").grid(row=1, column=0, padx=10, pady=10)
    second_entry = tk.Entry(root, width=16)
    second_entry.grid(row=1, column=1)

    operation = tk.StringVar(value="+")
    tk.OptionMenu(root, operation, "+", "-", "*", "/").grid(row=2, column=0)
    result_label = tk.Label(root, text="Result: ")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate():
        try:
            first = float(first_entry.get())
            second = float(second_entry.get())
            choice = operation.get()

            if choice == "+":
                answer = first + second
            elif choice == "-":
                answer = first - second
            elif choice == "*":
                answer = first * second
            else:
                if second == 0:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return
                answer = first / second

            result_label.config(text=f"Result: {answer:g}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=1, pady=10)
    root.mainloop()


if __name__ == "__main__":
    print("ICT105 - Worksheet 4, Session 7")
    print("1. Student registration")
    print("2. Student course list")
    print("3. Tkinter calculator")
    choice = input("Choose an exercise (1-3): ").strip()

    if choice == "1":
        exercise1()
    elif choice == "2":
        exercise2()
    elif choice == "3":
        open_calculator()
    else:
        print("Invalid choice.")


from datetime import datetime


# Exercises 1 and 2 - User profile and login attempts
class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Date of birth: {self.date_of_birth}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Exercises 3 and 4 - Classrooms and enrollment records
class classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0
        self.audit_log = []

    def describe_classroom(self):
        print(f"Classroom: {self.classroom_name}")
        print(f"Location: {self.classroom_location}")
        print(f"Seats: {self.seats_in_class}")

    def checksize_classroom(self):
        if self.students_enrolled <= self.seats_in_class:
            print(f"Enough seats for {self.students_enrolled} enrolled students.")
        else:
            print(f"Not enough seats for {self.students_enrolled} enrolled students.")

    def set_number_enrolled(self, number):
        self.update_number_enrolled(number)

    def update_number_enrolled(self, number):
        if not isinstance(number, int) or number < 0:
            print("The number of students must be a non-negative whole number.")
            return
        old_number = self.students_enrolled
        self.students_enrolled = number
        self.audit_log.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "old": old_number,
            "new": number
        })

    def show_audit_log(self):
        print("Enrollment changes:")
        for entry in self.audit_log:
            print(f"{entry['time']}: {entry['old']} -> {entry['new']}")


# Exercise 5 - Equipment inherits from classroom
class equipment(classroom):
    def __init__(self, classroom_name, classroom_location, seats_in_class, devices):
        super().__init__(classroom_name, classroom_location, seats_in_class)
        self.devices = devices

    def display_devices(self):
        print(f"Devices in {self.classroom_name}:")
        for device in self.devices:
            print(f"- {device}")


def exercise1():
    users = [
        User("Alice", "Smith", "alice@example.com", "alice01", "2004-05-12", "Perth"),
        User("Bob", "Johnson", "bob@example.com", "bobj", "2003-08-22", "Fremantle"),
        User("Charlie", "Brown", "charlie@example.com", "charlieb", "2005-01-17", "Cannington")
    ]
    for user in users:
        user.describe_user()
        user.greet_user()
        print()

