def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        print("\nChoose the operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        operation = input("Enter your choice (1/2/3/4/5): ")
        
        if operation == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid operation choice. Please try again.")

if __name__ == "__main__":
    main()
