"""
Description:
Create a calculator that can add, subtract, multiply, and divide numbers.
Optional: Add advanced operations like exponent, modulus, or square root.

Sample Input/Output:
Select operation (+, -, *, /): +
Enter first number: 5
Enter second number: 3
Result: 8
"""


def add(first_number, second_number):
    result = first_number + second_number
    display_result(result)

def sub(first_number, second_number):
    result = first_number - second_number
    display_result(result)


def multiply(first_number, second_number):
    result = first_number * second_number
    display_result(result)


def divide(first_number, second_number):
    if (second_number == 0):
        print("Sorry ,division by zero is undefined.")
    if (second_number > 0):
        result = first_number / second_number
        display_result(result)

def display_result(result):
    print(f"Result : {result:.2f}")

def calculate():
    operation = 0
    operation = int(input("\nMenu\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\nSelect your operation: (1-4): "))
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    if operation == 1:
        add(first_number, second_number)
    elif operation == 2:
        sub(first_number, second_number)
    elif operation == 3:
        multiply(first_number, second_number)
    elif operation == 4:
        divide(first_number, second_number)
    choice = input("Do you want to continue (y/n): ").lower()
    if choice == 'y':
        calculate()
    elif choice =='n':
        print("Thank you! ")
        exit(0)

print("Welcome to the Calculator! \nWhere your problems are not solved, merely quantified :)")
calculate()
