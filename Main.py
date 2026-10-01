from operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulus,
    square_root
)

from history import add_to_history, show_history


def calculator():
    while True:

        print("\n======================")
        print("     CALCULATOR")
        print("======================")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. History")
        print("9. Exit")

        choice = input("\nEnter choice: ")

        if choice == "9":
            print("Goodbye!")
            break

        if choice == "8":
            show_history()
            continue

        try:

            if choice == "7":

                number = float(input("Enter number: "))

                result = square_root(number)

                expression = f"√{number}"

            elif choice in ["1", "2", "3", "4", "5", "6"]:

                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                    expression = f"{a} + {b}"

                elif choice == "2":
                    result = subtract(a, b)
                    expression = f"{a} - {b}"

                elif choice == "3":
                    result = multiply(a, b)
                    expression = f"{a} × {b}"

                elif choice == "4":
                    result = divide(a, b)
                    expression = f"{a} ÷ {b}"

                elif choice == "5":
                    result = power(a, b)
                    expression = f"{a} ^ {b}"

                elif choice == "6":
                    result = modulus(a, b)
                    expression = f"{a} % {b}"

            else:
                print("Invalid choice.")
                continue

            print(f"\nResult: {result}")

            add_to_history(expression, result)

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    calculator()