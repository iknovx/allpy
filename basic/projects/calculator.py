print("Welcome to the calculator!")
print("You can perform addition (+), subtraction (-), multiplication (*), and division (/).")
num1 = float(input("Enter the first number: ")) # Get user input for the first number and convert it to a float
num2 = float(input("Enter the second number: ")) # Get user input for the second
operation = input("Enter the operation (+, -, *, /): ") # Get user input for the operation
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0: # Check for division by zero
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.") 