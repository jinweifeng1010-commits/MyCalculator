"""
MyCalculator - A Simple Python Calculator
A basic calculator application with support for basic arithmetic operations
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("        Welcome to MyCalculator!")
    print("="*40)
    print("Select operation:")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Power          (**)")
    print("6. Exit")
    print("="*40 + "\n")

def main():
    """Main calculator loop"""
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5/6): ").strip()

        if choice == '6':
            print("\nThank you for using MyCalculator! Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}\n")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}\n")
                elif choice == '3':
                    print(f"\n{num1} * {num2} = {multiply(num1, num2)}\n")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}\n")
                elif choice == '5':
                    print(f"\n{num1} ** {num2} = {power(num1, num2)}\n")
            except ValueError:
                print("\nInvalid input! Please enter valid numbers.\n")
        else:
            print("\nInvalid choice! Please enter a valid option (1-6).\n")

if __name__ == "__main__":
    main()
