def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Average")
    print("6. Grade from marks")
    print("7. Show summary")
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

def average(a, b, c):
    return (a + b + c) / 3

def add(*args):
    return sum(args)

def calculate(a, b, operation="+"):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")

def grade_from_marks(marks, maximum=100):
    if marks < 0 or marks > maximum:
        raise ValueError(
            f"Marks must be between 0 and {maximum}."
        )

    percentage = (marks / maximum) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def show_summary(**kwargs):
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def demonstrate_scope():
    local_variable = "I exist only inside this function."
    print(local_variable)


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            # D. Test add(2, 4, 6, 8)
            result = add(2, 4, 6, 8)
            print("add(2, 4, 6, 8) =", result)
            history.append(result)

        elif choice == "2":
            a = get_number("First number: ")
            b = get_number("Second number: ")

            result = calculate(a, b, "-")
            print(f"Result: {result:.2f}")
            history.append(result)

        elif choice == "3":
            a = get_number("First number: ")
            b = get_number("Second number: ")

            result = calculate(a, b, "*")
            print(f"Result: {result:.2f}")
            history.append(result)

        elif choice == "4":
            a = get_number("First number: ")
            b = get_number("Second number: ")

            try:
                result = calculate(a, b, "/")
                print(f"Result: {result:.2f}")
                history.append(result)
            except ZeroDivisionError as error:
                print("Error:", error)

        elif choice == "5":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            c = get_number("Third number: ")

            result = average(a, b, c)
            print(f"Average: {result:.2f}")
            history.append(result)

        elif choice == "6":
            marks = get_number("Enter marks: ")

            try:
                grade = grade_from_marks(marks)
                print(f"Grade: {grade}")
            except ValueError as error:
                print("Error:", error)

        elif choice == "7":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )

        else:
            print("Invalid menu choice. Try again.")


if __name__ == "__main__":
    main()

demonstrate_scope()