class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def summary(self):
        total_salary = sum(employee.salary for employee in self.employees)

        return (
            f"Department: {self.name}\n"
            f"Employees: {len(self.employees)}\n"
            f"Total Salary: {total_salary}"
        )

    def __str__(self):
        return self.name