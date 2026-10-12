def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


def even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"


def percentage(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return (num1 / num2) * 100



while True:
        print("Select an operation: ")
        print("1. Addition(+)")
        print("2. Subtraction(-)")
        print("3. Multiplication(*)")
        print("4. Division(/)")
        print("5. Check Even/Odd")
        print("6. Calculate percentage")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        
        if choice < 1 or choice > 7:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == 7:
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice == 1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == 5:
            num = int(input("Enter a number to check even/odd: "))
            print(f"The number {num} is {even_odd(num)}")
        elif choice == 6:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Percentage of {num1} and {num2}: {percentage(num1, num2)}%")


