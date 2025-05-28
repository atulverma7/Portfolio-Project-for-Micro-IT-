def calculator():
    while True:
        print("\n1. Addition")
        print("2. Multiplication")
        print("3. Division")
        print("4. Remainder")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a + b
            print(f"Result: {a} + {b} = {result}")

        elif choice == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = a * b
            print(f"Result: {a} * {b} = {result}")

        elif choice == 3:
            a = int(input("Enter numerator: "))
            b = int(input("Enter denominator: "))
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = a / b
                print(f"Result: {a} / {b} = {result:.2f}")

        elif choice == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = a % b
                print(f"Result: {a} % {b} = {result}")

        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
calculator()
