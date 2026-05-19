def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def show_menu():
    print("\n" + "=" * 30)
    print("SIMPLE CALCULATOR")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operation = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"
        else:
            result = divide(num1, num2)
            operation = "/"

        print(f"Result: {num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    main()
