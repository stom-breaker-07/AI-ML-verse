def calculator(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b if b != 0 else 'Undefined (division by zero)'}")
    print(f"Modulus: {a} % {b} = {a % b if b != 0 else 'Undefined (modulus by zero)'}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print(f"Floor Division: {a} // {b} = {a // b if b != 0 else 'Undefined (floor division by zero)'}")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calculator(a, b)

