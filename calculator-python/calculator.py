# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
print(f"Debug: num1 = {num1}")
num2 = float(input("Enter the second number: "))
print(f"Debug: num2 = {num2}")

# Ask the user to input a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")
print(f"Debug: operation = {operation}")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print(f"Debug: result = {result}")
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Debug: result = {result}")
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Debug: result = {result}")
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Debug: result = {result}")
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation.")