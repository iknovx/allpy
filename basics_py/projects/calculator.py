from math import sqrt
import time

CHOICES = {"1", "2", "3", "4", "5", "6"}
SINGLE_NUMBER_CHOICES = {"5", "6"}


def get_number(prompt):
    """Ask for a number, retry until a valid one is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.\n")


def calculator():
    while True:
        print("Simple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Calculate Square")
        print("6. Calculate Square Root")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "7":
            print("Exiting the calculator.")
            break

        if choice not in CHOICES:
            print("Invalid choice, please try again.\n")
            continue

        if choice in SINGLE_NUMBER_CHOICES:
            a = get_number("Enter a number: ")
            b = None
        else:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

        match choice:
            case "1":
                print(f"{a} + {b} = {a + b}")
            case "2":
                print(f"{a} - {b} = {a - b}")
            case "3":
                print(f"{a} * {b} = {a * b}")
            case "4":
                if b != 0:
                    print(f"{a} / {b} = {a / b}")
                else:
                    print("Error: Division by zero")
            case "5":
                print(f"The square of {a} is {a ** 2}")
            case "6":
                if a < 0:
                    print("Error: cannot take the square root of a negative number")
                else:
                    print(f"The square root of {a} is {sqrt(a)}")

        print()

        again = input("Do you want to calculate something else? (y/n): ").strip().lower()
        time.sleep(0.5)
        if again != "y":
            print("Exiting the calculator.")
            break


