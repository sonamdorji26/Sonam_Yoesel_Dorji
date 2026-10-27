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
