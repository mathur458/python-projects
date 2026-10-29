class BankAccount:
    def __init__(self, holder, account_number, opening_balance=0.0):
        if not holder.strip():
            raise ValueError("Account holder cannot be blank")

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)

    def transfer_to(self, other_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        other_account._balance += amount

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit must be positive")

            self._balance += amount

        except ValueError as e:
            print("Error:", e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal must be positive")

            if amount > self._balance:
                raise ValueError("Insufficient funds")

            self._balance -= amount

        except ValueError as e:
            print("Error:", e)

    def __str__(self):
        return f"BankAccount({self.holder}, balance={self._balance:.2f})"

    def __repr__(self):
        return (
            f"BankAccount(holder={self.holder!r}, "
            f"account_number={self.account_number!r}, "
            f"opening_balance={self._balance!r})"
        )

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self._balance + other._balance


account1 = BankAccount("Asha", "BA101", 1500)
account2 = BankAccount("Kabir", "BA102", 500)

account1.deposit(250)
account2.withdraw(100)

print(account1)
print(repr(account1))
print(account1.get_balance())

account1.withdraw(2000)
account2.deposit(0)

print(account1 + account2)

account1.transfer_to(account2, 300)

print(account1)
print(account2)

print("-------STUDENT CLASS-------")

class Student:
    def __init__(self, name, rollno, marks):

        self.name= name
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return f"Student({self.name}, rollno={self.rollno:.2f})"

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"rollno={self.rollno!r}, "
            f"marks={self.marks!r})"
        )

s1 = Student("Deeya",104,100)

print(s1)
print(repr(s1))