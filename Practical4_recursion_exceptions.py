class InvalidInputError(Exception):
    pass


def factorial(n):
    try:
        if n < 0:
            raise ValueError("n must be non-negative")

        if n == 0 or n == 1:
            return 1

        return n * factorial(n - 1)

    except ValueError as error:
        print(f"Factorial error: {error}")
        return None


def recursive_search(items, target, index=0):
    if index >= len(items):
        return -1

    if items[index] == target:
        return index

    return recursive_search(items, target, index + 1)


def read_non_negative_integer():
    raw = input("Enter a non-negative integer: ")

    try:
        value = int(raw)

        if value < 0:
            raise InvalidInputError("Number cannot be negative.")

    except ValueError:
        print("Input error: enter a whole number, such as 4.")
        return None

    except InvalidInputError as error:
        print(f"Validation error: {error}")
        return None

    else:
        print("Input accepted.")
        return value

    finally:
        print("Input validation attempt finished.")


def factorial_buggy(n):
    if n == 0:
        return 0

    return n * factorial_buggy(n - 1)


number = read_non_negative_integer()

print("Index of 8:", recursive_search([8, 3, 12], 8))
print("Index of 12:", recursive_search([8, 3, 12], 12))
print("Index of 5:", recursive_search([8, 3, 12], 5))

print("Factorial(0):", factorial(0))
print("Factorial(5):", factorial(5))
print("Factorial(-2):", factorial(-2))
