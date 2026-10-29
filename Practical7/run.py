from staff_app import Department, Developer, Manager, Employee


def main():
    engineering = Department("Engineering")

    dev = Developer("Deeya", "EMP101", engineering, "Python")
    dev.salary = 65000

    manager = Manager("Ryane", "EMP102", engineering, 5)
    manager.salary = 90000

    engineering.add_employee(dev)
    engineering.add_employee(manager)

    print(dev.describe())
    print("Salary:", dev.salary)

    print(manager.describe())
    print("Salary:", manager.salary)

    print("\nDepartment Summary:")
    print(engineering.summary())

    try:
        dev.salary = -100
    except ValueError as error:
        print("\nValidation:", error)

    try:
        employee = Employee("   ", "EMP103", engineering)
    except ValueError as error:
        print("Validation:", error)


if __name__ == "__main__":
    main()