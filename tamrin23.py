def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as error1:
        print(f"Error: Division by zero is not allowed. ({error1})")
        return None


continue_program = True
while continue_program:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        calculated_result = divide(num1, num2)

        if calculated_result is not None:
            print("Result:", calculated_result)
            continue_program = False

    except ValueError as error2:
        print(f"Error: Invalid input. Please enter numbers only. ({error2})")

print("The program was successfully implemented.!")
